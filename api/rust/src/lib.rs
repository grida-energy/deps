#![cfg_attr(not(feature = "std"), no_std)]
#![feature(try_blocks)]
#![feature(trim_prefix_suffix)]

extern crate alloc;

mod macros;
mod payloads;

#[cfg(feature = "pub-deps")]
pub mod deps;

mod voca {
    use alloc::{format, string::String};

    #[macro_export]
    macro_rules! include_proto_package {
        ($dir:literal, $package:literal) => {
            include!(concat!(env!("OUT_DIR"), "/", $dir, "/", $package, ".rs"));
            #[cfg(feature = "serde-json")]
            include!(concat!(
                env!("OUT_DIR"),
                "/",
                $dir,
                "/",
                $package,
                ".serde.rs"
            ));
            // pub const DESCRIPTOR: &[u8] = tonic::include_file_descriptor_set!("api/proto_descriptor");
        };
    }

    #[macro_export]
    macro_rules! impl_packet {
        ($st:path, $hd: path, $pl:path, $mx: path) => {
            impl $crate::rpc::v1::HasHeader for $st {
                type Header = $hd;
                fn get_header(&self) -> Option<&Self::Header> {
                    self.header.as_ref()
                }
            }
            impl $crate::rpc::v1::HasData for $st {
                type Data = $pl;
                fn get_data(&self) -> &Self::Data {
                    &self.payload
                }
            }
            impl $mx for $st {
                fn build(header: Option<$hd>, payload: $pl) -> Self {
                    $st {
                        header: header,
                        payload: payload,
                    }
                }
            }
        };
        (@request, $st:path, $pl:ty) => {
            $crate::voca::impl_packet!(
                $st,
                $crate::rpc::v1::Request,
                $pl,
                crate::rpc::v1::MixinRequest<$pl>
            );
        };
        (@response, $st:path, $pl:ty) => {
            $crate::voca::impl_packet!(
                $st,
                $crate::rpc::v1::Response,
                $pl,
                $crate::rpc::v1::MixinResponse<$pl>
            );
        };
        (@measure, $st:path) => {
            impl $crate::preset::StampedData for $st {
                fn timestamp(&self) -> pbs::wkt::Timestamp {
                    (self.timestamp).unwrap_or_default()
                }
            }
        };
    }

    pub use impl_packet;
    pub use include_proto_package;

    #[derive(Debug, Clone, PartialEq, Eq, Hash)]
    pub enum TopicKind {
        Measure,
        Command,
        VndParam,
        VndParamMeta,
        VndAlarm,
        VndAlarmMeta,
    }
    const _: () = {
        impl TopicKind {
            pub const fn as_str(&self) -> &str {
                match self {
                    TopicKind::Measure => "measure",
                    TopicKind::Command => "command",
                    TopicKind::VndParam => "vnd/param",
                    TopicKind::VndParamMeta => "vnd/param-meta",
                    TopicKind::VndAlarm => "vnd/alarm",
                    TopicKind::VndAlarmMeta => "vnd/alarm-meta",
                }
            }
        }
    };

