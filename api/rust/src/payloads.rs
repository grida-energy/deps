#[cfg(feature = "serde-json")]
#[cfg(test)]
mod tests {
    extern crate alloc;
    use alloc::{string::ToString, vec};

    use prost::Message;

    use crate::model::{esd, net, pcs, source};
    use crate::preset::bess;

    fn esd_bank_full() -> esd::v1::EsdBank {
        let bank = esd::v1::EsdBank {
            st: i32::MAX,
            st_cha: i32::MAX,
            cnt_mod: esd::v1::esd_bank::ModuleCount {
                tmp_max: f32::MAX,
                tmp_max_str: u32::MAX,
                tmp_max_mod: u32::MAX,
                tmp_min: f32::MAX,
                tmp_min_str: u32::MAX,
                tmp_min_mod: u32::MAX,
                tmp_avg: f32::MAX,
            }
            .into(),
            cnt_str: esd::v1::esd_bank::StringCount {
                v_max: f32::MAX,
                v_max_str: u32::MAX,
                v_min: f32::MAX,
                v_min_str: u32::MAX,
                v_avg: f32::MAX,
                a_max: f32::MAX,
                a_max_str: u32::MAX,
                a_min: f32::MAX,
                a_min_str: u32::MAX,
                a_avg: f32::MAX,
                n_conn: u32::MAX,
            }
            .into(),
            cnt_cell: esd::v1::esd_bank::CellCount {
                v_max: f32::MAX,
                v_max_str: u32::MAX,
                v_max_mod: u32::MAX,
                v_min: f32::MAX,
                v_min_str: u32::MAX,
                v_min_mod: u32::MAX,
                v_avg: f32::MAX,
                n_bal: u32::MAX,
            }
            .into(),
            soc: f32::MAX,
            dod: f32::MAX,
            soh: f32::MAX,
            n_cyc: u32::MAX,
            hb: u32::MAX,
            v: f32::MAX,
            a: f32::MAX,
            a_cha_max: f32::MAX,
            a_discha_max: f32::MAX,
            w: f32::MAX,
            status: esd::v1::esd_bank::Status {
                other: true,
                open_door: true,
            }
            .into(),
            warning: esd::v1::esd_bank::Warning {
                other: true,
                over_temp: true,
                under_temp: true,
                over_charge_current: true,
                over_discharge_current: true,
                over_volt: true,
                under_volt: true,
                under_soc_min: true,
                over_soc_max: true,
                voltage_imbalance: true,
                temperature_imbalance: true,
                current_imbalance: true,
                configuration: true,
            }
            .into(),
            fault: esd::v1::esd_bank::Fault {
                other: true,
                over_temp: true,
                under_temp: true,
                over_charge_current: true,
                over_discharge_current: true,
                over_volt: true,
                under_volt: true,
                under_soc_min: true,
                over_soc_max: true,
                voltage_imbalance: true,
                temperature_imbalance: true,
                current_imbalance: true,
                configuration: true,
                communication_error: true,
                contactor_error: true,
                fan_error: true,
                ground_fault: true,
            }
            .into(),
            strs: vec![],
        };
        bank
    }
    fn esd_str_full() -> esd::v1::EsdString {
        use esd::v1::esd_string;
        let esd_str = esd::v1::EsdString {
            con_fail: i32::MAX,
            soc: f32::MAX,
            dod: f32::MAX,
            n_cyc: u32::MAX,
            soh: f32::MAX,
            a: f32::MAX,
            v: f32::MAX,
            cnt_cell: esd_string::CellCount {
                v_max: f32::MAX,
                v_max_mod: u32::MAX,
                v_min: f32::MAX,
                v_min_mod: u32::MAX,
                v_avg: f32::MAX,
                n_cell_bal: u32::MAX,
            }
            .into(),
            cnt_mod: esd_string::ModuleCount {
                tmp_max: f32::MAX,
                tmp_max_mod: u32::MAX,
                tmp_min: f32::MAX,
                tmp_min_mod: u32::MAX,
                tmp_avg: f32::MAX,
            }
            .into(),
            st_con: esd_string::StCon {
                contactor_0: true,
                contactor_1: true,
                contactor_2: true,
                contactor_3: true,
                contactor_4: true,
                contactor_5: true,
                contactor_6: true,
                contactor_7: true,
                contactor_8: true,
                contactor_9: true,
                contactor_10: true,
                contactor_11: true,
                contactor_12: true,
                contactor_13: true,
                contactor_14: true,
                contactor_15: true,
                contactor_16: true,
                contactor_17: true,
                contactor_18: true,
                contactor_19: true,
                contactor_20: true,
                contactor_21: true,
                contactor_22: true,
                contactor_23: true,
                contactor_24: true,
                contactor_25: true,
                contactor_26: true,
                contactor_27: true,
                contactor_28: true,
                contactor_29: true,
                contactor_30: true,
            }
            .into(),
            status: esd_string::Status {
                other: true,
                open_door: true,
                string_enabled: true,
                contactor_status: true,
            }
            .into(),
            warning: esd_string::Warning {
                other: true,
                over_temp: true,
                under_temp: true,
                over_charge_current: true,
                over_discharge_current: true,
                over_volt: true,
                under_volt: true,
                under_soc_min: true,
                over_soc_max: true,
                voltage_imbalance: true,
                temperature_imbalance: true,
            }
            .into(),
            fault: esd_string::Fault {
                other: true,
                over_temp: true,
                under_temp: true,
                over_charge_current: true,
                over_discharge_current: true,
                over_volt: true,
                under_volt: true,
                under_soc_min: true,
                over_soc_max: true,
                voltage_imbalance: true,
                temperature_imbalance: true,
                communication_error: true,
                configuration: true,
                contactor_error: true,
                fan_error: true,
                ground_fault: true,
            }
            .into(),
            set_ena: i32::MAX,
            set_con: i32::MAX,
            mods: vec![],
        };
        esd_str
    }
    fn esd_module_full() -> esd::v1::EsdModule {
        use esd::v1::esd_module;
        let esd_mod = esd::v1::EsdModule {
            str_idx: u32::MAX,
            mod_idx: u32::MAX,
            n_cell: u32::MAX,
            soc: f32::MAX,
            dod: f32::MAX,
            soh: f32::MAX,
            n_cyc: u32::MAX,
            v: f32::MAX,
            cnt_cell: esd_module::CellCount {
                v_max: f32::MAX,
                v_max_cell: u32::MAX,
                v_min: f32::MAX,
                v_min_cell: u32::MAX,
                v_avg: f32::MAX,
                tmp_max: f32::MAX,
                tmp_max_cell: u32::MAX,
                tmp_min: f32::MAX,
                tmp_min_cell: u32::MAX,
                tmp_avg: f32::MAX,
                n_bal: u32::MAX,
            }
            .into(),
            sn: "0000_0000_0000_0000".to_string(),
            cells: vec![],
        };
        esd_mod
    }

