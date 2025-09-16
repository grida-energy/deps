use std::{env, path::PathBuf};

use std::{fs, path::Path};
fn sync_proto_files() -> Result<(), Box<dyn std::error::Error>> {
    let out_dir = env::var("CARGO_MANIFEST_DIR").unwrap();
    let target = Path::new(&out_dir).join("protos");
    let source = Path::new(&out_dir).join("../protos/deps");

    // rm -rf protos
    let _ = fs::remove_dir_all(&target);

    // mkdir protos
    fs::create_dir_all(&target).expect("fail to create protos directory");

    // cp -r ../protos/deps protos/deps
    let dest = target.join("deps");
    copy_dir_all(&source, &dest).expect("fail to copy deps");

    println!("cargo:rerun-if-changed={}", source.display());

    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    sync_proto_files()?;

    let packages: Vec<Package> = vec![
        ("deps/model/esd", "v0".into(), "**/*.v0.proto", &[]),
        ("deps/model/esd", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/model/nameplate", "v0".into(), "**/*.v0.proto", &[]),
        ("deps/model/nameplate", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/model/net", "v0".into(), "**/*.v0.proto", &[]),
        ("deps/model/net", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/model/pcs", "v0".into(), "**/*.v0.proto", &[]),
        ("deps/model/pcs", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/model/pms", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/model/source", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/model/collections", None, "**/*.proto", &[]),
        ("deps/preset/bess", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/preset/upms", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/rpc", "v1".into(), "**/*.v1.proto", &[]),
        ("deps/vnd", "v1".into(), "**/*.v1.proto", &[]),
    ];

    build_protos(&packages)?;

    Ok(())
}

pub type Package = (
    &'static str,
    Option<&'static str>,
    &'static str,
    &'static [&'static str],
);

pub fn build_protos(packages: &[Package]) -> Result<(), Box<dyn core::error::Error>> {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("protos");
    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());
    let well_known_types_path = "::pbs::wkt";

    for &packgage_item in packages.into_iter() {
        let (pivot_dir, sub_package, glob_pattern, deps) = packgage_item;

        let proto_file_path = root.join(pivot_dir);
        let package_sub_dir = {
            match sub_package {
                Some(sub) => format!("{}/{}", pivot_dir, sub),
                None => pivot_dir.to_string(),
            }
        };
        let package_out_dir = out_dir.join(package_sub_dir);
        std::fs::create_dir_all(&*package_out_dir).unwrap();
        let descriptor_path = package_out_dir.join("proto_descriptor.bin");

        let proto_files: Vec<_> =
            glob::glob(&format!("{}/{}", proto_file_path.display(), glob_pattern))
                .expect("fail to read glob pattern")
                .filter_map(Result::ok)
                .map(|path| path.to_string_lossy().to_string())
                .collect();
        if proto_files.is_empty() {
            continue;
        }

        for proto_file in &proto_files {
            println!("cargo:rerun-if-changed={}", proto_file);
        }

        let mut prost_conf = prost_build::Config::new();
        prost_conf.btree_map(&["."]);
        // .type_attribute(
        //     ".",
        //     "#[cfg_attr(feature = \"serde\", derive(serde::Serialize,serde::Deserialize))]",
        // );
        prost_conf
            .out_dir(&*package_out_dir)
            .file_descriptor_set_path(&descriptor_path)
            .compile_well_known_types()
            .extern_path(".google.protobuf", well_known_types_path);
        for dep in deps {
            let ext_path = format!(".{}", dep);
            let rust_path = format!("crate::{}", dep);
            prost_conf.extern_path(&*ext_path, &*rust_path);
            // pbjson_conf.extern_path(&*ext_path, &*rust_path);
        }
        prost_conf.compile_protos(&proto_files, &[&*root])?;

        #[cfg(feature = "serde-json")]
        {
            // let package_ext = format!(".eps.{}", package_dir.replace("/", "."));
            let pb_package = pivot_dir.replace("/", ".");
            let package_ext = format!(".{}", pb_package);
            let descriptor_set = std::fs::read(descriptor_path)?;
            let mut pbjson_conf = pbjson_build::Builder::new();
            pbjson_conf
                .btree_map(["."])
                .register_descriptors(&descriptor_set)?
                .ignore_unknown_fields()
                .out_dir(&*package_out_dir);
            for dep in deps {
                let ext_path = format!(".{}", dep);
                let rust_path = format!("crate::{}", dep);
                // prost_conf.extern_path(&*ext_path, &*rust_path);
                pbjson_conf.extern_path(&*ext_path, &*rust_path);
            }
            pbjson_conf.build(&[&*package_ext])?;
        }
    }

    // prost_build::compile_protos(&["protos/meter/compact.proto"], &["protos/"])?;
    Ok(())
}

fn copy_dir_all(src: &Path, dst: &Path) -> std::io::Result<()> {
    fs::create_dir_all(dst)?;
    for entry in fs::read_dir(src)? {
        let entry = entry?;
        let file_type = entry.file_type()?;
        let dest_path = dst.join(entry.file_name());
        if file_type.is_dir() {
            copy_dir_all(&entry.path(), &dest_path)?;
        } else {
            fs::copy(&entry.path(), &dest_path)?;
        }
    }
    Ok(())
}