    #[derive(Debug, Clone)]
    pub struct PresetTopics<T>(pub T);
    impl<T> PresetTopics<T> {
        pub const MEASURE: &str = TopicKind::Measure.as_str();
        pub const COMMAND: &str = TopicKind::Command.as_str();
        pub const VND_PARAM: &str = TopicKind::VndParam.as_str();
        pub const VND_PARAM_META: &str = TopicKind::VndParamMeta.as_str();
        pub const VND_ALARM: &str = TopicKind::VndAlarm.as_str();
        pub const VND_ALARM_META: &str = TopicKind::VndAlarmMeta.as_str();
    }
    impl<T: core::ops::Deref<Target = str>> PresetTopics<T> {
        pub fn subtopic_of<'t>(&self, topic: &'t str) -> Option<&'t str> {
            if !topic.starts_with(&*self.0) {
                return None;
            }
            Some(topic[self.0.len()..].trim_prefix('/'))
        }
        pub fn subtopic_kind_of<'t>(&self, topic: &'t str) -> Option<TopicKind> {
            self.subtopic_of(topic)
                .and_then(|d| match d.to_lowercase().as_str() {
                    Self::MEASURE => Some(TopicKind::Measure),
                    Self::COMMAND => Some(TopicKind::Command),
                    Self::VND_PARAM => Some(TopicKind::VndParam),
                    Self::VND_PARAM_META => Some(TopicKind::VndParamMeta),
                    Self::VND_ALARM => Some(TopicKind::VndAlarm),
                    Self::VND_ALARM_META => Some(TopicKind::VndAlarmMeta),
                    _ => None,
                })
        }

        pub fn any(&self) -> String {
            format!("{}/{}", &*self.0, "#")
        }
        pub fn measure(&self) -> String {
            format!("{}/{}", &*self.0, Self::MEASURE)
        }
        pub fn command(&self) -> String {
            format!("{}/{}", &*self.0, Self::COMMAND)
        }
        pub fn vnd_param(&self) -> String {
            format!("{}/{}", &*self.0, Self::VND_PARAM)
        }
        pub fn vnd_param_meta(&self) -> String {
            format!("{}/{}", &*self.0, Self::VND_PARAM_META)
        }
        pub fn vnd_alarm(&self) -> String {
            format!("{}/{}", &*self.0, Self::VND_ALARM)
        }
        pub fn vnd_alarm_meta(&self) -> String {
            format!("{}/{}", &*self.0, Self::VND_ALARM_META)
        }
    }
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_topic() -> anyhow::Result<()> {
            let dev_id = "test_device";
            let topics = PresetTopics(dev_id);
            assert_eq!(topics.measure(), format!("{}/measure", dev_id));
            assert_eq!(topics.command(), format!("{}/command", dev_id));
            assert_eq!(topics.vnd_param(), format!("{}/vnd/param", dev_id));
            assert_eq!(
                topics.vnd_param_meta(),
                format!("{}/vnd/param-meta", dev_id)
            );
            assert_eq!(topics.vnd_alarm(), format!("{}/vnd/alarm", dev_id));
            assert_eq!(
                topics.vnd_alarm_meta(),
                format!("{}/vnd/alarm-meta", dev_id)
            );
            Ok(())
        }
    }
}
pub use voca::{PresetTopics, TopicKind};

pub mod rpc {
    pub mod v1 {
        crate::voca::include_proto_package!("deps/rpc/v1", "deps.rpc.v1");
        pub type Result<T> = core::result::Result<T, response::Error>;
        pub trait HasHeader {
            type Header;
            fn get_header(&self) -> Option<&Self::Header>;
        }
        pub trait HasData {
            type Data;
            fn get_data(&self) -> &Self::Data;
        }
        pub trait MixinRequest<T>: HasHeader<Header = Request> + HasData<Data = T> {
            fn build(header: Option<Self::Header>, data: Self::Data) -> Self;
            // fn get_header(&self) -> Option<&Request>;
            // fn get_data(&self) -> &T;
        }
        pub trait MixinResponse<T>: HasHeader<Header = Response> + HasData<Data = T> {
            fn build(header: Option<Self::Header>, data: Self::Data) -> Self;
            // fn get_header(&self) -> Option<&Response>;
            // fn get_data(&self) -> &T;
        }

        pub trait MixinPacket<T> {
            fn ok(uuid: impl Into<alloc::string::String>, data: T) -> Self;
            fn error(
                uuid: impl Into<alloc::string::String>,
                error: (
                    crate::rpc::v1::response::ErrorCode,
                    impl Into<alloc::string::String>,
                ),
                data: T,
            ) -> Self;
        }
        const _: () = {
            impl<T, RQ> MixinPacket<T> for RQ
            where
                RQ: MixinResponse<T>,
            {
                fn ok(uuid: impl Into<alloc::string::String>, data: T) -> Self {
                    Self::build(Response::ok(uuid).into(), data)
                }
                fn error(
                    uuid: impl Into<alloc::string::String>,
                    error: (
                        crate::rpc::v1::response::ErrorCode,
                        impl Into<alloc::string::String>,
                    ),
                    data: T,
                ) -> Self {
                    Self::build(Response::error(uuid, error).into(), data)
                }
            }
        };