    fn esd_cell_full() -> esd::v1::EsdCell {
        use esd::v1::esd_cell;

        let esd_cell = esd::v1::EsdCell {
            v: f32::MAX,
            tmp: f32::MAX,
            st: esd_cell::St { is_balancing: true }.into(),
        };
        esd_cell
    }

    fn pcs_full() -> pcs::v1::ThreePhasePcsPart {
        use pcs::v1::three_phase_pcs_part;
        let pcs_part = pcs::v1::ThreePhasePcsPart {
            st: three_phase_pcs_part::St::Starting as i32,
            status: three_phase_pcs_part::Status {
                other: true,
                ac_disconnect: true,
                dc_disconnect: true,
                grid_disconnect: true,
                manual_shutdown: true,
                open_door: true,
                throttled: true,
                mppt: true,
                under_cool: true,
                spd: true,
            }
            .into(),
            fault: three_phase_pcs_part::Fault {
                other: true,
                ac_over_volt: true,
                ac_under_volt: true,
                over_frequency: true,
                under_frequency: true,
                over_current: true,
                ground_fault: true,
                dc_over_volt: true,
                over_temp: true,
                under_temp: true,
                ac_unbalance_volt: true,
                ac_unbalance_current: true,
                hw_test_failure: true,
                cb_trip: true,
            }
            .into(),
            warning: three_phase_pcs_part::Warning {
                other: true,
                ac_over_volt: true,
                ac_under_volt: true,
                over_frequency: true,
                under_frequency: true,
                over_load: true,
                dc_over_volt: true,
                over_temp: true,
                under_temp: true,
                ac_unbalance_volt: true,
                ac_unbalance_current: true,
            }
            .into(),
            dir_pwr: three_phase_pcs_part::DirPwr::AcToDc as i32,
            ph_v: pcs::v1::ThreePhase {
                ph_a: f32::MAX,
                ph_b: f32::MAX,
                ph_c: f32::MAX,
            }
            .into(),
            pp_v: pcs::v1::ThreePhaseLine {
                ph_ab: f32::MAX,
                ph_bc: f32::MAX,
                ph_ca: f32::MAX,
            }
            .into(),
            a: pcs::v1::ThreePhaseNSum {
                ph_a: f32::MAX,
                ph_b: f32::MAX,
                ph_c: f32::MAX,
                sum: f32::MAX,
            }
            .into(),
            w: f32::MAX,
            hz: f32::MAX,
            va: f32::MAX,
            var: f32::MAX,
            pf: f32::MAX,
            dc: pcs::v1::DcPart {
                dca: f32::MAX,
                dcv: f32::MAX,
                dcw: f32::MAX,
            }
            .into(),
            tmp: pcs::v1::TemperaturePart {
                tmp_cab: f32::MAX,
                tmp_snk: f32::MAX,
                tmp_trns: f32::MAX,
                tmp_ot: vec![f32::MAX, f32::MAX, f32::MAX],
            }
            .into(),
        };
        pcs_part
    }
    fn ac_line_full() -> net::v1::AcLine {
        net::v1::AcLine {
            v: f32::MAX,
            a: f32::MAX,
            hz: f32::MAX,
            w: f32::MAX,
            va: f32::MAX,
            var: f32::MAX,
            pf: f32::MAX,
            wh: net::v1::Energy {
                exported: f64::MAX,
                imported: f64::MAX,
            }
            .into(),
        }
    }
    fn dc_line_full() -> net::v1::Line {
        net::v1::Line {
            v: f32::MAX,
            a: f32::MAX,
            w: f32::MAX,
            wh: net::v1::Energy {
                exported: f64::MAX,
                imported: f64::MAX,
            }
            .into(),
        }
    }

