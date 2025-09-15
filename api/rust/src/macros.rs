#[macro_export]
macro_rules! collect_enum_into_map {
        ($map: ident, $rng: expr, $type: path, $offset: ident) => {
            for i in $rng {
                let Ok(d) = <$type>::try_from(i as i32) else {
                    continue;
                };
                $map.insert($offset + i, d.as_str_name());
            }
            #[allow(unused_assignments)]
            {
                $offset += $rng.len() as u32;
            }
        };
        ($width: literal, $($types: path),+) => {
            {
                extern crate alloc;
                use alloc::collections::BTreeMap;
                let mut map = BTreeMap::new();
                let mut offset: u32 = 0;
                $(
                    $crate::collect_enum_into_map!(map, 0..$width, $types, offset);
                )+
                map
            }
        };
        ($width: literal, $($types: path),+,) => {
            $crate::collect_enum_into_map!($width, $($types),+)
        }

    }

#[cfg(test)]
mod tests {

    #[cfg(feature = "std")]
    #[test]
    fn test_collect_enum_into_map() {
        extern crate alloc;
        let modes = crate::collect_enum_into_map!(
            16,
            crate::model::pcs::v1::three_phase_pcs_part::St,
            // crate::model::pcs::three_phase_pcs_part::Warning,
        );
        println!("{modes:#?}");
    }
}