        const _: () = {
            impl Request {}
            impl Response {
                pub fn new(
                    uuid: impl Into<alloc::string::String>,
                    error: Option<(response::ErrorCode, impl Into<alloc::string::String>)>,
                ) -> Self {
                    Response {
                        uuid: uuid.into(),
                        error: error.map(|(code, detail)| response::Error::new(code, detail)),
                    }
                }
                pub fn error(
                    uuid: impl Into<alloc::string::String>,
                    error: (response::ErrorCode, impl Into<alloc::string::String>),
                ) -> Self {
                    Response::new(uuid, error.into())
                }
                pub fn ok(uuid: impl Into<alloc::string::String>) -> Self {
                    Response::new(
                        uuid,
                        Option::<(response::ErrorCode, alloc::string::String)>::None,
                    )
                }
            }

            impl response::Error {
                pub fn new(
                    code: response::ErrorCode,
                    detail: impl Into<alloc::string::String>,
                ) -> Self {
                    response::Error {
                        code: code as i32,
                        detail: detail.into(),
                    }
                }
            }
        };
    }
}
pub mod vnd {
    pub mod v1 {
        crate::voca::include_proto_package!("deps/vnd/v1", "deps.vnd.v1");
        impl ParamIdRange {
            pub fn end(&self) -> u32 {
                self.start + self.length
            }
        }
        impl core::iter::IntoIterator for ParamIdRange {
            type Item = u32;
            type IntoIter = core::ops::Range<u32>;

            fn into_iter(self) -> Self::IntoIter {
                self.start..self.end()
            }
        }
        const _: () = {
            crate::voca::impl_packet!(@request, rpc::ParamRequest, Option<rpc::ParamReadWriteRequest>);
            crate::voca::impl_packet!(@response, rpc::ParamResponse, Option<rpc::ParamReadWriteResponse>);
            crate::voca::impl_packet!(@measure, rpc::AlarmResponse);
        };
    }
}
pub mod model {
    pub mod esd {
        pub mod v0 {
            crate::voca::include_proto_package!("deps/model/esd/v0", "deps.model.esd.v0");
        }
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/esd/v1", "deps.model.esd.v1");
            crate::voca::impl_packet!(@request, rpc::bank::CommandRequest, alloc::vec::Vec<esd_bank::Command>);
            crate::voca::impl_packet!(@response, rpc::bank::CommandResponse, u32);
            crate::voca::impl_packet!(@measure, rpc::bank::MeasureResponse);
        }
    }
    pub mod net {
        pub mod v0 {
            crate::voca::include_proto_package!("deps/model/net/v0", "deps.model.net.v0");
        }
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/net/v1", "deps.model.net.v1");
        }
    }
    pub mod nameplate {
        pub mod v0 {
            crate::voca::include_proto_package!(
                "deps/model/nameplate/v0",
                "deps.model.nameplate.v0"
            );
        }
        pub mod v1 {
            crate::voca::include_proto_package!(
                "deps/model/nameplate/v1",
                "deps.model.nameplate.v1"
            );
        }
    }
    pub mod pcs {
        pub mod v0 {
            crate::voca::include_proto_package!("deps/model/pcs/v0", "deps.model.pcs.v0");
        }
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/pcs/v1", "deps.model.pcs.v1");
            crate::voca::impl_packet!(@request, rpc::pcs::CommandRequest, alloc::vec::Vec<three_phase_pcs_part::Command>);
            crate::voca::impl_packet!(@response, rpc::pcs::CommandResponse, u32);
            crate::voca::impl_packet!(@measure, rpc::pcs::MeasureResponse);
            crate::voca::impl_packet!(@request, rpc::dc_dc::CommandRequest, alloc::vec::Vec<dc_dc_converter::Command>);
            crate::voca::impl_packet!(@response, rpc::dc_dc::CommandResponse, u32);
            crate::voca::impl_packet!(@measure, rpc::dc_dc::MeasureResponse);
            crate::voca::impl_packet!(@measure, rpc::grid::MeasureResponse);
        }
    }
    pub mod source {
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/source/v1", "deps.model.source.v1");
        }
    }
    pub mod tsdb {
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/tsdb/v1", "deps.model.tsdb.v1");
        }
    }
    pub mod pms {
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/pms/v1", "deps.model.pms.v1");

            const _: () = {
                impl From<&(Option<f64>, Option<f64>)> for MinMax {
                    fn from(value: &(Option<f64>, Option<f64>)) -> Self {
                        MinMax {
                            min: value.0,
                            max: value.1,
                        }
                    }
                }
                impl From<(Option<f64>, Option<f64>)> for MinMax {
                    fn from(value: (Option<f64>, Option<f64>)) -> Self {
                        (&value).into()
                    }
                }
                impl From<&MinMax> for (Option<f64>, Option<f64>) {
                    fn from(value: &MinMax) -> Self {
                        (value.min, value.max)
                    }
                }
                impl From<MinMax> for (Option<f64>, Option<f64>) {
                    fn from(value: MinMax) -> Self {
                        (&value).into()
                    }
                }

                impl From<&(f64, f64)> for Point2D {
                    fn from(value: &(f64, f64)) -> Self {
                        Point2D {
                            x: value.0,
                            y: value.1,
                        }
                    }
                }
                impl From<(f64, f64)> for Point2D {
                    fn from(value: (f64, f64)) -> Self {
                        (&value).into()
                    }
                }
                impl From<&Point2D> for (f64, f64) {
                    fn from(value: &Point2D) -> Self {
                        (value.x, value.y)
                    }
                }
                impl From<Point2D> for (f64, f64) {
                    fn from(value: Point2D) -> Self {
                        (&value).into()
                    }
                }
            };
        }
    }
    pub mod rms {
        pub mod v1 {
            crate::voca::include_proto_package!("deps/model/rms/v1", "deps.model.rms.v1");
            crate::voca::impl_packet!(@request, rpc::CommandRequest, alloc::vec::Vec<local_rms::Command>);
            crate::voca::impl_packet!(@response, rpc::CommandResponse, u32);
            crate::voca::impl_packet!(@measure, rpc::MeasureResponse);
        }
    }
}

