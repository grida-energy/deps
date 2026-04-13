import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from deps.rpc.header import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Rpc(_message.Message):
    __slots__ = ()
    class Bank(_message.Message):
        __slots__ = ()
        class MeasureResponse(_message.Message):
            __slots__ = ("timestamp", "payload")
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_FIELD_NUMBER: _ClassVar[int]
            timestamp: _timestamp_pb2.Timestamp
            payload: EsdBank
            def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[EsdBank, _Mapping]] = ...) -> None: ...
        class CommandRequest(_message.Message):
            __slots__ = ("header", "payload")
            HEADER_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_FIELD_NUMBER: _ClassVar[int]
            header: _v1_pb2.Request
            payload: _containers.RepeatedCompositeFieldContainer[EsdBank.Command]
            def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[EsdBank.Command, _Mapping]]] = ...) -> None: ...
        class CommandResponse(_message.Message):
            __slots__ = ("header", "payload")
            HEADER_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_FIELD_NUMBER: _ClassVar[int]
            header: _v1_pb2.Response
            payload: int
            def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[int] = ...) -> None: ...
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class EsdBank(_message.Message):
    __slots__ = ("st", "st_cha", "cnt_mod", "cnt_str", "cnt_cell", "soc", "dod", "soh", "n_cyc", "hb", "v", "a", "a_cha_max", "a_discha_max", "w", "status", "warning", "fault", "strs")
    class StCha(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_CHA_NA: _ClassVar[EsdBank.StCha]
        ST_CHA_STOP: _ClassVar[EsdBank.StCha]
        ST_CHA_EMPTY: _ClassVar[EsdBank.StCha]
        ST_CHA_DISCHARGING: _ClassVar[EsdBank.StCha]
        ST_CHA_CHARGING: _ClassVar[EsdBank.StCha]
        ST_CHA_FULL: _ClassVar[EsdBank.StCha]
        ST_CHA_HOLDING: _ClassVar[EsdBank.StCha]
        ST_CHA_TESTING: _ClassVar[EsdBank.StCha]
    ST_CHA_NA: EsdBank.StCha
    ST_CHA_STOP: EsdBank.StCha
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
        ST_FAULT: _ClassVar[EsdBank.St]
    ST_NA: EsdBank.St
    ST_DISCONNECTED: EsdBank.St
    ST_INITIALIZING: EsdBank.St
    ST_CONNECTED: EsdBank.St
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
        __slots__ = ("conn", "reset")
        CONN_FIELD_NUMBER: _ClassVar[int]
        RESET_FIELD_NUMBER: _ClassVar[int]
        conn: bool
        reset: bool
        def __init__(self, conn: _Optional[bool] = ..., reset: _Optional[bool] = ...) -> None: ...
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
    strs: _containers.RepeatedCompositeFieldContainer[EsdString]
    def __init__(self, st: _Optional[_Union[EsdBank.St, str]] = ..., st_cha: _Optional[_Union[EsdBank.StCha, str]] = ..., cnt_mod: _Optional[_Union[EsdBank.ModuleCount, _Mapping]] = ..., cnt_str: _Optional[_Union[EsdBank.StringCount, _Mapping]] = ..., cnt_cell: _Optional[_Union[EsdBank.CellCount, _Mapping]] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., soh: _Optional[float] = ..., n_cyc: _Optional[int] = ..., hb: _Optional[int] = ..., v: _Optional[float] = ..., a: _Optional[float] = ..., a_cha_max: _Optional[float] = ..., a_discha_max: _Optional[float] = ..., w: _Optional[float] = ..., status: _Optional[_Union[EsdBank.Status, _Mapping]] = ..., warning: _Optional[_Union[EsdBank.Warning, _Mapping]] = ..., fault: _Optional[_Union[EsdBank.Fault, _Mapping]] = ..., strs: _Optional[_Iterable[_Union[EsdString, _Mapping]]] = ...) -> None: ...

class EsdString(_message.Message):
    __slots__ = ("con_fail", "soc", "dod", "n_cyc", "soh", "a", "v", "cnt_cell", "cnt_mod", "st_con", "status", "warning", "fault", "mods")
    class ConFail(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CON_FAIL_NA: _ClassVar[EsdString.ConFail]
        CON_FAIL_NO_FAILURE: _ClassVar[EsdString.ConFail]
        CON_FAIL_BUTTON_PUSHED: _ClassVar[EsdString.ConFail]
        CON_FAIL_STR_GROUND_FAULT: _ClassVar[EsdString.ConFail]
        CON_FAIL_OUTSIDE_VOLTAGE_RANGE: _ClassVar[EsdString.ConFail]
        CON_FAIL_STRING_NOT_ENABLED: _ClassVar[EsdString.ConFail]
        CON_FAIL_FUSE_OPEN: _ClassVar[EsdString.ConFail]
        CON_FAIL_CONTACTOR_FAILURE: _ClassVar[EsdString.ConFail]
        CON_FAIL_PRECHARGE_FAILURE: _ClassVar[EsdString.ConFail]
        CON_FAIL_STRING_FAULT: _ClassVar[EsdString.ConFail]
    CON_FAIL_NA: EsdString.ConFail
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
        __slots__ = ("conn",)
        CONN_FIELD_NUMBER: _ClassVar[int]
        conn: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, conn: _Optional[_Iterable[bool]] = ...) -> None: ...
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
    mods: _containers.RepeatedCompositeFieldContainer[EsdModule]
    def __init__(self, con_fail: _Optional[_Union[EsdString.ConFail, str]] = ..., soc: _Optional[float] = ..., dod: _Optional[float] = ..., n_cyc: _Optional[int] = ..., soh: _Optional[float] = ..., a: _Optional[float] = ..., v: _Optional[float] = ..., cnt_cell: _Optional[_Union[EsdString.CellCount, _Mapping]] = ..., cnt_mod: _Optional[_Union[EsdString.ModuleCount, _Mapping]] = ..., st_con: _Optional[_Union[EsdString.StCon, _Mapping]] = ..., status: _Optional[_Union[EsdString.Status, _Mapping]] = ..., warning: _Optional[_Union[EsdString.Warning, _Mapping]] = ..., fault: _Optional[_Union[EsdString.Fault, _Mapping]] = ..., mods: _Optional[_Iterable[_Union[EsdModule, _Mapping]]] = ...) -> None: ...

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
