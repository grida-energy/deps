use once_cell::sync::Lazy;
use prost_reflect::DescriptorPool;

pub static DESCRIPTOR_POOL: Lazy<DescriptorPool> = Lazy::new(|| {
    DescriptorPool::decode(
        // include_bytes!(concat!(env!("OUT_DIR"), "/file_descriptor_set.bin")).as_ref(),
        include_bytes!(concat!(env!("OUT_DIR"), "/proto_descriptor.bin")).as_ref(),
    )
    .unwrap()
});

#[cfg(test)]
mod tests {
    use prost_reflect::ReflectMessage;

    #[test_log::test]
    fn test_fullpath() -> anyhow::Result<()> {
        let desc = crate::model::pcs::v1::ThreePhasePcsPart::default().descriptor();

        tracing::info!("={}", desc.full_name());

        Ok(())
    }
}
