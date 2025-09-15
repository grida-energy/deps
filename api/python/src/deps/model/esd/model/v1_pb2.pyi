from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EsdSummary(_message.Message):
    __slots__ = ("soc", "dod", "soh", "n_cyc", "cha_st", "hb", "state", "state_vnd", "evt1", "v", "v_max", "v_min", "cnt_cell", "a", "a_cha_max", "a_discha_max", "w", "set_op", "bank")
    class ChaSt(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHA_ST_NA: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_OFF: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_EMPTY: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_DISCHARGING: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_CHARGING: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_FULL: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_HOLDING: _ClassVar[EsdSummary.ChaSt]
        CHA_ST_TESTING: _ClassVar[EsdSummary.ChaSt]
    CHA_ST_NA: EsdSummary.ChaSt
    CHA_ST_OFF: EsdSummary.ChaSt
    CHA_ST_EMPTY: EsdSummary.ChaSt
    CHA_ST_DISCHARGING: EsdSummary.ChaSt
    CHA_ST_CHARGING: EsdSummary.ChaSt
    CHA_ST_FULL: EsdSummary.ChaSt
    CHA_ST_HOLDING: EsdSummary.ChaSt
    CHA_ST_TESTING: EsdSummary.ChaSt
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NA: _ClassVar[EsdSummary.State]
        STATE_DISCONNECTED: _ClassVar[EsdSummary.State]
        STATE_INITIALIZING: _ClassVar[EsdSummary.State]
        STATE_CONNECTED: _ClassVar[EsdSummary.State]
        STATE_STANDBY: _ClassVar[EsdSummary.State]
        STATE_SOC_PROTECTION: _ClassVar[EsdSummary.State]
        STATE_SUSPENDING: _ClassVar[EsdSummary.State]
        STATE_FAULT: _ClassVar[EsdSummary.State]
    STATE_NA: EsdSummary.State
    STATE_DISCONNECTED: EsdSummary.State
    STATE_INITIALIZING: EsdSummary.State
    STATE_CONNECTED: EsdSummary.State
    STATE_STANDBY: EsdSummary.State
    STATE_SOC_PROTECTION: EsdSummary.State
    STATE_SUSPENDING: EsdSummary.State
    STATE_FAULT: EsdSummary.State
    class SetOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SETOP_NA: _ClassVar[EsdSummary.SetOp]
        SETOP_CONNECT: _ClassVar[EsdSummary.SetOp]
        SETOP_DISCONNECT: _ClassVar[EsdSummary.SetOp]
    SETOP_NA: EsdSummary.SetOp
    SETOP_CONNECT: EsdSummary.SetOp
    SETOP_DISCONNECT: EsdSummary.SetOp
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
    class CellCount(_message.Message):
        __slots__ = ("v_max", "v_max_str", "v_max_mod", "v_min", "v_min_str", "v_min_mod", "v_avg")
        V_MAX_FIELD_NUMBER: _ClassVar[int]
        V_MAX_STR_FIELD_NUMBER: _ClassVar[int]
        V_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
        V_MIN_FIELD_NUMBER: _ClassVar[int]
        V_MIN_STR_FIELD_NUMBER: _ClassVar[int]
        V_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
        V_AVG_FIELD_NUMBER: _ClassVar[int]
        v_max: float
        v_max_str: int
        v_max_mod: int
        v_min: float
        v_min_str: int
        v_min_mod: int
        v_avg: float
        def __init__(self, v_max: _Optional[float] = ..., v_max_str: _Optional[int] = ..., v_max_mod: _Optional[int] = ..., v_min: _Optional[float] = ..., v_min_str: _Optional[int] = ..., v_min_mod: _Optional[int] = ..., v_avg: _Optional[float] = ...) -> None: ...
    class Command(_message.Message):
        __slots__ = ("set_op",)
        SET_OP_FIELD_NUMBER: _ClassVar[int]
        set_op: EsdSummary.SetOp
        def __init__(self, set_op: _Optional[_Union[EsdSummary.SetOp, str]] = ...) -> None: ...
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    CHA_ST_FIELD_NUMBER: _ClassVar[int]
    HB_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_VND_FIELD_NUMBER: _ClassVar[int]
    EVT1_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    V_MAX_FIELD_NUMBER: _ClassVar[int]
    V_MIN_FIELD_NUMBER: _ClassVar[int]
    CNT_CELL_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    A_CHA_MAX_FIELD_NUMBER: _ClassVar[int]
    A_DISCHA_MAX_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    SET_OP_FIELD_NUMBER: _ClassVar[int]
    BANK_FIELD_NUMBER: _ClassVar[int]
    soc: float
    dod: float
    soh: float
    n_cyc: int
    cha_st: EsdSummary.ChaSt
    hb: int
    state: EsdSummary.State
    state_vnd: int
    evt1: EsdSummary.Evt1
    v: float
    v_max: float
    v_min: float
    cnt_cell: EsdSummary.CellCount
    a: float
    a_cha_max: float
    a_discha_max: float
    w: float
    set_op: EsdSummary.SetOp
    bank: EsdBank
    def __init__(self, soc: _Optional[float] = ..., dod: _Optional[float] = ..., soh: _Optional[float] = ..., n_cyc: _Optional[int] = ..., cha_st: _Optional[_Union[EsdSummary.ChaSt, str]] = ..., hb: _Optional[int] = ..., state: _Optional[_Union[EsdSummary.State, str]] = ..., state_vnd: _Optional[int] = ..., evt1: _Optional[_Union[EsdSummary.Evt1, _Mapping]] = ..., v: _Optional[float] = ..., v_max: _Optional[float] = ..., v_min: _Optional[float] = ..., cnt_cell: _Optional[_Union[EsdSummary.CellCount, _Mapping]] = ..., a: _Optional[float] = ..., a_cha_max: _Optional[float] = ..., a_discha_max: _Optional[float] = ..., w: _Optional[float] = ..., set_op: _Optional[_Union[EsdSummary.SetOp, str]] = ..., bank: _Optional[_Union[EsdBank, _Mapping]] = ...) -> None: ...

class EsdBank(_message.Message):
    __slots__ = ("st", "st_cha", "cnt_mod", "cnt_str", "cnt_cell", "soc", "dod", "soh", "n_cyc", "hb", "v", "a", "a_cha_max", "a_discha_max", "w", "status", "warning", "fault", "set_op", "strs")
    class StCha(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_CHA_NA: _ClassVar[EsdBank.StCha]
        ST_CHA_OFF: _ClassVar[EsdBank.StCha]
        ST_CHA_EMPTY: _ClassVar[EsdBank.StCha]
        ST_CHA_DISCHARGING: _ClassVar[EsdBank.StCha]
        ST_CHA_CHARGING: _ClassVar[EsdBank.StCha]
        ST_CHA_FULL: _ClassVar[EsdBank.StCha]
        ST_CHA_HOLDING: _ClassVar[EsdBank.StCha]
        ST_CHA_TESTING: _ClassVar[EsdBank.StCha]
    ST_CHA_NA: EsdBank.StCha
    ST_CHA_OFF: EsdBank.StCha
    ST_CHA_EMPTY: EsdBank.StCha
    ST_CHA_DISCHARGING: EsdBank.StCha
    ST_CHA_CHARGING: EsdBank.StCha
    ST_CHA_FULL: EsdBank.StCha
    ST_CHA_HOLDING: EsdBank.StCha
    ST_CHA_TESTING: EsdBank.StCha
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_NA: _ClassVar[EsdBank.St]
        ST_DISCONNECTED: _ClassVar[EsdBank.St]
        ST_INITIALIZING: _ClassVar[EsdBank.St]
        ST_CONNECTED: _ClassVar[EsdBank.St]
        ST_STANDBY: _ClassVar[EsdBank.St]
        ST_SOC_PROTECTION: _ClassVar[EsdBank.St]
        ST_SUSPENDING: _ClassVar[EsdBank.St]
        ST_FAULT: _ClassVar[EsdBank.St]
    ST_NA: EsdBank.St
    ST_DISCONNECTED: EsdBank.St
    ST_INITIALIZING: EsdBank.St
    ST_CONNECTED: EsdBank.St
    ST_STANDBY: EsdBank.St
    ST_SOC_PROTECTION: EsdBank.St
    ST_SUSPENDING: EsdBank.St
    ST_FAULT: EsdBank.St
    class Status(_message.Message):
        __slots__ = ("OTHER", "OPEN_DOOR")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OPEN_DOOR_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        OPEN_DOOR: bool
        def __init__(self, OTHER: _Optional[bool] = ..., OPEN_DOOR: _Optional[bool] = ...) -> None: ...
    class Warning(_message.Message):
        __slots__ = ("OTHER", "OVER_TEMP", "UNDER_TEMP", "OVER_CHARGE_CURRENT", "OVER_DISCHARGE_CURRENT", "OVER_VOLT", "UNDER_VOLT", "UNDER_SOC_MIN", "OVER_SOC_MAX", "VOLTAGE_IMBALANCE", "TEMPERATURE_IMBALANCE", "CURRENT_IMBALANCE", "CONFIGURATION")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        OVER_TEMP: bool
        UNDER_TEMP: bool
        OVER_CHARGE_CURRENT: bool
        OVER_DISCHARGE_CURRENT: bool
        OVER_VOLT: bool
        UNDER_VOLT: bool
        UNDER_SOC_MIN: bool
        OVER_SOC_MAX: bool
        VOLTAGE_IMBALANCE: bool
        TEMPERATURE_IMBALANCE: bool
        CURRENT_IMBALANCE: bool
        CONFIGURATION: bool
        def __init__(self, OTHER: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., OVER_CHARGE_CURRENT: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT: _Optional[bool] = ..., OVER_VOLT: _Optional[bool] = ..., UNDER_VOLT: _Optional[bool] = ..., UNDER_SOC_MIN: _Optional[bool] = ..., OVER_SOC_MAX: _Optional[bool] = ..., VOLTAGE_IMBALANCE: _Optional[bool] = ..., TEMPERATURE_IMBALANCE: _Optional[bool] = ..., CURRENT_IMBALANCE: _Optional[bool] = ..., CONFIGURATION: _Optional[bool] = ...) -> None: ...
    class Fault(_message.Message):
        __slots__ = ("OTHER", "OVER_TEMP", "UNDER_TEMP", "OVER_CHARGE_CURRENT", "OVER_DISCHARGE_CURRENT", "OVER_VOLT", "UNDER_VOLT", "UNDER_SOC_MIN", "OVER_SOC_MAX", "VOLTAGE_IMBALANCE", "TEMPERATURE_IMBALANCE", "CURRENT_IMBALANCE", "CONFIGURATION", "COMMUNICATION_ERROR", "CONTACTOR_ERROR", "FAN_ERROR", "GROUND_FAULT")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        COMMUNICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_ERROR_FIELD_NUMBER: _ClassVar[int]
        FAN_ERROR_FIELD_NUMBER: _ClassVar[int]
        GROUND_FAULT_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        OVER_TEMP: bool
        UNDER_TEMP: bool
        OVER_CHARGE_CURRENT: bool
        OVER_DISCHARGE_CURRENT: bool
        OVER_VOLT: bool
        UNDER_VOLT: bool
        UNDER_SOC_MIN: bool
        OVER_SOC_MAX: bool
        VOLTAGE_IMBALANCE: bool
        TEMPERATURE_IMBALANCE: bool
        CURRENT_IMBALANCE: bool
        CONFIGURATION: bool
        COMMUNICATION_ERROR: bool
        CONTACTOR_ERROR: bool
        FAN_ERROR: bool
        GROUND_FAULT: bool
        def __init__(self, OTHER: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., OVER_CHARGE_CURRENT: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT: _Optional[bool] = ..., OVER_VOLT: _Optional[bool] = ..., UNDER_VOLT: _Optional[bool] = ..., UNDER_SOC_MIN: _Optional[bool] = ..., OVER_SOC_MAX: _Optional[bool] = ..., VOLTAGE_IMBALANCE: _Optional[bool] = ..., TEMPERATURE_IMBALANCE: _Optional[bool] = ..., CURRENT_IMBALANCE: _Optional[bool] = ..., CONFIGURATION: _Optional[bool] = ..., COMMUNICATION_ERROR: _Optional[bool] = ..., CONTACTOR_ERROR: _Optional[bool] = ..., FAN_ERROR: _Optional[bool] = ..., GROUND_FAULT: _Optional[bool] = ...) -> None: ...
    class Command(_message.Message):
        __slots__ = ("set_op",)
        class SetOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SET_OP_NA: _ClassVar[EsdBank.Command.SetOp]
            SET_OP_CONNECT: _ClassVar[EsdBank.Command.SetOp]
            SET_OP_DISCONNECT: _ClassVar[EsdBank.Command.SetOp]
        SET_OP_NA: EsdBank.Command.SetOp
        SET_OP_CONNECT: EsdBank.Command.SetOp
        SET_OP_DISCONNECT: EsdBank.Command.SetOp
        SET_OP_FIELD_NUMBER: _ClassVar[int]
        set_op: EsdBank.Command.SetOp
        def __init__(self, set_op: _Optional[_Union[EsdBank.Command.SetOp, str]] = ...) -> None: ...
    class CellCount(_message.Message):
        __slots__ = ("v_max", "v_max_str", "v_max_mod", "v_min", "v_min_str", "v_min_mod", "v_avg", "n_bal")
        V_MAX_FIELD_NUMBER: _ClassVar[int]
        V_MAX_STR_FIELD_NUMBER: _ClassVar[int]
        V_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
        V_MIN_FIELD_NUMBER: _ClassVar[int]
        V_MIN_STR_FIELD_NUMBER: _ClassVar[int]
        V_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
        V_AVG_FIELD_NUMBER: _ClassVar[int]
        N_BAL_FIELD_NUMBER: _ClassVar[int]
        v_max: float
        v_max_str: int
        v_max_mod: int
        v_min: float
        v_min_str: int
        v_min_mod: int
        v_avg: float
        n_bal: int
        def __init__(self, v_max: _Optional[float] = ..., v_max_str: _Optional[int] = ..., v_max_mod: _Optional[int] = ..., v_min: _Optional[float] = ..., v_min_str: _Optional[int] = ..., v_min_mod: _Optional[int] = ..., v_avg: _Optional[float] = ..., n_bal: _Optional[int] = ...) -> None: ...
    class ModuleCount(_message.Message):
        __slots__ = ("tmp_max", "tmp_max_str", "tmp_max_mod", "tmp_min", "tmp_min_str", "tmp_min_mod", "tmp_avg")
        TMP_MAX_FIELD_NUMBER: _ClassVar[int]
        TMP_MAX_STR_FIELD_NUMBER: _ClassVar[int]
        TMP_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_STR_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
        TMP_AVG_FIELD_NUMBER: _ClassVar[int]
        tmp_max: float
        tmp_max_str: int
        tmp_max_mod: int
        tmp_min: float
        tmp_min_str: int
        tmp_min_mod: int
        tmp_avg: float
        def __init__(self, tmp_max: _Optional[float] = ..., tmp_max_str: _Optional[int] = ..., tmp_max_mod: _Optional[int] = ..., tmp_min: _Optional[float] = ..., tmp_min_str: _Optional[int] = ..., tmp_min_mod: _Optional[int] = ..., tmp_avg: _Optional[float] = ...) -> None: ...
    class StringCount(_message.Message):
        __slots__ = ("v_max", "v_max_str", "v_min", "v_min_str", "v_avg", "a_max", "a_max_str", "a_min", "a_min_str", "a_avg", "n_conn")
        V_MAX_FIELD_NUMBER: _ClassVar[int]
        V_MAX_STR_FIELD_NUMBER: _ClassVar[int]
        V_MIN_FIELD_NUMBER: _ClassVar[int]
        V_MIN_STR_FIELD_NUMBER: _ClassVar[int]
        V_AVG_FIELD_NUMBER: _ClassVar[int]
        A_MAX_FIELD_NUMBER: _ClassVar[int]
        A_MAX_STR_FIELD_NUMBER: _ClassVar[int]
        A_MIN_FIELD_NUMBER: _ClassVar[int]
        A_MIN_STR_FIELD_NUMBER: _ClassVar[int]
        A_AVG_FIELD_NUMBER: _ClassVar[int]
        N_CONN_FIELD_NUMBER: _ClassVar[int]
        v_max: float
        v_max_str: int
        v_min: float
        v_min_str: int
        v_avg: float
        a_max: float
        a_max_str: int
        a_min: float
        a_min_str: int
        a_avg: float
        n_conn: int
        def __init__(self, v_max: _Optional[float] = ..., v_max_str: _Optional[int] = ..., v_min: _Optional[float] = ..., v_min_str: _Optional[int] = ..., v_avg: _Optional[float] = ..., a_max: _Optional[float] = ..., a_max_str: _Optional[int] = ..., a_min: _Optional[float] = ..., a_min_str: _Optional[int] = ..., a_avg: _Optional[float] = ..., n_conn: _Optional[int] = ...) -> None: ...
    ST_FIELD_NUMBER: _ClassVar[int]
    ST_CHA_FIELD_NUMBER: _ClassVar[int]
    CNT_MOD_FIELD_NUMBER: _ClassVar[int]
    CNT_STR_FIELD_NUMBER: _ClassVar[int]
    CNT_CELL_FIELD_NUMBER: _ClassVar[int]
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    HB_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    A_CHA_MAX_FIELD_NUMBER: _ClassVar[int]
    A_DISCHA_MAX_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    SET_OP_FIELD_NUMBER: _ClassVar[int]
    STRS_FIELD_NUMBER: _ClassVar[int]
    st: EsdBank.St
    st_cha: EsdBank.StCha
    cnt_mod: EsdBank.ModuleCount
    cnt_str: EsdBank.StringCount
    cnt_cell: EsdBank.CellCount
    soc: float
    dod: float
    soh: float
    n_cyc: int
    hb: int
    v: float
    a: float
    a_cha_max: float
    a_discha_max: float
    w: float
    status: EsdBank.Status
    warning: EsdBank.Warning
    fault: EsdBank.Fault
    set_op: EsdBank.Command.SetOp
    strs: _containers.RepeatedCompositeFieldContainer[EsdString]
    def __init__(self, st: _Optional[_Union[EsdBank.St, str]] = ..., st_cha: _Optional[_Union[EsdBank.StCha, str]] = ..., cnt_mod: _Optional[_Union[EsdBank.ModuleCount, _Mapping]] = ..., cnt_str: _Optional[_Union[EsdBank.StringCount, _Mapping]] = ..., cnt_cell: _Optional[_Union[EsdBank.CellCount, _Mapping]] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., soh: _Optional[float] = ..., n_cyc: _Optional[int] = ..., hb: _Optional[int] = ..., v: _Optional[float] = ..., a: _Optional[float] = ..., a_cha_max: _Optional[float] = ..., a_discha_max: _Optional[float] = ..., w: _Optional[float] = ..., status: _Optional[_Union[EsdBank.Status, _Mapping]] = ..., warning: _Optional[_Union[EsdBank.Warning, _Mapping]] = ..., fault: _Optional[_Union[EsdBank.Fault, _Mapping]] = ..., set_op: _Optional[_Union[EsdBank.Command.SetOp, str]] = ..., strs: _Optional[_Iterable[_Union[EsdString, _Mapping]]] = ...) -> None: ...

class EsdString(_message.Message):
    __slots__ = ("con_fail", "soc", "dod", "n_cyc", "soh", "a", "v", "cnt_cell", "cnt_mod", "st_con", "status", "warning", "fault", "set_ena", "set_con", "mods")
    class ConFail(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CON_FAIL_NO_FAILURE: _ClassVar[EsdString.ConFail]
        CON_FAIL_BUTTON_PUSHED: _ClassVar[EsdString.ConFail]
        CON_FAIL_STR_GROUND_FAULT: _ClassVar[EsdString.ConFail]
        CON_FAIL_OUTSIDE_VOLTAGE_RANGE: _ClassVar[EsdString.ConFail]
        CON_FAIL_STRING_NOT_ENABLED: _ClassVar[EsdString.ConFail]
        CON_FAIL_FUSE_OPEN: _ClassVar[EsdString.ConFail]
        CON_FAIL_CONTACTOR_FAILURE: _ClassVar[EsdString.ConFail]
        CON_FAIL_PRECHARGE_FAILURE: _ClassVar[EsdString.ConFail]
        CON_FAIL_STRING_FAULT: _ClassVar[EsdString.ConFail]
    CON_FAIL_NO_FAILURE: EsdString.ConFail
    CON_FAIL_BUTTON_PUSHED: EsdString.ConFail
    CON_FAIL_STR_GROUND_FAULT: EsdString.ConFail
    CON_FAIL_OUTSIDE_VOLTAGE_RANGE: EsdString.ConFail
    CON_FAIL_STRING_NOT_ENABLED: EsdString.ConFail
    CON_FAIL_FUSE_OPEN: EsdString.ConFail
    CON_FAIL_CONTACTOR_FAILURE: EsdString.ConFail
    CON_FAIL_PRECHARGE_FAILURE: EsdString.ConFail
    CON_FAIL_STRING_FAULT: EsdString.ConFail
    class StCon(_message.Message):
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
    class Status(_message.Message):
        __slots__ = ("OTHER", "OPEN_DOOR", "STRING_ENABLED", "CONTACTOR_STATUS")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OPEN_DOOR_FIELD_NUMBER: _ClassVar[int]
        STRING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_STATUS_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        OPEN_DOOR: bool
        STRING_ENABLED: bool
        CONTACTOR_STATUS: bool
        def __init__(self, OTHER: _Optional[bool] = ..., OPEN_DOOR: _Optional[bool] = ..., STRING_ENABLED: _Optional[bool] = ..., CONTACTOR_STATUS: _Optional[bool] = ...) -> None: ...
    class Warning(_message.Message):
        __slots__ = ("OTHER", "OVER_TEMP", "UNDER_TEMP", "OVER_CHARGE_CURRENT", "OVER_DISCHARGE_CURRENT", "OVER_VOLT", "UNDER_VOLT", "UNDER_SOC_MIN", "OVER_SOC_MAX", "VOLTAGE_IMBALANCE", "TEMPERATURE_IMBALANCE")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        OVER_TEMP: bool
        UNDER_TEMP: bool
        OVER_CHARGE_CURRENT: bool
        OVER_DISCHARGE_CURRENT: bool
        OVER_VOLT: bool
        UNDER_VOLT: bool
        UNDER_SOC_MIN: bool
        OVER_SOC_MAX: bool
        VOLTAGE_IMBALANCE: bool
        TEMPERATURE_IMBALANCE: bool
        def __init__(self, OTHER: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., OVER_CHARGE_CURRENT: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT: _Optional[bool] = ..., OVER_VOLT: _Optional[bool] = ..., UNDER_VOLT: _Optional[bool] = ..., UNDER_SOC_MIN: _Optional[bool] = ..., OVER_SOC_MAX: _Optional[bool] = ..., VOLTAGE_IMBALANCE: _Optional[bool] = ..., TEMPERATURE_IMBALANCE: _Optional[bool] = ...) -> None: ...
    class Fault(_message.Message):
        __slots__ = ("OTHER", "OVER_TEMP", "UNDER_TEMP", "OVER_CHARGE_CURRENT", "OVER_DISCHARGE_CURRENT", "OVER_VOLT", "UNDER_VOLT", "UNDER_SOC_MIN", "OVER_SOC_MAX", "VOLTAGE_IMBALANCE", "TEMPERATURE_IMBALANCE", "COMMUNICATION_ERROR", "CONFIGURATION", "CONTACTOR_ERROR", "FAN_ERROR", "GROUND_FAULT")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        OVER_CHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_DISCHARGE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        UNDER_SOC_MIN_FIELD_NUMBER: _ClassVar[int]
        OVER_SOC_MAX_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IMBALANCE_FIELD_NUMBER: _ClassVar[int]
        COMMUNICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        CONTACTOR_ERROR_FIELD_NUMBER: _ClassVar[int]
        FAN_ERROR_FIELD_NUMBER: _ClassVar[int]
        GROUND_FAULT_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        OVER_TEMP: bool
        UNDER_TEMP: bool
        OVER_CHARGE_CURRENT: bool
        OVER_DISCHARGE_CURRENT: bool
        OVER_VOLT: bool
        UNDER_VOLT: bool
        UNDER_SOC_MIN: bool
        OVER_SOC_MAX: bool
        VOLTAGE_IMBALANCE: bool
        TEMPERATURE_IMBALANCE: bool
        COMMUNICATION_ERROR: bool
        CONFIGURATION: bool
        CONTACTOR_ERROR: bool
        FAN_ERROR: bool
        GROUND_FAULT: bool
        def __init__(self, OTHER: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., OVER_CHARGE_CURRENT: _Optional[bool] = ..., OVER_DISCHARGE_CURRENT: _Optional[bool] = ..., OVER_VOLT: _Optional[bool] = ..., UNDER_VOLT: _Optional[bool] = ..., UNDER_SOC_MIN: _Optional[bool] = ..., OVER_SOC_MAX: _Optional[bool] = ..., VOLTAGE_IMBALANCE: _Optional[bool] = ..., TEMPERATURE_IMBALANCE: _Optional[bool] = ..., COMMUNICATION_ERROR: _Optional[bool] = ..., CONFIGURATION: _Optional[bool] = ..., CONTACTOR_ERROR: _Optional[bool] = ..., FAN_ERROR: _Optional[bool] = ..., GROUND_FAULT: _Optional[bool] = ...) -> None: ...
    class Command(_message.Message):
        __slots__ = ("set_con", "set_ena")
        class SetEna(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SET_ENA_NA: _ClassVar[EsdString.Command.SetEna]
            SET_ENA_ENABLE_STRING: _ClassVar[EsdString.Command.SetEna]
            SET_ENA_DISABLE_STRING: _ClassVar[EsdString.Command.SetEna]
        SET_ENA_NA: EsdString.Command.SetEna
        SET_ENA_ENABLE_STRING: EsdString.Command.SetEna
        SET_ENA_DISABLE_STRING: EsdString.Command.SetEna
        class SetCon(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SET_CON_NA: _ClassVar[EsdString.Command.SetCon]
            SET_CON_CONNECT_STRING: _ClassVar[EsdString.Command.SetCon]
            SET_CON_DISCONNECT_STRING: _ClassVar[EsdString.Command.SetCon]
        SET_CON_NA: EsdString.Command.SetCon
        SET_CON_CONNECT_STRING: EsdString.Command.SetCon
        SET_CON_DISCONNECT_STRING: EsdString.Command.SetCon
        SET_CON_FIELD_NUMBER: _ClassVar[int]
        SET_ENA_FIELD_NUMBER: _ClassVar[int]
        set_con: EsdString.Command.SetCon
        set_ena: EsdString.Command.SetEna
        def __init__(self, set_con: _Optional[_Union[EsdString.Command.SetCon, str]] = ..., set_ena: _Optional[_Union[EsdString.Command.SetEna, str]] = ...) -> None: ...
    class CellCount(_message.Message):
        __slots__ = ("v_max", "v_max_mod", "v_min", "v_min_mod", "v_avg", "n_cell_bal")
        V_MAX_FIELD_NUMBER: _ClassVar[int]
        V_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
        V_MIN_FIELD_NUMBER: _ClassVar[int]
        V_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
        V_AVG_FIELD_NUMBER: _ClassVar[int]
        N_CELL_BAL_FIELD_NUMBER: _ClassVar[int]
        v_max: float
        v_max_mod: int
        v_min: float
        v_min_mod: int
        v_avg: float
        n_cell_bal: int
        def __init__(self, v_max: _Optional[float] = ..., v_max_mod: _Optional[int] = ..., v_min: _Optional[float] = ..., v_min_mod: _Optional[int] = ..., v_avg: _Optional[float] = ..., n_cell_bal: _Optional[int] = ...) -> None: ...
    class ModuleCount(_message.Message):
        __slots__ = ("tmp_max", "tmp_max_mod", "tmp_min", "tmp_min_mod", "tmp_avg")
        TMP_MAX_FIELD_NUMBER: _ClassVar[int]
        TMP_MAX_MOD_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_MOD_FIELD_NUMBER: _ClassVar[int]
        TMP_AVG_FIELD_NUMBER: _ClassVar[int]
        tmp_max: float
        tmp_max_mod: int
        tmp_min: float
        tmp_min_mod: int
        tmp_avg: float
        def __init__(self, tmp_max: _Optional[float] = ..., tmp_max_mod: _Optional[int] = ..., tmp_min: _Optional[float] = ..., tmp_min_mod: _Optional[int] = ..., tmp_avg: _Optional[float] = ...) -> None: ...
    CON_FAIL_FIELD_NUMBER: _ClassVar[int]
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    CNT_CELL_FIELD_NUMBER: _ClassVar[int]
    CNT_MOD_FIELD_NUMBER: _ClassVar[int]
    ST_CON_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    SET_ENA_FIELD_NUMBER: _ClassVar[int]
    SET_CON_FIELD_NUMBER: _ClassVar[int]
    MODS_FIELD_NUMBER: _ClassVar[int]
    con_fail: EsdString.ConFail
    soc: float
    dod: float
    n_cyc: int
    soh: float
    a: float
    v: float
    cnt_cell: EsdString.CellCount
    cnt_mod: EsdString.ModuleCount
    st_con: EsdString.StCon
    status: EsdString.Status
    warning: EsdString.Warning
    fault: EsdString.Fault
    set_ena: EsdString.Command.SetEna
    set_con: EsdString.Command.SetCon
    mods: _containers.RepeatedCompositeFieldContainer[EsdModule]
    def __init__(self, con_fail: _Optional[_Union[EsdString.ConFail, str]] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., n_cyc: _Optional[int] = ..., soh: _Optional[float] = ..., a: _Optional[float] = ..., v: _Optional[float] = ..., cnt_cell: _Optional[_Union[EsdString.CellCount, _Mapping]] = ..., cnt_mod: _Optional[_Union[EsdString.ModuleCount, _Mapping]] = ..., st_con: _Optional[_Union[EsdString.StCon, _Mapping]] = ..., status: _Optional[_Union[EsdString.Status, _Mapping]] = ..., warning: _Optional[_Union[EsdString.Warning, _Mapping]] = ..., fault: _Optional[_Union[EsdString.Fault, _Mapping]] = ..., set_ena: _Optional[_Union[EsdString.Command.SetEna, str]] = ..., set_con: _Optional[_Union[EsdString.Command.SetCon, str]] = ..., mods: _Optional[_Iterable[_Union[EsdModule, _Mapping]]] = ...) -> None: ...

class EsdModule(_message.Message):
    __slots__ = ("str_idx", "mod_idx", "n_cell", "soc", "dod", "soh", "n_cyc", "v", "cnt_cell", "sn", "cells")
    class CellCount(_message.Message):
        __slots__ = ("v_max", "v_max_cell", "v_min", "v_min_cell", "v_avg", "tmp_max", "tmp_max_cell", "tmp_min", "tmp_min_cell", "tmp_avg", "n_bal")
        V_MAX_FIELD_NUMBER: _ClassVar[int]
        V_MAX_CELL_FIELD_NUMBER: _ClassVar[int]
        V_MIN_FIELD_NUMBER: _ClassVar[int]
        V_MIN_CELL_FIELD_NUMBER: _ClassVar[int]
        V_AVG_FIELD_NUMBER: _ClassVar[int]
        TMP_MAX_FIELD_NUMBER: _ClassVar[int]
        TMP_MAX_CELL_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_FIELD_NUMBER: _ClassVar[int]
        TMP_MIN_CELL_FIELD_NUMBER: _ClassVar[int]
        TMP_AVG_FIELD_NUMBER: _ClassVar[int]
        N_BAL_FIELD_NUMBER: _ClassVar[int]
        v_max: float
        v_max_cell: int
        v_min: float
        v_min_cell: int
        v_avg: float
        tmp_max: float
        tmp_max_cell: int
        tmp_min: float
        tmp_min_cell: int
        tmp_avg: float
        n_bal: int
        def __init__(self, v_max: _Optional[float] = ..., v_max_cell: _Optional[int] = ..., v_min: _Optional[float] = ..., v_min_cell: _Optional[int] = ..., v_avg: _Optional[float] = ..., tmp_max: _Optional[float] = ..., tmp_max_cell: _Optional[int] = ..., tmp_min: _Optional[float] = ..., tmp_min_cell: _Optional[int] = ..., tmp_avg: _Optional[float] = ..., n_bal: _Optional[int] = ...) -> None: ...
    STR_IDX_FIELD_NUMBER: _ClassVar[int]
    MOD_IDX_FIELD_NUMBER: _ClassVar[int]
    N_CELL_FIELD_NUMBER: _ClassVar[int]
    SOC_FIELD_NUMBER: _ClassVar[int]
    DOD_FIELD_NUMBER: _ClassVar[int]
    SOH_FIELD_NUMBER: _ClassVar[int]
    N_CYC_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    CNT_CELL_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    str_idx: int
    mod_idx: int
    n_cell: int
    soc: float
    dod: float
    soh: float
    n_cyc: int
    v: float
    cnt_cell: EsdModule.CellCount
    sn: str
    cells: _containers.RepeatedCompositeFieldContainer[EsdCell]
    def __init__(self, str_idx: _Optional[int] = ..., mod_idx: _Optional[int] = ..., n_cell: _Optional[int] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., soh: _Optional[float] = ..., n_cyc: _Optional[int] = ..., v: _Optional[float] = ..., cnt_cell: _Optional[_Union[EsdModule.CellCount, _Mapping]] = ..., sn: _Optional[str] = ..., cells: _Optional[_Iterable[_Union[EsdCell, _Mapping]]] = ...) -> None: ...

class EsdCell(_message.Message):
    __slots__ = ("v", "tmp", "st")
    class St(_message.Message):
        __slots__ = ("is_balancing",)
        IS_BALANCING_FIELD_NUMBER: _ClassVar[int]
        is_balancing: bool
        def __init__(self, is_balancing: _Optional[bool] = ...) -> None: ...
    V_FIELD_NUMBER: _ClassVar[int]
    TMP_FIELD_NUMBER: _ClassVar[int]
    ST_FIELD_NUMBER: _ClassVar[int]
    v: float
    tmp: float
    st: EsdCell.St
    def __init__(self, v: _Optional[float] = ..., tmp: _Optional[float] = ..., st: _Optional[_Union[EsdCell.St, _Mapping]] = ...) -> None: ...
