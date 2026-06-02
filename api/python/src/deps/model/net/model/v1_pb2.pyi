import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Line(_message.Message):
    __slots__ = ("v", "a", "w", "wh")
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    v: float
    a: float
    w: float
    wh: Energy
    def __init__(self, v: _Optional[float] = ..., a: _Optional[float] = ..., w: _Optional[float] = ..., wh: _Optional[_Union[Energy, _Mapping]] = ...) -> None: ...

class AcLine(_message.Message):
    __slots__ = ("v", "a", "hz", "w", "va", "var", "pf", "wh")
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    v: float
    a: float
    hz: float
    w: float
    va: float
    var: float
    pf: float
    wh: Energy
    def __init__(self, v: _Optional[float] = ..., a: _Optional[float] = ..., hz: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., wh: _Optional[_Union[Energy, _Mapping]] = ...) -> None: ...

class AcLineSum(_message.Message):
    __slots__ = ("a", "hz", "w", "va", "var", "pf", "wh")
    A_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    a: float
    hz: float
    w: float
    va: float
    var: float
    pf: float
    wh: Energy
    def __init__(self, a: _Optional[float] = ..., hz: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., wh: _Optional[_Union[Energy, _Mapping]] = ...) -> None: ...

class Energy(_message.Message):
    __slots__ = ("exported", "imported")
    EXPORTED_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FIELD_NUMBER: _ClassVar[int]
    exported: float
    imported: float
    def __init__(self, exported: _Optional[float] = ..., imported: _Optional[float] = ...) -> None: ...

class LineToLine(_message.Message):
    __slots__ = ("ab", "bc", "ca")
    AB_FIELD_NUMBER: _ClassVar[int]
    BC_FIELD_NUMBER: _ClassVar[int]
    CA_FIELD_NUMBER: _ClassVar[int]
    ab: float
    bc: float
    ca: float
    def __init__(self, ab: _Optional[float] = ..., bc: _Optional[float] = ..., ca: _Optional[float] = ...) -> None: ...

class AcLineThreePhase(_message.Message):
    __slots__ = ("sum", "a", "b", "c", "pp_v")
    SUM_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    PP_V_FIELD_NUMBER: _ClassVar[int]
    sum: AcLineSum
    a: AcLine
    b: AcLine
    c: AcLine
    pp_v: LineToLine
    def __init__(self, sum: _Optional[_Union[AcLineSum, _Mapping]] = ..., a: _Optional[_Union[AcLine, _Mapping]] = ..., b: _Optional[_Union[AcLine, _Mapping]] = ..., c: _Optional[_Union[AcLine, _Mapping]] = ..., pp_v: _Optional[_Union[LineToLine, _Mapping]] = ...) -> None: ...

class Phasor(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Harmonics(_message.Message):
    __slots__ = ("v_series", "a_series", "thd_v", "thd_a", "tdd_a", "phs_v", "phs_a")
    V_SERIES_FIELD_NUMBER: _ClassVar[int]
    A_SERIES_FIELD_NUMBER: _ClassVar[int]
    THD_V_FIELD_NUMBER: _ClassVar[int]
    THD_A_FIELD_NUMBER: _ClassVar[int]
    TDD_A_FIELD_NUMBER: _ClassVar[int]
    PHS_V_FIELD_NUMBER: _ClassVar[int]
    PHS_A_FIELD_NUMBER: _ClassVar[int]
    v_series: _containers.RepeatedScalarFieldContainer[float]
    a_series: _containers.RepeatedScalarFieldContainer[float]
    thd_v: float
    thd_a: float
    tdd_a: float
    phs_v: Phasor
    phs_a: Phasor
    def __init__(self, v_series: _Optional[_Iterable[float]] = ..., a_series: _Optional[_Iterable[float]] = ..., thd_v: _Optional[float] = ..., thd_a: _Optional[float] = ..., tdd_a: _Optional[float] = ..., phs_v: _Optional[_Union[Phasor, _Mapping]] = ..., phs_a: _Optional[_Union[Phasor, _Mapping]] = ...) -> None: ...

class HarmonicsThreePhase(_message.Message):
    __slots__ = ("a", "b", "c")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    a: Harmonics
    b: Harmonics
    c: Harmonics
    def __init__(self, a: _Optional[_Union[Harmonics, _Mapping]] = ..., b: _Optional[_Union[Harmonics, _Mapping]] = ..., c: _Optional[_Union[Harmonics, _Mapping]] = ...) -> None: ...

class MeterThreePhase(_message.Message):
    __slots__ = ("main", "harmonics")
    MAIN_FIELD_NUMBER: _ClassVar[int]
    HARMONICS_FIELD_NUMBER: _ClassVar[int]
    main: AcLineThreePhase
    harmonics: HarmonicsThreePhase
    def __init__(self, main: _Optional[_Union[AcLineThreePhase, _Mapping]] = ..., harmonics: _Optional[_Union[HarmonicsThreePhase, _Mapping]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class MeterThreePhase(_message.Message):
        __slots__ = ()
        class MeasureResponse(_message.Message):
            __slots__ = ("timestamp", "payload")
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_FIELD_NUMBER: _ClassVar[int]
            timestamp: _timestamp_pb2.Timestamp
            payload: MeterThreePhase
            def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[MeterThreePhase, _Mapping]] = ...) -> None: ...
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
