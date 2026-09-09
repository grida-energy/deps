import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlatEsd(_message.Message):
    __slots__ = ("soc", "dod", "soh", "n_cyc", "cha_st", "loc_rem_ctl", "hb", "typ", "state", "state_vnd", "warr_dt", "evt1", "evt2", "evt_vnd1", "evt_vnd2", "v", "v_max", "v_min", "cell_v_max", "cell_v_max_str", "cell_v_max_mod", "cell_v_min", "cell_v_min_str", "cell_v_min_mod", "cell_v_avg", "a", "a_cha_max", "a_discha_max", "w", "state_req_pcs", "w_req", "set_op")
    class ChaSt(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_CHAST: _ClassVar[FlatEsd.ChaSt]
        OFF: _ClassVar[FlatEsd.ChaSt]
        EMPTY: _ClassVar[FlatEsd.ChaSt]
        DISCHARGING: _ClassVar[FlatEsd.ChaSt]
        CHARGING: _ClassVar[FlatEsd.ChaSt]
        FULL: _ClassVar[FlatEsd.ChaSt]
        HOLDING: _ClassVar[FlatEsd.ChaSt]
        TESTING: _ClassVar[FlatEsd.ChaSt]
    NA_CHAST: FlatEsd.ChaSt
    OFF: FlatEsd.ChaSt
    EMPTY: FlatEsd.ChaSt
    DISCHARGING: FlatEsd.ChaSt
    CHARGING: FlatEsd.ChaSt
    FULL: FlatEsd.ChaSt
    HOLDING: FlatEsd.ChaSt
    TESTING: FlatEsd.ChaSt
    class LocRemCtl(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_LOCREMCTL: _ClassVar[FlatEsd.LocRemCtl]
        LOCAL: _ClassVar[FlatEsd.LocRemCtl]
        REMOTE: _ClassVar[FlatEsd.LocRemCtl]
    NA_LOCREMCTL: FlatEsd.LocRemCtl
    LOCAL: FlatEsd.LocRemCtl
    REMOTE: FlatEsd.LocRemCtl
    class Typ(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_TYP: _ClassVar[FlatEsd.Typ]
        LEAD_ACID: _ClassVar[FlatEsd.Typ]
        NICKEL_METAL_HYDRATE: _ClassVar[FlatEsd.Typ]
        NICKEL_CADMIUM: _ClassVar[FlatEsd.Typ]
        LITHIUM_ION: _ClassVar[FlatEsd.Typ]
        CARBON_ZINC: _ClassVar[FlatEsd.Typ]
        ZINC_CHLORIDE: _ClassVar[FlatEsd.Typ]
        ALKAINE: _ClassVar[FlatEsd.Typ]
        RECHARGEABLE_ALKAINE: _ClassVar[FlatEsd.Typ]
        SODIUM_SULFUR: _ClassVar[FlatEsd.Typ]
        FLOW: _ClassVar[FlatEsd.Typ]
        OTHER: _ClassVar[FlatEsd.Typ]
    NA_TYP: FlatEsd.Typ
    LEAD_ACID: FlatEsd.Typ
    NICKEL_METAL_HYDRATE: FlatEsd.Typ
    NICKEL_CADMIUM: FlatEsd.Typ
    LITHIUM_ION: FlatEsd.Typ
    CARBON_ZINC: FlatEsd.Typ
    ZINC_CHLORIDE: FlatEsd.Typ
    ALKAINE: FlatEsd.Typ
    RECHARGEABLE_ALKAINE: FlatEsd.Typ
    SODIUM_SULFUR: FlatEsd.Typ
    FLOW: FlatEsd.Typ
    OTHER: FlatEsd.Typ
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_STATE: _ClassVar[FlatEsd.State]
        DISCONNECTED: _ClassVar[FlatEsd.State]
        INITIALIZING: _ClassVar[FlatEsd.State]
        CONNECTED: _ClassVar[FlatEsd.State]
        STANDBY: _ClassVar[FlatEsd.State]
        SOC_PROTECTION: _ClassVar[FlatEsd.State]
        SUSPENDING: _ClassVar[FlatEsd.State]
        FAULT: _ClassVar[FlatEsd.State]
    NA_STATE: FlatEsd.State
    DISCONNECTED: FlatEsd.State
    INITIALIZING: FlatEsd.State
    CONNECTED: FlatEsd.State
    STANDBY: FlatEsd.State
    SOC_PROTECTION: FlatEsd.State
    SUSPENDING: FlatEsd.State
    FAULT: FlatEsd.State
    class ReqPcstate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_REQUEST: _ClassVar[FlatEsd.ReqPcstate]
        START: _ClassVar[FlatEsd.ReqPcstate]
        STOP: _ClassVar[FlatEsd.ReqPcstate]
    NO_REQUEST: FlatEsd.ReqPcstate
    START: FlatEsd.ReqPcstate
    STOP: FlatEsd.ReqPcstate
    class SetOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_SETOP: _ClassVar[FlatEsd.SetOp]
        CONNECT: _ClassVar[FlatEsd.SetOp]
        DISCONNECT: _ClassVar[FlatEsd.SetOp]
    NA_SETOP: FlatEsd.SetOp
    CONNECT: FlatEsd.SetOp
    DISCONNECT: FlatEsd.SetOp
    class SetPcsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_SETPCSSTATE: _ClassVar[FlatEsd.SetPcsState]
        PCS_STOPPED: _ClassVar[FlatEsd.SetPcsState]
        PCS_STANDBY: _ClassVar[FlatEsd.SetPcsState]
        PCS_STARTED: _ClassVar[FlatEsd.SetPcsState]
    NA_SETPCSSTATE: FlatEsd.SetPcsState
    PCS_STOPPED: FlatEsd.SetPcsState
    PCS_STANDBY: FlatEsd.SetPcsState
    PCS_STARTED: FlatEsd.SetPcsState
    class Evt1(_message.Message):
        __slots__ = ("COMMUNICATION_ERROR", "OVER_TEMP_ALARM", "OVER_TEMP_WARNING", "UNDER_TEMP_ALARM", "UNDER_TEMP_WARNING", "OVER_CHARGE_CURRENT_ALARM", "OVER_CHARGE_CURRENT_WARNING", "OVER_DISCHARGE_CURRENT_ALARM", "OVER_DISCHARGE_CURRENT_WARNING", "OVER_VOLT_ALARM", "OVER_VOLT_WARNING", "UNDER_VOLT_ALARM", "UNDER_VOLT_WARNING", "UNDER_SOC_MIN_ALARM", "UNDER_SOC_MIN_WARNING", "OVER_SOC_MAX_ALARM", "OVER_SOC_MAX_WARNING", "VOLTAGE_IMBALANCE_WARNING", "TEMPERATURE_IMBALANCE_ALARM", "TEMPERATURE_IMBALANCE_WARNING", "CONTACTOR_ERROR", "FAN_ERROR", "GROUND_FAULT", "OPEN_DOOR_ERROR", "CURRENT_IMBALANCE_WARNING", "OTHER_ALARM", "OTHER_WARNING", "RESERVED_1", "CONFIGURATION_ALARM", "CONFIGURATION_WARNING")
        COMMUNICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_WARNING_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_ALARM_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_WARNING_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_ALARM_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_WARNING_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_ALARM_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_WARNING_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_IMBALANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_ALARM_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_ERROR_FIELD_NUMBER: _ClassVar[int]
        FAN_ERROR_FIELD_NUMBER: _ClassVar[int]
        GROUND_FAULT_FIELD_NUMBER: _ClassVar[int]
        OPEN_DOOR_ERROR_FIELD_NUMBER: _ClassVar[int]
        CURRENT_IMBALANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
        OTHER_ALARM_FIELD_NUMBER: _ClassVar[int]
        OTHER_WARNING_FIELD_NUMBER: _ClassVar[int]
        RESERVED_1_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ALARM_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_WARNING_FIELD_NUMBER: _ClassVar[int]
        COMMUNICATION_ERROR: bool
        OVER_TEMP_ALARM: bool
        OVER_TEMP_WARNING: bool
        UNDER_TEMP_ALARM: bool
        UNDER_TEMP_WARNING: bool
        OVER_CHARGE_CURRENT_ALARM: bool
        OVER_CHARGE_CURRENT_WARNING: bool
        OVER_DISCHARGE_CURRENT_ALARM: bool
        OVER_DISCHARGE_CURRENT_WARNING: bool
        OVER_VOLT_ALARM: bool
        OVER_VOLT_WARNING: bool
        UNDER_VOLT_ALARM: bool
        UNDER_VOLT_WARNING: bool
        UNDER_SOC_MIN_ALARM: bool
        UNDER_SOC_MIN_WARNING: bool
        OVER_SOC_MAX_ALARM: bool
        OVER_SOC_MAX_WARNING: bool
        VOLTAGE_IMBALANCE_WARNING: bool
        TEMPERATURE_IMBALANCE_ALARM: bool
        TEMPERATURE_IMBALANCE_WARNING: bool
        CONTACTOR_ERROR: bool
        FAN_ERROR: bool
        GROUND_FAULT: bool
        OPEN_DOOR_ERROR: bool
        CURRENT_IMBALANCE_WARNING: bool
        OTHER_ALARM: bool
        OTHER_WARNING: bool
        RESERVED_1: bool
        CONFIGURATION_ALARM: bool
        CONFIGURATION_WARNING: bool
        def __init__(self, COMMUNICATION_ERROR: _Optional[bool] = ..., OVER_TEMP_ALARM: _Optional[bool] = ..., OVER_TEMP_WARNING: _Optional[bool] = ..., UNDER_TEMP_ALARM: _Optional[bool] = ..., UNDER_TEMP_WARNING: _Optional[bool] = ..., OVER_CHARGE_CURRENT_ALARM: _Optional[bool] = ..., OVER_CHARGE_CURRENT_WARNING: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT_ALARM: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT_WARNING: _Optional[bool] = ..., OVER_VOLT_ALARM: _Optional[bool] = ..., OVER_VOLT_WARNING: _Optional[bool] = ..., UNDER_VOLT_ALARM: _Optional[bool] = ..., UNDER_VOLT_WARNING: _Optional[bool] = ..., UNDER_SOC_MIN_ALARM: _Optional[bool] = ..., UNDER_SOC_MIN_WARNING: _Optional[bool] = ..., OVER_SOC_MAX_ALARM: _Optional[bool] = ..., OVER_SOC_MAX_WARNING: _Optional[bool] = ..., VOLTAGE_IMBALANCE_WARNING: _Optional[bool] = ..., TEMPERATURE_IMBALANCE_ALARM: _Optional[bool] = ..., TEMPERATURE_IMBALANCE_WARNING: _Optional[bool] = ..., CONTACTOR_ERROR: _Optional[bool] = ..., FAN_ERROR: _Optional[bool] = ..., GROUND_FAULT: _Optional[bool] = ..., OPEN_DOOR_ERROR: _Optional[bool] = ..., CURRENT_IMBALANCE_WARNING: _Optional[bool] = ..., OTHER_ALARM: _Optional[bool] = ..., OTHER_WARNING: _Optional[bool] = ..., RESERVED_1: _Optional[bool] = ..., CONFIGURATION_ALARM: _Optional[bool] = ..., CONFIGURATION_WARNING: _Optional[bool] = ...) -> None: ...
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    CHA_ST_FIELD_NUMBER: _ClassVar[int]
    LOC_REM_CTL_FIELD_NUMBER: _ClassVar[int]
    HB_FIELD_NUMBER: _ClassVar[int]
    TYP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_VND_FIELD_NUMBER: _ClassVar[int]
    WARR_DT_FIELD_NUMBER: _ClassVar[int]
    EVT1_FIELD_NUMBER: _ClassVar[int]
    EVT2_FIELD_NUMBER: _ClassVar[int]
    EVT_VND1_FIELD_NUMBER: _ClassVar[int]
    EVT_VND2_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    V_MAX_FIELD_NUMBER: _ClassVar[int]
    V_MIN_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_STR_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_STR_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
    CELL_V_AVG_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    A_CHA_MAX_FIELD_NUMBER: _ClassVar[int]
    A_DISCHA_MAX_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    STATE_REQ_PCS_FIELD_NUMBER: _ClassVar[int]
    W_REQ_FIELD_NUMBER: _ClassVar[int]
    SET_OP_FIELD_NUMBER: _ClassVar[int]
    soc: float
    dod: float
    soh: float
    n_cyc: float
    cha_st: FlatEsd.ChaSt
    loc_rem_ctl: FlatEsd.LocRemCtl
    hb: int
    typ: FlatEsd.Typ
    state: FlatEsd.State
    state_vnd: int
    warr_dt: _timestamp_pb2.Timestamp
    evt1: FlatEsd.Evt1
    evt2: int
    evt_vnd1: int
    evt_vnd2: int
    v: float
    v_max: float
    v_min: float
    cell_v_max: float
    cell_v_max_str: int
    cell_v_max_mod: int
    cell_v_min: float
    cell_v_min_str: int
    cell_v_min_mod: int
    cell_v_avg: float
    a: float
    a_cha_max: float
    a_discha_max: float
    w: float
    state_req_pcs: FlatEsd.ReqPcstate
    w_req: float
    set_op: FlatEsd.SetOp
    def __init__(self, soc: _Optional[float] = ..., dod: _Optional[float] = ..., soh: _Optional[float] = ..., n_cyc: _Optional[float] = ..., cha_st: _Optional[_Union[FlatEsd.ChaSt, str]] = ..., loc_rem_ctl: _Optional[_Union[FlatEsd.LocRemCtl, str]] = ..., hb: _Optional[int] = ..., typ: _Optional[_Union[FlatEsd.Typ, str]] = ..., state: _Optional[_Union[FlatEsd.State, str]] = ..., state_vnd: _Optional[int] = ..., warr_dt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., evt1: _Optional[_Union[FlatEsd.Evt1, _Mapping]] = ..., evt2: _Optional[int] = ..., evt_vnd1: _Optional[int] = ..., evt_vnd2: _Optional[int] = ..., v: _Optional[float] = ..., v_max: _Optional[float] = ..., v_min: _Optional[float] = ..., cell_v_max: _Optional[float] = ..., cell_v_max_str: _Optional[int] = ..., cell_v_max_mod: _Optional[int] = ..., cell_v_min: _Optional[float] = ..., cell_v_min_str: _Optional[int] = ..., cell_v_min_mod: _Optional[int] = ..., cell_v_avg: _Optional[float] = ..., a: _Optional[float] = ..., a_cha_max: _Optional[float] = ..., a_discha_max: _Optional[float] = ..., w: _Optional[float] = ..., state_req_pcs: _Optional[_Union[FlatEsd.ReqPcstate, str]] = ..., w_req: _Optional[float] = ..., set_op: _Optional[_Union[FlatEsd.SetOp, str]] = ...) -> None: ...

class FlatEsdCommand(_message.Message):
    __slots__ = ("set_op", "set_pcs_state")
    SET_OP_FIELD_NUMBER: _ClassVar[int]
    SET_PCS_STATE_FIELD_NUMBER: _ClassVar[int]
    set_op: FlatEsd.SetOp
    set_pcs_state: FlatEsd.SetPcsState
    def __init__(self, set_op: _Optional[_Union[FlatEsd.SetOp, str]] = ..., set_pcs_state: _Optional[_Union[FlatEsd.SetPcsState, str]] = ...) -> None: ...

class CommpactEsdCommands(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[FlatEsdCommand]
    def __init__(self, commands: _Optional[_Iterable[_Union[FlatEsdCommand, _Mapping]]] = ...) -> None: ...

class FlatEsdBank(_message.Message):
    __slots__ = ("n_str", "n_str_con", "mod_tmp_max", "mod_tmp_max_str", "mod_tmp_max_mod", "mod_tmp_min", "mod_tmp_min_str", "mod_tmp_min_mod", "mod_tmp_avg", "str_v_max", "str_v_max_str", "str_v_min", "str_v_min_str", "str_v_avg", "str_a_max", "str_a_max_str", "str_a_min", "str_a_min_str", "str_a_avg", "n_cell_bal", "strs")
    N_STR_FIELD_NUMBER: _ClassVar[int]
    N_STR_CON_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MAX_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MAX_STR_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MIN_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MIN_STR_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_AVG_FIELD_NUMBER: _ClassVar[int]
    STR_V_MAX_FIELD_NUMBER: _ClassVar[int]
    STR_V_MAX_STR_FIELD_NUMBER: _ClassVar[int]
    STR_V_MIN_FIELD_NUMBER: _ClassVar[int]
    STR_V_MIN_STR_FIELD_NUMBER: _ClassVar[int]
    STR_V_AVG_FIELD_NUMBER: _ClassVar[int]
    STR_A_MAX_FIELD_NUMBER: _ClassVar[int]
    STR_A_MAX_STR_FIELD_NUMBER: _ClassVar[int]
    STR_A_MIN_FIELD_NUMBER: _ClassVar[int]
    STR_A_MIN_STR_FIELD_NUMBER: _ClassVar[int]
    STR_A_AVG_FIELD_NUMBER: _ClassVar[int]
    N_CELL_BAL_FIELD_NUMBER: _ClassVar[int]
    STRS_FIELD_NUMBER: _ClassVar[int]
    n_str: int
    n_str_con: int
    mod_tmp_max: float
    mod_tmp_max_str: int
    mod_tmp_max_mod: int
    mod_tmp_min: float
    mod_tmp_min_str: int
    mod_tmp_min_mod: int
    mod_tmp_avg: float
    str_v_max: float
    str_v_max_str: float
    str_v_min: float
    str_v_min_str: float
    str_v_avg: float
    str_a_max: float
    str_a_max_str: float
    str_a_min: float
    str_a_min_str: float
    str_a_avg: float
    n_cell_bal: float
    strs: _containers.RepeatedCompositeFieldContainer[FlatEsdString]
    def __init__(self, n_str: _Optional[int] = ..., n_str_con: _Optional[int] = ..., mod_tmp_max: _Optional[float] = ..., mod_tmp_max_str: _Optional[int] = ..., mod_tmp_max_mod: _Optional[int] = ..., mod_tmp_min: _Optional[float] = ..., mod_tmp_min_str: _Optional[int] = ..., mod_tmp_min_mod: _Optional[int] = ..., mod_tmp_avg: _Optional[float] = ..., str_v_max: _Optional[float] = ..., str_v_max_str: _Optional[float] = ..., str_v_min: _Optional[float] = ..., str_v_min_str: _Optional[float] = ..., str_v_avg: _Optional[float] = ..., str_a_max: _Optional[float] = ..., str_a_max_str: _Optional[float] = ..., str_a_min: _Optional[float] = ..., str_a_min_str: _Optional[float] = ..., str_a_avg: _Optional[float] = ..., n_cell_bal: _Optional[float] = ..., strs: _Optional[_Iterable[_Union[FlatEsdString, _Mapping]]] = ...) -> None: ...

class FlatEsdString(_message.Message):
    __slots__ = ("n_mod", "st", "con_fail", "n_cell_bal", "soc", "dod", "n_cyc", "soh", "a", "v", "cell_v_max", "cell_v_max_mod", "cell_v_min", "cell_v_min_mod", "cell_v_avg", "mod_tmp_max", "mod_tmp_max_mod", "mod_tmp_min", "mod_tmp_min_mod", "mod_tmp_avg", "con_st", "evt1", "evt2", "evt_vnd1", "evt_vnd2", "set_ena", "set_con", "mods")
    class ConFail(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_FAILURE: _ClassVar[FlatEsdString.ConFail]
        BUTTON_PUSHED: _ClassVar[FlatEsdString.ConFail]
        STR_GROUND_FAULT: _ClassVar[FlatEsdString.ConFail]
        OUTSIDE_VOLTAGE_RANGE: _ClassVar[FlatEsdString.ConFail]
        STRING_NOT_ENABLED: _ClassVar[FlatEsdString.ConFail]
        FUSE_OPEN: _ClassVar[FlatEsdString.ConFail]
        CONTACTOR_FAILURE: _ClassVar[FlatEsdString.ConFail]
        PRECHARGE_FAILURE: _ClassVar[FlatEsdString.ConFail]
        STRING_FAULT: _ClassVar[FlatEsdString.ConFail]
    NO_FAILURE: FlatEsdString.ConFail
    BUTTON_PUSHED: FlatEsdString.ConFail
    STR_GROUND_FAULT: FlatEsdString.ConFail
    OUTSIDE_VOLTAGE_RANGE: FlatEsdString.ConFail
    STRING_NOT_ENABLED: FlatEsdString.ConFail
    FUSE_OPEN: FlatEsdString.ConFail
    CONTACTOR_FAILURE: FlatEsdString.ConFail
    PRECHARGE_FAILURE: FlatEsdString.ConFail
    STRING_FAULT: FlatEsdString.ConFail
    class SetEna(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_SETENA: _ClassVar[FlatEsdString.SetEna]
        ENABLE_STRING: _ClassVar[FlatEsdString.SetEna]
        DISABLE_STRING: _ClassVar[FlatEsdString.SetEna]
    NA_SETENA: FlatEsdString.SetEna
    ENABLE_STRING: FlatEsdString.SetEna
    DISABLE_STRING: FlatEsdString.SetEna
    class SetCon(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_SETCON: _ClassVar[FlatEsdString.SetCon]
        CONNECT_STRING: _ClassVar[FlatEsdString.SetCon]
        DISCONNECT_STRING: _ClassVar[FlatEsdString.SetCon]
    NA_SETCON: FlatEsdString.SetCon
    CONNECT_STRING: FlatEsdString.SetCon
    DISCONNECT_STRING: FlatEsdString.SetCon
    class St(_message.Message):
        __slots__ = ("STRING_ENABLED", "CONTACTOR_STATUS")
        STRING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_STATUS_FIELD_NUMBER: _ClassVar[int]
        STRING_ENABLED: bool
        CONTACTOR_STATUS: bool
        def __init__(self, STRING_ENABLED: _Optional[bool] = ..., CONTACTOR_STATUS: _Optional[bool] = ...) -> None: ...
    class ConSt(_message.Message):
        __slots__ = ("CONTACTOR_0", "CONTACTOR_1", "CONTACTOR_2", "CONTACTOR_3", "CONTACTOR_4", "CONTACTOR_5", "CONTACTOR_6", "CONTACTOR_7", "CONTACTOR_8", "CONTACTOR_9", "CONTACTOR_10", "CONTACTOR_11", "CONTACTOR_12", "CONTACTOR_13", "CONTACTOR_14", "CONTACTOR_15", "CONTACTOR_16", "CONTACTOR_17", "CONTACTOR_18", "CONTACTOR_19", "CONTACTOR_20", "CONTACTOR_21", "CONTACTOR_22", "CONTACTOR_23", "CONTACTOR_24", "CONTACTOR_25", "CONTACTOR_26", "CONTACTOR_27", "CONTACTOR_28", "CONTACTOR_29", "CONTACTOR_30")
        CONTACTOR_0_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_1_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_2_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_3_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_4_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_5_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_6_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_7_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_8_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_9_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_10_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_11_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_12_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_13_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_14_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_15_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_16_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_17_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_18_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_19_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_20_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_21_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_22_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_23_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_24_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_25_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_26_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_27_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_28_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_29_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_30_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_0: bool
        CONTACTOR_1: bool
        CONTACTOR_2: bool
        CONTACTOR_3: bool
        CONTACTOR_4: bool
        CONTACTOR_5: bool
        CONTACTOR_6: bool
        CONTACTOR_7: bool
        CONTACTOR_8: bool
        CONTACTOR_9: bool
        CONTACTOR_10: bool
        CONTACTOR_11: bool
        CONTACTOR_12: bool
        CONTACTOR_13: bool
        CONTACTOR_14: bool
        CONTACTOR_15: bool
        CONTACTOR_16: bool
        CONTACTOR_17: bool
        CONTACTOR_18: bool
        CONTACTOR_19: bool
        CONTACTOR_20: bool
        CONTACTOR_21: bool
        CONTACTOR_22: bool
        CONTACTOR_23: bool
        CONTACTOR_24: bool
        CONTACTOR_25: bool
        CONTACTOR_26: bool
        CONTACTOR_27: bool
        CONTACTOR_28: bool
        CONTACTOR_29: bool
        CONTACTOR_30: bool
        def __init__(self, CONTACTOR_0: _Optional[bool] = ..., CONTACTOR_1: _Optional[bool] = ..., CONTACTOR_2: _Optional[bool] = ..., CONTACTOR_3: _Optional[bool] = ..., CONTACTOR_4: _Optional[bool] = ..., CONTACTOR_5: _Optional[bool] = ..., CONTACTOR_6: _Optional[bool] = ..., CONTACTOR_7: _Optional[bool] = ..., CONTACTOR_8: _Optional[bool] = ..., CONTACTOR_9: _Optional[bool] = ..., CONTACTOR_10: _Optional[bool] = ..., CONTACTOR_11: _Optional[bool] = ..., CONTACTOR_12: _Optional[bool] = ..., CONTACTOR_13: _Optional[bool] = ..., CONTACTOR_14: _Optional[bool] = ..., CONTACTOR_15: _Optional[bool] = ..., CONTACTOR_16: _Optional[bool] = ..., CONTACTOR_17: _Optional[bool] = ..., CONTACTOR_18: _Optional[bool] = ..., CONTACTOR_19: _Optional[bool] = ..., CONTACTOR_20: _Optional[bool] = ..., CONTACTOR_21: _Optional[bool] = ..., CONTACTOR_22: _Optional[bool] = ..., CONTACTOR_23: _Optional[bool] = ..., CONTACTOR_24: _Optional[bool] = ..., CONTACTOR_25: _Optional[bool] = ..., CONTACTOR_26: _Optional[bool] = ..., CONTACTOR_27: _Optional[bool] = ..., CONTACTOR_28: _Optional[bool] = ..., CONTACTOR_29: _Optional[bool] = ..., CONTACTOR_30: _Optional[bool] = ...) -> None: ...
    class Evt1(_message.Message):
        __slots__ = ("COMMUNICATION_ERROR", "OVER_TEMP_ALARM", "OVER_TEMP_WARNING", "UNDER_TEMP_ALARM", "UNDER_TEMP_WARNING", "OVER_CHARGE_CURRENT_ALARM", "OVER_CHARGE_CURRENT_WARNING", "OVER_DISCHARGE_CURRENT_ALARM", "OVER_DISCHARGE_CURRENT_WARNING", "OVER_VOLT_ALARM", "OVER_VOLT_WARNING", "UNDER_VOLT_ALARM", "UNDER_VOLT_WARNING", "UNDER_SOC_MIN_ALARM", "UNDER_SOC_MIN_WARNING", "OVER_SOC_MAX_ALARM", "OVER_SOC_MAX_WARNING", "VOLTAGE_IMBALANCE_WARNING", "TEMPERATURE_IMBALANCE_ALARM", "TEMPERATURE_IMBALANCE_WARNING", "CONTACTOR_ERROR", "FAN_ERROR", "GROUND_FAULT", "OPEN_DOOR_ERROR", "OTHER_ALARM", "OTHER_WARNING", "CONFIGURATION_ALARM")
        COMMUNICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_WARNING_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_ALARM_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_WARNING_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_ALARM_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_WARNING_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_ALARM_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_WARNING_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_ALARM_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_WARNING_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_IMBALANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_ALARM_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_ERROR_FIELD_NUMBER: _ClassVar[int]
        FAN_ERROR_FIELD_NUMBER: _ClassVar[int]
        GROUND_FAULT_FIELD_NUMBER: _ClassVar[int]
        OPEN_DOOR_ERROR_FIELD_NUMBER: _ClassVar[int]
        OTHER_ALARM_FIELD_NUMBER: _ClassVar[int]
        OTHER_WARNING_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ALARM_FIELD_NUMBER: _ClassVar[int]
        COMMUNICATION_ERROR: bool
        OVER_TEMP_ALARM: bool
        OVER_TEMP_WARNING: bool
        UNDER_TEMP_ALARM: bool
        UNDER_TEMP_WARNING: bool
        OVER_CHARGE_CURRENT_ALARM: bool
        OVER_CHARGE_CURRENT_WARNING: bool
        OVER_DISCHARGE_CURRENT_ALARM: bool
        OVER_DISCHARGE_CURRENT_WARNING: bool
        OVER_VOLT_ALARM: bool
        OVER_VOLT_WARNING: bool
        UNDER_VOLT_ALARM: bool
        UNDER_VOLT_WARNING: bool
        UNDER_SOC_MIN_ALARM: bool
        UNDER_SOC_MIN_WARNING: bool
        OVER_SOC_MAX_ALARM: bool
        OVER_SOC_MAX_WARNING: bool
        VOLTAGE_IMBALANCE_WARNING: bool
        TEMPERATURE_IMBALANCE_ALARM: bool
        TEMPERATURE_IMBALANCE_WARNING: bool
        CONTACTOR_ERROR: bool
        FAN_ERROR: bool
        GROUND_FAULT: bool
        OPEN_DOOR_ERROR: bool
        OTHER_ALARM: bool
        OTHER_WARNING: bool
        CONFIGURATION_ALARM: bool
        def __init__(self, COMMUNICATION_ERROR: _Optional[bool] = ..., OVER_TEMP_ALARM: _Optional[bool] = ..., OVER_TEMP_WARNING: _Optional[bool] = ..., UNDER_TEMP_ALARM: _Optional[bool] = ..., UNDER_TEMP_WARNING: _Optional[bool] = ..., OVER_CHARGE_CURRENT_ALARM: _Optional[bool] = ..., OVER_CHARGE_CURRENT_WARNING: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT_ALARM: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT_WARNING: _Optional[bool] = ..., OVER_VOLT_ALARM: _Optional[bool] = ..., OVER_VOLT_WARNING: _Optional[bool] = ..., UNDER_VOLT_ALARM: _Optional[bool] = ..., UNDER_VOLT_WARNING: _Optional[bool] = ..., UNDER_SOC_MIN_ALARM: _Optional[bool] = ..., UNDER_SOC_MIN_WARNING: _Optional[bool] = ..., OVER_SOC_MAX_ALARM: _Optional[bool] = ..., OVER_SOC_MAX_WARNING: _Optional[bool] = ..., VOLTAGE_IMBALANCE_WARNING: _Optional[bool] = ..., TEMPERATURE_IMBALANCE_ALARM: _Optional[bool] = ..., TEMPERATURE_IMBALANCE_WARNING: _Optional[bool] = ..., CONTACTOR_ERROR: _Optional[bool] = ..., FAN_ERROR: _Optional[bool] = ..., GROUND_FAULT: _Optional[bool] = ..., OPEN_DOOR_ERROR: _Optional[bool] = ..., OTHER_ALARM: _Optional[bool] = ..., OTHER_WARNING: _Optional[bool] = ..., CONFIGURATION_ALARM: _Optional[bool] = ...) -> None: ...
    N_MOD_FIELD_NUMBER: _ClassVar[int]
    ST_FIELD_NUMBER: _ClassVar[int]
    CON_FAIL_FIELD_NUMBER: _ClassVar[int]
    N_CELL_BAL_FIELD_NUMBER: _ClassVar[int]
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
    CELL_V_AVG_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MAX_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MIN_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
    MOD_TMP_AVG_FIELD_NUMBER: _ClassVar[int]
    CON_ST_FIELD_NUMBER: _ClassVar[int]
    EVT1_FIELD_NUMBER: _ClassVar[int]
    EVT2_FIELD_NUMBER: _ClassVar[int]
    EVT_VND1_FIELD_NUMBER: _ClassVar[int]
    EVT_VND2_FIELD_NUMBER: _ClassVar[int]
    SET_ENA_FIELD_NUMBER: _ClassVar[int]
    SET_CON_FIELD_NUMBER: _ClassVar[int]
    MODS_FIELD_NUMBER: _ClassVar[int]
    n_mod: int
    st: FlatEsdString.St
    con_fail: FlatEsdString.ConFail
    n_cell_bal: int
    soc: float
    dod: float
    n_cyc: float
    soh: float
    a: float
    v: float
    cell_v_max: float
    cell_v_max_mod: int
    cell_v_min: float
    cell_v_min_mod: int
    cell_v_avg: float
    mod_tmp_max: float
    mod_tmp_max_mod: int
    mod_tmp_min: float
    mod_tmp_min_mod: int
    mod_tmp_avg: float
    con_st: FlatEsdString.ConSt
    evt1: FlatEsdString.Evt1
    evt2: int
    evt_vnd1: int
    evt_vnd2: int
    set_ena: FlatEsdString.SetEna
    set_con: FlatEsdString.SetCon
    mods: _containers.RepeatedCompositeFieldContainer[FlatEsdModule]
    def __init__(self, n_mod: _Optional[int] = ..., st: _Optional[_Union[FlatEsdString.St, _Mapping]] = ..., con_fail: _Optional[_Union[FlatEsdString.ConFail, str]] = ..., n_cell_bal: _Optional[int] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., n_cyc: _Optional[float] = ..., soh: _Optional[float] = ..., a: _Optional[float] = ..., v: _Optional[float] = ..., cell_v_max: _Optional[float] = ..., cell_v_max_mod: _Optional[int] = ..., cell_v_min: _Optional[float] = ..., cell_v_min_mod: _Optional[int] = ..., cell_v_avg: _Optional[float] = ..., mod_tmp_max: _Optional[float] = ..., mod_tmp_max_mod: _Optional[int] = ..., mod_tmp_min: _Optional[float] = ..., mod_tmp_min_mod: _Optional[int] = ..., mod_tmp_avg: _Optional[float] = ..., con_st: _Optional[_Union[FlatEsdString.ConSt, _Mapping]] = ..., evt1: _Optional[_Union[FlatEsdString.Evt1, _Mapping]] = ..., evt2: _Optional[int] = ..., evt_vnd1: _Optional[int] = ..., evt_vnd2: _Optional[int] = ..., set_ena: _Optional[_Union[FlatEsdString.SetEna, str]] = ..., set_con: _Optional[_Union[FlatEsdString.SetCon, str]] = ..., mods: _Optional[_Iterable[_Union[FlatEsdModule, _Mapping]]] = ...) -> None: ...

class FlatEsdStringCommand(_message.Message):
    __slots__ = ("set_ena", "set_con")
    SET_ENA_FIELD_NUMBER: _ClassVar[int]
    SET_CON_FIELD_NUMBER: _ClassVar[int]
    set_ena: FlatEsdString.SetEna
    set_con: FlatEsdString.SetCon
    def __init__(self, set_ena: _Optional[_Union[FlatEsdString.SetEna, str]] = ..., set_con: _Optional[_Union[FlatEsdString.SetCon, str]] = ...) -> None: ...

class EsdStringCommands(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[FlatEsdStringCommand]
    def __init__(self, commands: _Optional[_Iterable[_Union[FlatEsdStringCommand, _Mapping]]] = ...) -> None: ...

class FlatEsdModule(_message.Message):
    __slots__ = ("str_idx", "mod_idx", "n_cell", "soc", "dod", "soh", "n_cyc", "v", "cell_v_max", "cell_v_max_cell", "cell_v_min", "cell_v_min_cell", "cell_v_avg", "cell_tmp_max", "cell_tmp_max_cell", "cell_tmp_min", "cell_tmp_min_cell", "cell_tmp_avg", "n_cell_bal", "sn", "cells")
    STR_IDX_FIELD_NUMBER: _ClassVar[int]
    MOD_IDX_FIELD_NUMBER: _ClassVar[int]
    N_CELL_FIELD_NUMBER: _ClassVar[int]
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MAX_CELL_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_FIELD_NUMBER: _ClassVar[int]
    CELL_V_MIN_CELL_FIELD_NUMBER: _ClassVar[int]
    CELL_V_AVG_FIELD_NUMBER: _ClassVar[int]
    CELL_TMP_MAX_FIELD_NUMBER: _ClassVar[int]
    CELL_TMP_MAX_CELL_FIELD_NUMBER: _ClassVar[int]
    CELL_TMP_MIN_FIELD_NUMBER: _ClassVar[int]
    CELL_TMP_MIN_CELL_FIELD_NUMBER: _ClassVar[int]
    CELL_TMP_AVG_FIELD_NUMBER: _ClassVar[int]
    N_CELL_BAL_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    str_idx: int
    mod_idx: int
    n_cell: int
    soc: float
    dod: float
    soh: float
    n_cyc: float
    v: float
    cell_v_max: float
    cell_v_max_cell: int
    cell_v_min: float
    cell_v_min_cell: int
    cell_v_avg: float
    cell_tmp_max: float
    cell_tmp_max_cell: int
    cell_tmp_min: float
    cell_tmp_min_cell: int
    cell_tmp_avg: float
    n_cell_bal: int
    sn: str
    cells: _containers.RepeatedCompositeFieldContainer[FlatEsdCell]
    def __init__(self, str_idx: _Optional[int] = ..., mod_idx: _Optional[int] = ..., n_cell: _Optional[int] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., soh: _Optional[float] = ..., n_cyc: _Optional[float] = ..., v: _Optional[float] = ..., cell_v_max: _Optional[float] = ..., cell_v_max_cell: _Optional[int] = ..., cell_v_min: _Optional[float] = ..., cell_v_min_cell: _Optional[int] = ..., cell_v_avg: _Optional[float] = ..., cell_tmp_max: _Optional[float] = ..., cell_tmp_max_cell: _Optional[int] = ..., cell_tmp_min: _Optional[float] = ..., cell_tmp_min_cell: _Optional[int] = ..., cell_tmp_avg: _Optional[float] = ..., n_cell_bal: _Optional[int] = ..., sn: _Optional[str] = ..., cells: _Optional[_Iterable[_Union[FlatEsdCell, _Mapping]]] = ...) -> None: ...

class FlatEsdCell(_message.Message):
    __slots__ = ("cell_v", "cell_tmp", "cell_st")
    class CellSt(_message.Message):
        __slots__ = ("cell_is_balancing",)
        CELL_IS_BALANCING_FIELD_NUMBER: _ClassVar[int]
        cell_is_balancing: bool
        def __init__(self, cell_is_balancing: _Optional[bool] = ...) -> None: ...
    CELL_V_FIELD_NUMBER: _ClassVar[int]
    CELL_TMP_FIELD_NUMBER: _ClassVar[int]
    CELL_ST_FIELD_NUMBER: _ClassVar[int]
    cell_v: float
    cell_tmp: float
    cell_st: FlatEsdCell.CellSt
    def __init__(self, cell_v: _Optional[float] = ..., cell_tmp: _Optional[float] = ..., cell_st: _Optional[_Union[FlatEsdCell.CellSt, _Mapping]] = ...) -> None: ...