pub mod preset {
    pub trait StampedData {
        fn timestamp(&self) -> pbs::wkt::Timestamp;
    }

    pub mod bess {
        pub mod v1 {
            crate::voca::include_proto_package!("deps/preset/bess/v1", "deps.preset.bess.v1");
            const _: () = {
                crate::voca::impl_packet!(@request, rpc::CommandRequest, alloc::vec::Vec<BessCommand>);
                crate::voca::impl_packet!(@response, rpc::CommandResponse, u32);
                crate::voca::impl_packet!(@measure, rpc::MeasureResponse);
            };
        }
    }
    pub mod upms {
        pub mod v1 {
            crate::voca::include_proto_package!("deps/preset/upms/v1", "deps.preset.upms.v1");
            const _: () = {
                extern crate alloc;
                // use alloc::vec::Vec;

                crate::voca::impl_packet!(@request, rpc::CommandRequest, alloc::vec::Vec<PmsCommand>);
                crate::voca::impl_packet!(@response, rpc::CommandResponse, u32);
                crate::voca::impl_packet!(@measure, rpc::MeasureResponse);
            };
        }
    }
    pub mod dbserver {
        pub mod v1 {
            crate::voca::include_proto_package!(
                "deps/preset/dbserver/v1",
                "deps.preset.dbserver.v1"
            );
            crate::voca::impl_packet!(@request, rpc::PullLogRequest, Option<crate::model::tsdb::v1::LogConstraint>);
            crate::voca::impl_packet!(@response, rpc::PullLogResponse, alloc::vec::Vec<crate::model::tsdb::v1::LogItem>);
            crate::voca::impl_packet!(@request, rpc::PullMeasureRequest, Option<crate::model::tsdb::v1::MeasureConstraint>);
            crate::voca::impl_packet!(@response, rpc::PullMeasureResponse, alloc::vec::Vec<pbs::wkt::ListValue>);
        }
    }
}

