import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CastHeader(_message.Message):
    __slots__ = ()
    CASTSTAMP_FIELD_NUMBER: _ClassVar[int]
    POINTSTAMP_FIELD_NUMBER: _ClassVar[int]
    LEADTIME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    caststamp: _timestamp_pb2.Timestamp
    pointstamp: _timestamp_pb2.Timestamp
    leadtime: _duration_pb2.Duration
    kind: int
    def __init__(self, caststamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pointstamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., leadtime: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., kind: _Optional[int] = ...) -> None: ...

class StationCast(_message.Message):
    __slots__ = ()
    HEADER_FIELD_NUMBER: _ClassVar[int]
    W_CAP_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    header: CastHeader
    w_cap: float
    wh: float
    def __init__(self, header: _Optional[_Union[CastHeader, _Mapping]] = ..., w_cap: _Optional[float] = ..., wh: _Optional[float] = ...) -> None: ...

class H2StationMeasure(_message.Message):
    __slots__ = ()
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    KG_CAP_FIELD_NUMBER: _ClassVar[int]
    KG_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    kg_cap: float
    kg: float
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., kg_cap: _Optional[float] = ..., kg: _Optional[float] = ...) -> None: ...

class WindData(_message.Message):
    __slots__ = ()
    MPS_SPD_FIELD_NUMBER: _ClassVar[int]
    DEG_DIR_FIELD_NUMBER: _ClassVar[int]
    mps_spd: float
    deg_dir: float
    def __init__(self, mps_spd: _Optional[float] = ..., deg_dir: _Optional[float] = ...) -> None: ...

class WeatherCast(_message.Message):
    __slots__ = ()
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TMP_FIELD_NUMBER: _ClassVar[int]
    RH_FIELD_NUMBER: _ClassVar[int]
    IRR_FIELD_NUMBER: _ClassVar[int]
    WIND_FIELD_NUMBER: _ClassVar[int]
    header: CastHeader
    tmp: _containers.RepeatedScalarFieldContainer[float]
    rh: _containers.RepeatedScalarFieldContainer[float]
    irr: _containers.RepeatedScalarFieldContainer[float]
    wind: _containers.RepeatedCompositeFieldContainer[WindData]
    def __init__(self, header: _Optional[_Union[CastHeader, _Mapping]] = ..., tmp: _Optional[_Iterable[float]] = ..., rh: _Optional[_Iterable[float]] = ..., irr: _Optional[_Iterable[float]] = ..., wind: _Optional[_Iterable[_Union[WindData, _Mapping]]] = ...) -> None: ...

class GridOperation(_message.Message):
    __slots__ = ()
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    W_DMND_FIELD_NUMBER: _ClassVar[int]
    W_PV_FIELD_NUMBER: _ClassVar[int]
    W_WIND_FIELD_NUMBER: _ClassVar[int]
    W_RE_TOT_FIELD_NUMBER: _ClassVar[int]
    W_CAP_SUP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    w_dmnd: float
    w_pv: float
    w_wind: float
    w_re_tot: float
    w_cap_sup: float
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., w_dmnd: _Optional[float] = ..., w_pv: _Optional[float] = ..., w_wind: _Optional[float] = ..., w_re_tot: _Optional[float] = ..., w_cap_sup: _Optional[float] = ...) -> None: ...

class GridOutputControl(_message.Message):
    __slots__ = ()
    HEADER_FIELD_NUMBER: _ClassVar[int]
    W_P_M2_CTL_FIELD_NUMBER: _ClassVar[int]
    W_P_M2_MIN_FIELD_NUMBER: _ClassVar[int]
    header: CastHeader
    w_p_m2_ctl: float
    w_p_m2_min: float
    def __init__(self, header: _Optional[_Union[CastHeader, _Mapping]] = ..., w_p_m2_ctl: _Optional[float] = ..., w_p_m2_min: _Optional[float] = ...) -> None: ...

class EnergyCast(_message.Message):
    __slots__ = ()
    HEADER_FIELD_NUMBER: _ClassVar[int]
    W_CAP_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    W_TOT_FIELD_NUMBER: _ClassVar[int]
    W_MIN_FIELD_NUMBER: _ClassVar[int]
    W_MAX_FIELD_NUMBER: _ClassVar[int]
    header: CastHeader
    w_cap: float
    w: _containers.RepeatedScalarFieldContainer[float]
    w_tot: float
    w_min: float
    w_max: float
    def __init__(self, header: _Optional[_Union[CastHeader, _Mapping]] = ..., w_cap: _Optional[float] = ..., w: _Optional[_Iterable[float]] = ..., w_tot: _Optional[float] = ..., w_min: _Optional[float] = ..., w_max: _Optional[float] = ...) -> None: ...