    fn grid_full() -> pcs::v1::ThreePhaseGridPart {
        pcs::v1::ThreePhaseGridPart {
            sum: net::v1::AcLineSum {
                a: f32::MAX,
                hz: f32::MAX,
                w: f32::MAX,
                va: f32::MAX,
                var: f32::MAX,
                pf: f32::MAX,
                wh: net::v1::Energy {
                    exported: f64::MAX,
                    imported: f64::MAX,
                }
                .into(),
            }
            .into(),
            a: ac_line_full().into(),
            b: ac_line_full().into(),
            c: ac_line_full().into(),
        }
    }
    fn dcdc_full() -> pcs::v1::DcDcConverter {
        use pcs::v1::dc_dc_converter;
        pcs::v1::DcDcConverter {
            st: dc_dc_converter::St::Na as i32,
            status: dc_dc_converter::Status { other: true }.into(),
            fault: dc_dc_converter::Fault { other: true }.into(),
            warning: dc_dc_converter::Warning { other: true }.into(),
            input: dc_line_full().into(),
            output: dc_line_full().into(),
        }
    }
    fn pv_some() -> source::v1::PvLine {
        source::v1::PvLine {
            strings: vec![source::v1::PvString {
                v: f32::MAX,
                a: f32::MAX,
                w: f32::MAX,
            }],
        }
    }
    fn only_hpcs_full() -> bess::v1::Bess {
        bess::v1::Bess {
            bank: None,
            pcs: pcs_full().into(),
            on_grid: grid_full().into(),
            off_grid: grid_full().into(),
            dcdc: dcdc_full().into(),
            pv: pv_some().into(),
        }
    }