const _: () = {
    extern crate alloc;
    use model::esd;
    impl From<esd::v1::esd_string::Fault> for esd::v1::esd_bank::Fault {
        fn from(value: esd::v1::esd_string::Fault) -> Self {
            esd::v1::esd_bank::Fault {
                other: value.other,
                over_temp: value.over_temp,
                under_temp: value.under_temp,
                over_charge_current: value.over_charge_current,
                over_discharge_current: value.over_discharge_current,
                over_volt: value.over_volt,
                under_volt: value.under_volt,
                under_soc_min: value.under_soc_min,
                over_soc_max: value.over_soc_max,
                voltage_imbalance: value.voltage_imbalance,
                temperature_imbalance: value.temperature_imbalance,
                current_imbalance: false,
                configuration: value.configuration,
                communication_error: value.communication_error,
                contactor_error: value.contactor_error,
                fan_error: value.fan_error,
                ground_fault: value.ground_fault,
            }
        }
    }
    impl From<esd::v1::esd_string::Warning> for esd::v1::esd_bank::Warning {
        fn from(value: esd::v1::esd_string::Warning) -> Self {
            esd::v1::esd_bank::Warning {
                other: value.other,
                over_temp: value.over_temp,
                under_temp: value.under_temp,
                over_charge_current: value.over_charge_current,
                over_discharge_current: value.over_discharge_current,
                over_volt: value.over_volt,
                under_volt: value.under_volt,
                under_soc_min: value.under_soc_min,
                over_soc_max: value.over_soc_max,
                voltage_imbalance: value.voltage_imbalance,
                temperature_imbalance: value.temperature_imbalance,
                current_imbalance: false,
                configuration: false,
            }
        }
    }
    impl From<esd::v1::esd_string::Status> for esd::v1::esd_bank::Status {
        fn from(value: esd::v1::esd_string::Status) -> Self {
            esd::v1::esd_bank::Status {
                other: value.other,
                open_door: value.open_door,
            }
        }
    }

    impl model::esd::v1::EsdBank {
        pub fn from_single_string(string: model::esd::v1::EsdString) -> Self {
            model::esd::v1::EsdBank {
                st: esd::v1::esd_bank::St::Na.into(),
                st_cha: esd::v1::esd_bank::StCha::Na.into(),

                a: string.a,
                v: string.v,
                w: string.a * string.v,
                a_cha_max: 0.,
                a_discha_max: 0.,

                dod: string.dod,
                soc: string.soc,
                soh: string.soh,
                n_cyc: string.n_cyc,

                fault: string.fault.map(Into::into),
                warning: string.warning.map(Into::into),
                status: string.status.map(Into::into),

                hb: 0,
                // set_op: {
                //     use esd::v1::esd_bank::command::SetOp;
                //     use esd::v1::esd_string::command::SetCon;
                //     use esd::v1::esd_string::command::SetEna;
                //     let ena = TryInto::<SetEna>::try_into(string.set_ena).unwrap_or(SetEna::Na);
                //     let con = TryInto::<SetCon>::try_into(string.set_con).unwrap_or(SetCon::Na);
                //     let op = match (ena, con) {
                //         (SetEna::EnableString, SetCon::ConnectString) => SetOp::Connect,
                //         (SetEna::Na, _) => SetOp::Na,
                //         (_, SetCon::Na) => SetOp::Na,
                //         _ => SetOp::Disconnect,
                //     };
                //     op as i32
                // },
                cnt_mod: string
                    .cnt_mod
                    .map(|cm| model::esd::v1::esd_bank::ModuleCount {
                        tmp_max: cm.tmp_max,
                        tmp_max_str: 1,
                        tmp_max_mod: cm.tmp_max_mod,
                        tmp_min: cm.tmp_min,
                        tmp_min_str: 1,
                        tmp_min_mod: cm.tmp_min_mod,
                        tmp_avg: cm.tmp_avg,
                    }),
                cnt_str: model::esd::v1::esd_bank::StringCount {
                    v_max: string.v,
                    v_max_str: 1,
                    v_min: string.v,
                    v_min_str: 1,
                    v_avg: string.v,
                    a_max: string.a,
                    a_max_str: 1,
                    a_min: string.a,
                    a_min_str: 1,
                    a_avg: string.a,
                    n_conn: if string.status.map(|d| d.contactor_status).unwrap_or(false) {
                        1
                    } else {
                        0
                    },
                }
                .into(),
                cnt_cell: None,
                strs: alloc::vec![string],
            }
        }
    }

    impl From<core::ops::Range<u32>> for vnd::v1::ParamIdRange {
        fn from(value: core::ops::Range<u32>) -> Self {
            vnd::v1::ParamIdRange {
                start: value.start,
                length: value.end.saturating_sub(value.start),
            }
        }
    }
};
const _: () = {
    extern crate alloc;
    impl From<rpc::v1::response::ErrorCode> for rpc::v1::response::Error {
        fn from(value: rpc::v1::response::ErrorCode) -> Self {
            rpc::v1::response::Error {
                code: value.into(),
                detail: alloc::string::String::new(),
            }
        }
    }
};

#[cfg(test)]
mod test {
    // use alloc::collections::BTreeMap;

    use prost::Message;

