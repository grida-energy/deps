from deps.model.net.model import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ThreePhaseLine(_message.Message):
    __slots__ = ("ph_ab", "ph_bc", "ph_ca")
    PH_AB_FIELD_NUMBER: _ClassVar[int]
    PH_BC_FIELD_NUMBER: _ClassVar[int]
    PH_CA_FIELD_NUMBER: _ClassVar[int]
    ph_ab: float
    ph_bc: float
    ph_ca: float
    def __init__(self, ph_ab: _Optional[float] = ..., ph_bc: _Optional[float] = ..., ph_ca: _Optional[float] = ...) -> None: ...

class ThreePhase(_message.Message):
    __slots__ = ("ph_a", "ph_b", "ph_c")
    PH_A_FIELD_NUMBER: _ClassVar[int]
    PH_B_FIELD_NUMBER: _ClassVar[int]
    PH_C_FIELD_NUMBER: _ClassVar[int]
    ph_a: float
    ph_b: float
    ph_c: float
    def __init__(self, ph_a: _Optional[float] = ..., ph_b: _Optional[float] = ..., ph_c: _Optional[float] = ...) -> None: ...

class ThreePhaseNSum(_message.Message):
    __slots__ = ("ph_a", "ph_b", "ph_c", "sum")
    PH_A_FIELD_NUMBER: _ClassVar[int]
    PH_B_FIELD_NUMBER: _ClassVar[int]
    PH_C_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    ph_a: float
    ph_b: float
    ph_c: float
    sum: float
    def __init__(self, ph_a: _Optional[float] = ..., ph_b: _Optional[float] = ..., ph_c: _Optional[float] = ..., sum: _Optional[float] = ...) -> None: ...

