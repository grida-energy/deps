from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompactEsdRtg(_message.Message):
    __slots__ = ("ah_rtg", "wh_rtg", "w_cha_rte_max", "w_discha_rte_max", "discha_rte", "soc_max", "soc_min")
    AH_RTG_FIELD_NUMBER: _ClassVar[int]
    WH_RTG_FIELD_NUMBER: _ClassVar[int]
    W_CHA_RTE_MAX_FIELD_NUMBER: _ClassVar[int]
    W_DISCHA_RTE_MAX_FIELD_NUMBER: _ClassVar[int]
    DISCHA_RTE_FIELD_NUMBER: _ClassVar[int]
    SOC_MAX_FIELD_NUMBER: _ClassVar[int]
    SOC_MIN_FIELD_NUMBER: _ClassVar[int]
    ah_rtg: float
    wh_rtg: float
    w_cha_rte_max: float
    w_discha_rte_max: float
    discha_rte: float
    soc_max: float
    soc_min: float
    def __init__(self, ah_rtg: _Optional[float] = ..., wh_rtg: _Optional[float] = ..., w_cha_rte_max: _Optional[float] = ..., w_discha_rte_max: _Optional[float] = ..., discha_rte: _Optional[float] = ..., soc_max: _Optional[float] = ..., soc_min: _Optional[float] = ...) -> None: ...

class PcsControlsNameplateRatings(_message.Message):
    __slots__ = ("w_rtg", "va_rtg", "var_rtg_q1", "var_rtg_q2", "var_rtg_q3", "var_rtg_q4", "a_rtg", "pf_rtg_q1", "pf_rtg_q2", "pf_rtg_q3", "pf_rtg_q4")
    W_RTG_FIELD_NUMBER: _ClassVar[int]
    VA_RTG_FIELD_NUMBER: _ClassVar[int]
    VAR_RTG_Q1_FIELD_NUMBER: _ClassVar[int]
    VAR_RTG_Q2_FIELD_NUMBER: _ClassVar[int]
    VAR_RTG_Q3_FIELD_NUMBER: _ClassVar[int]
    VAR_RTG_Q4_FIELD_NUMBER: _ClassVar[int]
    A_RTG_FIELD_NUMBER: _ClassVar[int]
    PF_RTG_Q1_FIELD_NUMBER: _ClassVar[int]
    PF_RTG_Q2_FIELD_NUMBER: _ClassVar[int]
    PF_RTG_Q3_FIELD_NUMBER: _ClassVar[int]
    PF_RTG_Q4_FIELD_NUMBER: _ClassVar[int]
    w_rtg: float
    va_rtg: float
    var_rtg_q1: float
    var_rtg_q2: float
    var_rtg_q3: float
    var_rtg_q4: float
    a_rtg: float
    pf_rtg_q1: float
    pf_rtg_q2: float
    pf_rtg_q3: float
    pf_rtg_q4: float
    def __init__(self, w_rtg: _Optional[float] = ..., va_rtg: _Optional[float] = ..., var_rtg_q1: _Optional[float] = ..., var_rtg_q2: _Optional[float] = ..., var_rtg_q3: _Optional[float] = ..., var_rtg_q4: _Optional[float] = ..., a_rtg: _Optional[float] = ..., pf_rtg_q1: _Optional[float] = ..., pf_rtg_q2: _Optional[float] = ..., pf_rtg_q3: _Optional[float] = ..., pf_rtg_q4: _Optional[float] = ...) -> None: ...

class ConfigurablePcs(_message.Message):
    __slots__ = ("ph_v_rtg", "hz_rtg", "a_ph_rtg", "w_rtg", "dca_rtg", "dcv_rtg")
    PH_V_RTG_FIELD_NUMBER: _ClassVar[int]
    HZ_RTG_FIELD_NUMBER: _ClassVar[int]
    A_PH_RTG_FIELD_NUMBER: _ClassVar[int]
    W_RTG_FIELD_NUMBER: _ClassVar[int]
    DCA_RTG_FIELD_NUMBER: _ClassVar[int]
    DCV_RTG_FIELD_NUMBER: _ClassVar[int]
    ph_v_rtg: float
    hz_rtg: float
    a_ph_rtg: float
    w_rtg: float
    dca_rtg: float
    dcv_rtg: float
    def __init__(self, ph_v_rtg: _Optional[float] = ..., hz_rtg: _Optional[float] = ..., a_ph_rtg: _Optional[float] = ..., w_rtg: _Optional[float] = ..., dca_rtg: _Optional[float] = ..., dcv_rtg: _Optional[float] = ...) -> None: ...