    #[test_log::test]
    fn test_size() -> anyhow::Result<()> {
        tracing::info!("esd_bank_full size: {}", esd_bank_full().encoded_len());
        tracing::info!("esd_string size: {}", esd_str_full().encoded_len());
        tracing::info!("esd_module_max size: {}", esd_module_full().encoded_len());
        tracing::info!("esd_cell_max size: {}", esd_cell_full().encoded_len());
        tracing::info!("pcs_part size: {}", pcs_full().encoded_len());
        tracing::info!("only threephase meter: {}", grid_full().encoded_len());

        let mod_max = esd_module_full().encoded_len() + esd_cell_full().encoded_len() * 20;
        let rack_max = esd_str_full().encoded_len() + mod_max * 17;
        let bank_max = esd_bank_full().encoded_len() + rack_max * 1;
        tracing::info!(
            "esd_bank={}, rack_max={}, mod_max={}",
            bank_max,
            rack_max,
            mod_max
        );
        let bess_size = only_hpcs_full().encoded_len();
        tracing::info!("only_hpcs_full size: {}", bess_size);
        tracing::info!(
            "only_hpcs_full json size: {}",
            serde_json::to_string(&only_hpcs_full())?.as_bytes().len()
        );
        Ok(())
    }
    #[test]
    fn test_hvac() -> anyhow::Result<()> {
        mod hvac {
            #[derive(prost::Message)]
            pub struct Command {
                #[prost(bool, tag = "1")]
                pub dor: bool,
                #[prost(bool, tag = "2")]
                pub hp: bool,
                #[prost(bool, tag = "3")]
                pub lp: bool,
                #[prost(bool, tag = "4")]
                pub halon: bool,
                #[prost(bool, tag = "5")]
                pub comp_oc: bool,
                #[prost(bool, tag = "6")]
                pub ptc_ot: bool,
                #[prost(bool, tag = "7")]
                pub fan_oc: bool,
            }
            #[derive(prost::Message)]
            pub struct Fault {
                #[prost(bool, tag = "1")]
                pub in_tmp_sensor: bool,
                #[prost(bool, tag = "2")]
                pub ex_tmp_sensor: bool,
                #[prost(bool, tag = "3")]
                pub rh_sensor: bool,
            }
            #[derive(prost::Message)]
            pub struct Status {
                #[prost(bool, tag = "1")]
                pub comp: bool,
                #[prost(bool, tag = "2")]
                pub fan: bool,
                #[prost(bool, tag = "3")]
                pub alarm: bool,
                #[prost(bool, tag = "4")]
                pub ptc_heater: bool,
            }
            #[derive(prost::Message)]
            pub struct Measure {
                #[prost(float, tag = "1")]
                pub in_tmp: f32,
                #[prost(float, tag = "2")]
                pub ex_tmp: f32,
                #[prost(float, tag = "3")]
                pub rh: f32,
            }
            #[derive(prost::Message)]
            pub struct Parameters {
                #[prost(float, tag = "1")]
                pub tmp_setpoint: f32,
                #[prost(float, tag = "2")]
                pub tmp_upper: f32,
                #[prost(float, tag = "3")]
                pub tmp_lower: f32,
                #[prost(uint32, tag = "4")]
                pub delay_time: u32,
                #[prost(float, tag = "5")]
                pub hysteresis: f32,
                #[prost(float, tag = "6")]
                pub save_ops: f32,
                #[prost(float, tag = "7")]
                pub in_tmp_calib: f32,
                #[prost(float, tag = "8")]
                pub ex_tmp_calib: f32,
                #[prost(float, tag = "9")]
                pub rh_calib: f32,
                #[prost(bool, tag = "10")]
                pub power: bool,
                #[prost(uint32, tag = "11")]
                pub rh_setpoint: u32,
                #[prost(uint32, tag = "12")]
                pub rh_delta: u32,
                #[prost(float, tag = "13")]
                pub heat_off_setpoint: f32,
                #[prost(float, tag = "14")]
                pub heat_on_setpoint: f32,
                #[prost(uint32, tag = "15")]
                pub unit_id: u32,
                #[prost(int32, tag = "16")]
                pub baud_rate: i32,
                #[prost(uint32, tag = "17")]
                pub handheater: u32,
                #[prost(uint32, tag = "18")]
                pub model: u32,
            }
        }
        #[derive(prost::Message)]
        struct Hvac {
            #[prost(message, optional, tag = "1")]
            command: Option<hvac::Command>,
            #[prost(message, optional, tag = "2")]
            fault: Option<hvac::Fault>,
            #[prost(message, optional, tag = "3")]
            status: Option<hvac::Status>,
            #[prost(message, optional, tag = "4")]
            measure: Option<hvac::Measure>,
            #[prost(message, optional, tag = "5")]
            parameters: Option<hvac::Parameters>,
        }

        let hvac_full = Hvac {
            command: hvac::Command {
                dor: true,
                hp: true,
                lp: true,
                halon: true,
                comp_oc: true,
                ptc_ot: true,
                fan_oc: true,
            }
            .into(),
            fault: hvac::Fault {
                in_tmp_sensor: true,
                ex_tmp_sensor: true,
                rh_sensor: true,
            }
            .into(),
            status: hvac::Status {
                comp: true,
                fan: true,
                alarm: true,
                ptc_heater: true,
            }
            .into(),
            measure: hvac::Measure {
                in_tmp: f32::MAX,
                ex_tmp: f32::MAX,
                rh: f32::MAX,
            }
            .into(),
            parameters: hvac::Parameters {
                tmp_setpoint: f32::MAX,
                tmp_upper: f32::MAX,
                tmp_lower: f32::MAX,
                delay_time: u32::MAX,
                hysteresis: f32::MAX,
                save_ops: f32::MAX,
                in_tmp_calib: f32::MAX,
                ex_tmp_calib: f32::MAX,
                rh_calib: f32::MAX,
                power: true,
                rh_setpoint: u32::MAX,
                rh_delta: u32::MAX,
                heat_off_setpoint: f32::MAX,
                heat_on_setpoint: f32::MAX,
                unit_id: u32::MAX,
                baud_rate: i32::MAX,
                handheater: u32::MAX,
                model: u32::MAX,
            }
            .into(),
        };

        tracing::info!("hvac_full size: {}", hvac_full.encoded_len() + 32);

        Ok(())
    }
}