class ThreePhasePcsPart(_message.Message):
    __slots__ = ("st", "status", "fault", "warning", "dir_pwr", "ph_v", "pp_v", "a", "w", "hz", "va", "var", "pf", "dc", "tmp")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_NA: _ClassVar[ThreePhasePcsPart.St]
        ST_OFF: _ClassVar[ThreePhasePcsPart.St]
        ST_SLEEPING: _ClassVar[ThreePhasePcsPart.St]
        ST_STARTING: _ClassVar[ThreePhasePcsPart.St]
        ST_SHUTTING_DOWN: _ClassVar[ThreePhasePcsPart.St]
        ST_FAULT: _ClassVar[ThreePhasePcsPart.St]
        ST_STANDBY: _ClassVar[ThreePhasePcsPart.St]
        ST_OPERATION: _ClassVar[ThreePhasePcsPart.St]
        ST_BYPASS: _ClassVar[ThreePhasePcsPart.St]
    ST_NA: ThreePhasePcsPart.St
    ST_OFF: ThreePhasePcsPart.St
    ST_SLEEPING: ThreePhasePcsPart.St
    ST_STARTING: ThreePhasePcsPart.St
    ST_SHUTTING_DOWN: ThreePhasePcsPart.St
    ST_FAULT: ThreePhasePcsPart.St
    ST_STANDBY: ThreePhasePcsPart.St
    ST_OPERATION: ThreePhasePcsPart.St
    ST_BYPASS: ThreePhasePcsPart.St
    class DirPwr(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIR_PWR_NA: _ClassVar[ThreePhasePcsPart.DirPwr]
        DIR_PWR_STOP: _ClassVar[ThreePhasePcsPart.DirPwr]
        DIR_PWR_DC_TO_AC: _ClassVar[ThreePhasePcsPart.DirPwr]
        DIR_PWR_AC_TO_DC: _ClassVar[ThreePhasePcsPart.DirPwr]
    DIR_PWR_NA: ThreePhasePcsPart.DirPwr
    DIR_PWR_STOP: ThreePhasePcsPart.DirPwr
    DIR_PWR_DC_TO_AC: ThreePhasePcsPart.DirPwr
    DIR_PWR_AC_TO_DC: ThreePhasePcsPart.DirPwr
    class Fault(_message.Message):
        __slots__ = ("OTHER", "AC_OVER_VOLT", "AC_UNDER_VOLT", "OVER_FREQUENCY", "UNDER_FREQUENCY", "OVER_CURRENT", "GROUND_FAULT", "DC_OVER_VOLT", "OVER_TEMP", "UNDER_TEMP", "AC_UNBALANCE_VOLT", "AC_UNBALANCE_CURRENT", "HW_TEST_FAILURE", "CB_TRIP")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        AC_OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        AC_UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        OVER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        UNDER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        OVER_CURRENT_FIELD_NUMBER: _ClassVar[int]
        GROUND_FAULT_FIELD_NUMBER: _ClassVar[int]
        DC_OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        AC_UNBALANCE_VOLT_FIELD_NUMBER: _ClassVar[int]
        AC_UNBALANCE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        HW_TEST_FAILURE_FIELD_NUMBER: _ClassVar[int]
        CB_TRIP_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        AC_OVER_VOLT: bool
        AC_UNDER_VOLT: bool
        OVER_FREQUENCY: bool
        UNDER_FREQUENCY: bool
        OVER_CURRENT: bool
        GROUND_FAULT: bool
        DC_OVER_VOLT: bool
        OVER_TEMP: bool
        UNDER_TEMP: bool
        AC_UNBALANCE_VOLT: bool
        AC_UNBALANCE_CURRENT: bool
        HW_TEST_FAILURE: bool
        CB_TRIP: bool
        def __init__(self, OTHER: _Optional[bool] = ..., AC_OVER_VOLT: _Optional[bool] = ..., AC_UNDER_VOLT: _Optional[bool] = ..., OVER_FREQUENCY: _Optional[bool] = ..., UNDER_FREQUENCY: _Optional[bool] = ..., OVER_CURRENT: _Optional[bool] = ..., GROUND_FAULT: _Optional[bool] = ..., DC_OVER_VOLT: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., AC_UNBALANCE_VOLT: _Optional[bool] = ..., AC_UNBALANCE_CURRENT: _Optional[bool] = ..., HW_TEST_FAILURE: _Optional[bool] = ..., CB_TRIP: _Optional[bool] = ...) -> None: ...
    class Warning(_message.Message):
        __slots__ = ("OTHER", "AC_OVER_VOLT", "AC_UNDER_VOLT", "OVER_FREQUENCY", "UNDER_FREQUENCY", "OVER_LOAD", "DC_OVER_VOLT", "OVER_TEMP", "UNDER_TEMP", "AC_UNBALANCE_VOLT", "AC_UNBALANCE_CURRENT")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        AC_OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        AC_UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        OVER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        UNDER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        OVER_LOAD_FIELD_NUMBER: _ClassVar[int]
        DC_OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        AC_UNBALANCE_VOLT_FIELD_NUMBER: _ClassVar[int]
        AC_UNBALANCE_CURRENT_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        AC_OVER_VOLT: bool
        AC_UNDER_VOLT: bool
        OVER_FREQUENCY: bool
        UNDER_FREQUENCY: bool
        OVER_LOAD: bool
        DC_OVER_VOLT: bool
        OVER_TEMP: bool
        UNDER_TEMP: bool
        AC_UNBALANCE_VOLT: bool
        AC_UNBALANCE_CURRENT: bool
        def __init__(self, OTHER: _Optional[bool] = ..., AC_OVER_VOLT: _Optional[bool] = ..., AC_UNDER_VOLT: _Optional[bool] = ..., OVER_FREQUENCY: _Optional[bool] = ..., UNDER_FREQUENCY: _Optional[bool] = ..., OVER_LOAD: _Optional[bool] = ..., DC_OVER_VOLT: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., AC_UNBALANCE_VOLT: _Optional[bool] = ..., AC_UNBALANCE_CURRENT: _Optional[bool] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("OTHER", "AC_DISCONNECT", "DC_DISCONNECT", "GRID_DISCONNECT", "MANUAL_SHUTDOWN", "OPEN_DOOR", "THROTTLED", "MPPT", "UNDER_COOL", "SPD")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        AC_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
        DC_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
        GRID_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
        MANUAL_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        OPEN_DOOR_FIELD_NUMBER: _ClassVar[int]
        THROTTLED_FIELD_NUMBER: _ClassVar[int]
        MPPT_FIELD_NUMBER: _ClassVar[int]
        UNDER_COOL_FIELD_NUMBER: _ClassVar[int]
        SPD_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        AC_DISCONNECT: bool
        DC_DISCONNECT: bool
        GRID_DISCONNECT: bool
        MANUAL_SHUTDOWN: bool
        OPEN_DOOR: bool
        THROTTLED: bool
        MPPT: bool
        UNDER_COOL: bool
        SPD: bool
        def __init__(self, OTHER: _Optional[bool] = ..., AC_DISCONNECT: _Optional[bool] = ..., DC_DISCONNECT: _Optional[bool] = ..., GRID_DISCONNECT: _Optional[bool] = ..., MANUAL_SHUTDOWN: _Optional[bool] = ..., OPEN_DOOR: _Optional[bool] = ..., THROTTLED: _Optional[bool] = ..., MPPT: _Optional[bool] = ..., UNDER_COOL: _Optional[bool] = ..., SPD: _Optional[bool] = ...) -> None: ...
    class Command(_message.Message):
        __slots__ = ("action", "ref")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_NA: _ClassVar[ThreePhasePcsPart.Command.Action]
            ACTION_CONNECT: _ClassVar[ThreePhasePcsPart.Command.Action]
            ACTION_DISCONNECT: _ClassVar[ThreePhasePcsPart.Command.Action]
            ACTION_RESET_ALARM: _ClassVar[ThreePhasePcsPart.Command.Action]
        ACTION_NA: ThreePhasePcsPart.Command.Action
        ACTION_CONNECT: ThreePhasePcsPart.Command.Action
        ACTION_DISCONNECT: ThreePhasePcsPart.Command.Action
        ACTION_RESET_ALARM: ThreePhasePcsPart.Command.Action
        class Reference(_message.Message):
            __slots__ = ("a", "v", "w", "dcv", "dca", "p_pct", "q_pct", "pf", "hz")
            A_FIELD_NUMBER: _ClassVar[int]
            V_FIELD_NUMBER: _ClassVar[int]
            W_FIELD_NUMBER: _ClassVar[int]
            DCV_FIELD_NUMBER: _ClassVar[int]
            DCA_FIELD_NUMBER: _ClassVar[int]
            P_PCT_FIELD_NUMBER: _ClassVar[int]
            Q_PCT_FIELD_NUMBER: _ClassVar[int]
            PF_FIELD_NUMBER: _ClassVar[int]
            HZ_FIELD_NUMBER: _ClassVar[int]
            a: float
            v: float
            w: float
            dcv: float
            dca: float
            p_pct: float
            q_pct: float
            pf: float
            hz: float
            def __init__(self, a: _Optional[float] = ..., v: _Optional[float] = ..., w: _Optional[float] = ..., dcv: _Optional[float] = ..., dca: _Optional[float] = ..., p_pct: _Optional[float] = ..., q_pct: _Optional[float] = ..., pf: _Optional[float] = ..., hz: _Optional[float] = ...) -> None: ...
        ACTION_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        action: ThreePhasePcsPart.Command.Action
        ref: ThreePhasePcsPart.Command.Reference
        def __init__(self, action: _Optional[_Union[ThreePhasePcsPart.Command.Action, str]] = ..., ref: _Optional[_Union[ThreePhasePcsPart.Command.Reference, _Mapping]] = ...) -> None: ...
    ST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    DIR_PWR_FIELD_NUMBER: _ClassVar[int]
    PH_V_FIELD_NUMBER: _ClassVar[int]
    PP_V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    DC_FIELD_NUMBER: _ClassVar[int]
    TMP_FIELD_NUMBER: _ClassVar[int]
    st: ThreePhasePcsPart.St
    status: ThreePhasePcsPart.Status
    fault: ThreePhasePcsPart.Fault
    warning: ThreePhasePcsPart.Warning
    dir_pwr: ThreePhasePcsPart.DirPwr
    ph_v: ThreePhase
    pp_v: ThreePhaseLine
    a: ThreePhaseNSum
    w: float
    hz: float
    va: float
    var: float
    pf: float
    dc: DcPart
    tmp: TemperaturePart
    def __init__(self, st: _Optional[_Union[ThreePhasePcsPart.St, str]] = ..., status: _Optional[_Union[ThreePhasePcsPart.Status, _Mapping]] = ..., fault: _Optional[_Union[ThreePhasePcsPart.Fault, _Mapping]] = ..., warning: _Optional[_Union[ThreePhasePcsPart.Warning, _Mapping]] = ..., dir_pwr: _Optional[_Union[ThreePhasePcsPart.DirPwr, str]] = ..., ph_v: _Optional[_Union[ThreePhase, _Mapping]] = ..., pp_v: _Optional[_Union[ThreePhaseLine, _Mapping]] = ..., a: _Optional[_Union[ThreePhaseNSum, _Mapping]] = ..., w: _Optional[float] = ..., hz: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., dc: _Optional[_Union[DcPart, _Mapping]] = ..., tmp: _Optional[_Union[TemperaturePart, _Mapping]] = ...) -> None: ...

class ThreePhaseGridPart(_message.Message):
    __slots__ = ("sum", "a", "b", "c")
    SUM_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    sum: _v1_pb2.AcLineSum
    a: _v1_pb2.AcLine
    b: _v1_pb2.AcLine
    c: _v1_pb2.AcLine
    def __init__(self, sum: _Optional[_Union[_v1_pb2.AcLineSum, _Mapping]] = ..., a: _Optional[_Union[_v1_pb2.AcLine, _Mapping]] = ..., b: _Optional[_Union[_v1_pb2.AcLine, _Mapping]] = ..., c: _Optional[_Union[_v1_pb2.AcLine, _Mapping]] = ...) -> None: ...

class DcPart(_message.Message):
    __slots__ = ("dca", "dcv", "dcw")
    DCA_FIELD_NUMBER: _ClassVar[int]
    DCV_FIELD_NUMBER: _ClassVar[int]
    DCW_FIELD_NUMBER: _ClassVar[int]
    dca: float
    dcv: float
    dcw: float
    def __init__(self, dca: _Optional[float] = ..., dcv: _Optional[float] = ..., dcw: _Optional[float] = ...) -> None: ...

class TemperaturePart(_message.Message):
    __slots__ = ("tmp_cab", "tmp_snk", "tmp_trns", "tmp_ot")
    TMP_CAB_FIELD_NUMBER: _ClassVar[int]
    TMP_SNK_FIELD_NUMBER: _ClassVar[int]
    TMP_TRNS_FIELD_NUMBER: _ClassVar[int]
    TMP_OT_FIELD_NUMBER: _ClassVar[int]
    tmp_cab: float
    tmp_snk: float
    tmp_trns: float
    tmp_ot: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, tmp_cab: _Optional[float] = ..., tmp_snk: _Optional[float] = ..., tmp_trns: _Optional[float] = ..., tmp_ot: _Optional[_Iterable[float]] = ...) -> None: ...

class DcDcConverter(_message.Message):
    __slots__ = ()
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_NA: _ClassVar[DcDcConverter.St]
    ST_NA: DcDcConverter.St
    class Fault(_message.Message):
        __slots__ = ("OTHER",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        def __init__(self, OTHER: _Optional[bool] = ...) -> None: ...
    class Warning(_message.Message):
        __slots__ = ("OTHER",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        def __init__(self, OTHER: _Optional[bool] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("OTHER",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        OTHER: bool
        def __init__(self, OTHER: _Optional[bool] = ...) -> None: ...
    class Command(_message.Message):
        __slots__ = ("enable",)
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        def __init__(self, enable: _Optional[bool] = ...) -> None: ...
    def __init__(self) -> None: ...