class ProtectionItem(_message.Message):
    __slots__ = ("level", "win_tms")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    level: float
    win_tms: float
    def __init__(self, level: _Optional[float] = ..., win_tms: _Optional[float] = ...) -> None: ...

class ProtectionConfigAc(_message.Message):
    __slots__ = ("ph_v_ph_disconn_max", "ph_v_ph_alarm_max", "ph_v_ph_disconn_min", "ph_v_ph_alarm_min", "a_disconn_max", "a_alarm_max", "hz_disconn_max", "hz_alarm_max", "hz_disconn_min", "hz_alarm_min")
    PH_V_PH_DISCONN_MAX_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_ALARM_MAX_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_DISCONN_MIN_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_ALARM_MIN_FIELD_NUMBER: _ClassVar[int]
    A_DISCONN_MAX_FIELD_NUMBER: _ClassVar[int]
    A_ALARM_MAX_FIELD_NUMBER: _ClassVar[int]
    HZ_DISCONN_MAX_FIELD_NUMBER: _ClassVar[int]
    HZ_ALARM_MAX_FIELD_NUMBER: _ClassVar[int]
    HZ_DISCONN_MIN_FIELD_NUMBER: _ClassVar[int]
    HZ_ALARM_MIN_FIELD_NUMBER: _ClassVar[int]
    ph_v_ph_disconn_max: ProtectionItem
    ph_v_ph_alarm_max: ProtectionItem
    ph_v_ph_disconn_min: ProtectionItem
    ph_v_ph_alarm_min: ProtectionItem
    a_disconn_max: ProtectionItem
    a_alarm_max: ProtectionItem
    hz_disconn_max: ProtectionItem
    hz_alarm_max: ProtectionItem
    hz_disconn_min: ProtectionItem
    hz_alarm_min: ProtectionItem
    def __init__(self, ph_v_ph_disconn_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., ph_v_ph_alarm_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., ph_v_ph_disconn_min: _Optional[_Union[ProtectionItem, _Mapping]] = ..., ph_v_ph_alarm_min: _Optional[_Union[ProtectionItem, _Mapping]] = ..., a_disconn_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., a_alarm_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., hz_disconn_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., hz_alarm_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., hz_disconn_min: _Optional[_Union[ProtectionItem, _Mapping]] = ..., hz_alarm_min: _Optional[_Union[ProtectionItem, _Mapping]] = ...) -> None: ...

class ProtectionConfigDc(_message.Message):
    __slots__ = ("dcv_disconn_max", "dcv_alarm_max", "dcv_disconn_min", "dcv_alarm_min", "dca_disconn_max", "dca_alarm_max")
    DCV_DISCONN_MAX_FIELD_NUMBER: _ClassVar[int]
    DCV_ALARM_MAX_FIELD_NUMBER: _ClassVar[int]
    DCV_DISCONN_MIN_FIELD_NUMBER: _ClassVar[int]
    DCV_ALARM_MIN_FIELD_NUMBER: _ClassVar[int]
    DCA_DISCONN_MAX_FIELD_NUMBER: _ClassVar[int]
    DCA_ALARM_MAX_FIELD_NUMBER: _ClassVar[int]
    dcv_disconn_max: ProtectionItem
    dcv_alarm_max: ProtectionItem
    dcv_disconn_min: ProtectionItem
    dcv_alarm_min: ProtectionItem
    dca_disconn_max: ProtectionItem
    dca_alarm_max: ProtectionItem
    def __init__(self, dcv_disconn_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., dcv_alarm_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., dcv_disconn_min: _Optional[_Union[ProtectionItem, _Mapping]] = ..., dcv_alarm_min: _Optional[_Union[ProtectionItem, _Mapping]] = ..., dca_disconn_max: _Optional[_Union[ProtectionItem, _Mapping]] = ..., dca_alarm_max: _Optional[_Union[ProtectionItem, _Mapping]] = ...) -> None: ...