    #[test]
    fn test_protobuf() -> anyhow::Result<()> {
        extern crate alloc;
        use alloc::vec;

        let value = crate::model::net::v0::FlatMeterSinglePhase {
            a: 0.,
            v: 0.,
            w: 0.,
            va: 0.,
            var: 0.,
            pf: 0.,
            hz: 0.,
            tot_wh_imp: 1.,
            tot_wh_exp: 0.,
        };

        let mut buf = vec![];
        value
            .encode(&mut buf)
            .map_err(|e| anyhow::anyhow!("{e:?}"))?;
        tracing::info!("Encoded value: {:?}", buf);
        let decoded_value = crate::model::net::v0::FlatMeterSinglePhase::decode(&*buf)
            .map_err(|e| anyhow::anyhow!("{e:?}"))?;
        assert_eq!(value, decoded_value);
        Ok(())
    }

    #[cfg(feature = "serde-json")]
    #[cfg(feature = "std")]
    #[test_log::test]
    fn test_reqresp() -> anyhow::Result<()> {
        extern crate alloc;
        use crate::rpc;
        use crate::vnd;
        use alloc::string::ToString;
        use alloc::vec;

        // crate::rpc::response::ErrorCode::NotSupportedMessage

        // pbjson_types::Value

        let req = vnd::v1::rpc::ParamRequest {
            header: rpc::v1::Request {
                uuid: "test-uuid".to_string(),
                resp_topic: "test/response".to_string(),
            }
            .into(),
            payload: vnd::v1::rpc::ParamReadWriteRequest {
                reads: vec![(1..2).into()],
                writes: vnd::v1::ParamBlock {
                    ranges: vec![(1..2).into()],
                    values: vec![0f64.into()],
                }
                .into(),
            }
            .into(),
        };

        let json_str = serde_json::to_string_pretty(&req)?;
        tracing::info!("JSON Request: {json_str}");

        Ok(())
    }

    #[cfg(feature = "serde-json")]
    #[cfg(feature = "std")]
    #[test_log::test]
    fn test_pcs_measure() -> anyhow::Result<()> {
        extern crate alloc;
        use crate::model::pcs::v0::PcsThreePhase;

        let req = PcsThreePhase {
            a: 1.,
            pp_v_ph_ab: (230.).into(),
            var: (10.).into(),
            ..Default::default()
        };

        let json_str = serde_json::to_string_pretty(&req)?;
        tracing::info!("JSON Request: {json_str}");

        Ok(())
    }

    #[cfg(feature = "serde-json")]
    #[cfg(feature = "std")]
    #[test_log::test]
    fn test_pcs_command() -> anyhow::Result<()> {
        let cmds = vec![
            vec![
                10, 38, 18, 36, 102, 55, 52, 54, 51, 49, 48, 52, 45, 48, 54, 50, 51, 45, 52, 100,
                98, 97, 45, 97, 102, 49, 99, 45, 52, 101, 57, 101, 52, 48, 51, 49, 50, 102, 54, 57,
                18, 9, 18, 7, 18, 5, 29, 0, 0, 84, 66,
            ],
            vec![
                10, 38, 18, 36, 100, 54, 56, 101, 57, 56, 101, 54, 45, 51, 53, 53, 101, 45, 52, 97,
                98, 48, 45, 56, 53, 49, 51, 45, 48, 49, 55, 51, 101, 101, 99, 53, 52, 97, 56, 50,
                18, 9, 18, 7, 18, 5, 29, 0, 0, 0, 0,
            ],
        ];
        for cmd in cmds {
            let req = crate::preset::bess::v1::rpc::CommandRequest::decode(&*cmd)?;
            tracing::info!("Decoded Request: {req:?}");
        }
        Ok(())
    }

    #[test]
    fn test_mixin_error() -> anyhow::Result<()> {
        extern crate alloc;
        use crate::rpc::v1::MixinPacket;
        use crate::rpc::v1::response::ErrorCode;

        {
            let resp = crate::vnd::v1::rpc::ParamResponse::error(
                "test-uuid",
                (ErrorCode::NotSupportedMessage, "Not supported"),
                None,
            );

            tracing::info!("Error Response: {:?}", resp);
        }
        {
            let resp = crate::preset::bess::v1::rpc::CommandResponse::error(
                "test-uuid",
                (ErrorCode::InvalidParameter, "Internal error"),
                0,
            );
            tracing::info!("Error Response: {:?}", resp);
        }

        Ok(())
    }
}
