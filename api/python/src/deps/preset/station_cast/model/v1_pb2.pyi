import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from deps.model.cast.model import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CastSet(_message.Message):
    __slots__ = ("cst_stn", "h2", "forecast")
    CST_STN_FIELD_NUMBER: _ClassVar[int]
    H2_FIELD_NUMBER: _ClassVar[int]
    FORECAST_FIELD_NUMBER: _ClassVar[int]
    cst_stn: _v1_pb2.StationCast
    h2: _v1_pb2.H2StationMeasure
    forecast: _v1_pb2.WeatherCast
    def __init__(self, cst_stn: _Optional[_Union[_v1_pb2.StationCast, _Mapping]] = ..., h2: _Optional[_Union[_v1_pb2.H2StationMeasure, _Mapping]] = ..., forecast: _Optional[_Union[_v1_pb2.WeatherCast, _Mapping]] = ...) -> None: ...

class StationCastPreset(_message.Message):
    __slots__ = ("group", "ops_grid", "ctl_grid", "cst_dmnd", "cst_re")
    class GroupEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CastSet
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CastSet, _Mapping]] = ...) -> None: ...
    GROUP_FIELD_NUMBER: _ClassVar[int]
    OPS_GRID_FIELD_NUMBER: _ClassVar[int]
    CTL_GRID_FIELD_NUMBER: _ClassVar[int]
    CST_DMND_FIELD_NUMBER: _ClassVar[int]
    CST_RE_FIELD_NUMBER: _ClassVar[int]
    group: _containers.MessageMap[str, CastSet]
    ops_grid: _v1_pb2.GridOperation
    ctl_grid: _v1_pb2.GridOutputControl
    cst_dmnd: _v1_pb2.EnergyCast
    cst_re: _v1_pb2.EnergyCast
    def __init__(self, group: _Optional[_Mapping[str, CastSet]] = ..., ops_grid: _Optional[_Union[_v1_pb2.GridOperation, _Mapping]] = ..., ctl_grid: _Optional[_Union[_v1_pb2.GridOutputControl, _Mapping]] = ..., cst_dmnd: _Optional[_Union[_v1_pb2.EnergyCast, _Mapping]] = ..., cst_re: _Optional[_Union[_v1_pb2.EnergyCast, _Mapping]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class CastMeasure(_message.Message):
        __slots__ = ("timestamp", "data")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        data: StationCastPreset
        def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data: _Optional[_Union[StationCastPreset, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