class ProtectionTemperature(_message.Message):
    __slots__ = ("tmp_cab", "tmp_snk", "tmp_trns", "tmp_ot")
    TMP_CAB_FIELD_NUMBER: _ClassVar[int]
    TMP_SNK_FIELD_NUMBER: _ClassVar[int]
    TMP_TRNS_FIELD_NUMBER: _ClassVar[int]
    TMP_OT_FIELD_NUMBER: _ClassVar[int]
    tmp_cab: ProtectionItem
    tmp_snk: ProtectionItem
    tmp_trns: ProtectionItem
    tmp_ot: ProtectionItem
    def __init__(self, tmp_cab: _Optional[_Union[ProtectionItem, _Mapping]] = ..., tmp_snk: _Optional[_Union[ProtectionItem, _Mapping]] = ..., tmp_trns: _Optional[_Union[ProtectionItem, _Mapping]] = ..., tmp_ot: _Optional[_Union[ProtectionItem, _Mapping]] = ...) -> None: ...

class Calibration(_message.Message):
    __slots__ = ("gain", "offset")
    GAIN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    gain: float
    offset: float
    def __init__(self, gain: _Optional[float] = ..., offset: _Optional[float] = ...) -> None: ...

class CalibrationAc(_message.Message):
    __slots__ = ("a_ph_a", "a_ph_b", "a_ph_c", "pp_v_ph_ab", "pp_v_ph_bc", "pp_v_ph_ca", "ph_v_ph_a", "ph_v_ph_b", "ph_v_ph_c")
    A_PH_A_FIELD_NUMBER: _ClassVar[int]
    A_PH_B_FIELD_NUMBER: _ClassVar[int]
    A_PH_C_FIELD_NUMBER: _ClassVar[int]
    PP_V_PH_AB_FIELD_NUMBER: _ClassVar[int]
    PP_V_PH_BC_FIELD_NUMBER: _ClassVar[int]
    PP_V_PH_CA_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_A_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_B_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_C_FIELD_NUMBER: _ClassVar[int]
    a_ph_a: Calibration
    a_ph_b: Calibration
    a_ph_c: Calibration
    pp_v_ph_ab: Calibration
    pp_v_ph_bc: Calibration
    pp_v_ph_ca: Calibration
    ph_v_ph_a: Calibration
    ph_v_ph_b: Calibration
    ph_v_ph_c: Calibration
    def __init__(self, a_ph_a: _Optional[_Union[Calibration, _Mapping]] = ..., a_ph_b: _Optional[_Union[Calibration, _Mapping]] = ..., a_ph_c: _Optional[_Union[Calibration, _Mapping]] = ..., pp_v_ph_ab: _Optional[_Union[Calibration, _Mapping]] = ..., pp_v_ph_bc: _Optional[_Union[Calibration, _Mapping]] = ..., pp_v_ph_ca: _Optional[_Union[Calibration, _Mapping]] = ..., ph_v_ph_a: _Optional[_Union[Calibration, _Mapping]] = ..., ph_v_ph_b: _Optional[_Union[Calibration, _Mapping]] = ..., ph_v_ph_c: _Optional[_Union[Calibration, _Mapping]] = ...) -> None: ...

class CalibrationDc(_message.Message):
    __slots__ = ("dca", "dcv")
    DCA_FIELD_NUMBER: _ClassVar[int]
    DCV_FIELD_NUMBER: _ClassVar[int]
    dca: Calibration
    dcv: Calibration
    def __init__(self, dca: _Optional[_Union[Calibration, _Mapping]] = ..., dcv: _Optional[_Union[Calibration, _Mapping]] = ...) -> None: ...
