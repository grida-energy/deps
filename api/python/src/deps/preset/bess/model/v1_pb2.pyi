import datetime

from deps.model.esd.model import v1_pb2 as _v1_pb2
from deps.model.pcs.model import v1_pb2 as _v1_pb2_1
from deps.model.source.model import v1_pb2 as _v1_pb2_1_1
from deps.rpc.header import v1_pb2 as _v1_pb2_1_1_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bess(_message.Message):
    __slots__ = ("battery", "pcs", "off_grid", "on_grid")
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    PCS_FIELD_NUMBER: _ClassVar[int]
    OFF_GRID_FIELD_NUMBER: _ClassVar[int]
    ON_GRID_FIELD_NUMBER: _ClassVar[int]
    battery: _v1_pb2.EsdBank
    pcs: _v1_pb2_1.ThreePhasePcsPart
    off_grid: _v1_pb2_1.ThreePhaseGridPart
    on_grid: _v1_pb2_1.ThreePhaseGridPart
    def __init__(self, battery: _Optional[_Union[_v1_pb2.EsdBank, _Mapping]] = ..., pcs: _Optional[_Union[_v1_pb2_1.ThreePhasePcsPart, _Mapping]] = ..., off_grid: _Optional[_Union[_v1_pb2_1.ThreePhaseGridPart, _Mapping]] = ..., on_grid: _Optional[_Union[_v1_pb2_1.ThreePhaseGridPart, _Mapping]] = ...) -> None: ...

class BessMeasure(_message.Message):
    __slots__ = ("timestamp", "data")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    data: Bess
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data: _Optional[_Union[Bess, _Mapping]] = ...) -> None: ...

class BessCommand(_message.Message):
    __slots__ = ("battery", "pcs")
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    PCS_FIELD_NUMBER: _ClassVar[int]
    battery: _v1_pb2.EsdBank.Command
    pcs: _v1_pb2_1.ThreePhasePcsPart.Command
    def __init__(self, battery: _Optional[_Union[_v1_pb2.EsdBank.Command, _Mapping]] = ..., pcs: _Optional[_Union[_v1_pb2_1.ThreePhasePcsPart.Command, _Mapping]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class BessRequest(_message.Message):
        __slots__ = ("head", "data")
        HEAD_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        head: _v1_pb2_1_1_1.Request
        data: BessCommand
        def __init__(self, head: _Optional[_Union[_v1_pb2_1_1_1.Request, _Mapping]] = ..., data: _Optional[_Union[BessCommand, _Mapping]] = ...) -> None: ...
    class BessResponse(_message.Message):
        __slots__ = ("head",)
        HEAD_FIELD_NUMBER: _ClassVar[int]
        head: _v1_pb2_1_1_1.Response
        def __init__(self, head: _Optional[_Union[_v1_pb2_1_1_1.Response, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class HybridBess(_message.Message):
    __slots__ = ("battery", "pcs", "off_grid", "on_grid", "pv")
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    PCS_FIELD_NUMBER: _ClassVar[int]
    OFF_GRID_FIELD_NUMBER: _ClassVar[int]
    ON_GRID_FIELD_NUMBER: _ClassVar[int]
    PV_FIELD_NUMBER: _ClassVar[int]
    battery: _v1_pb2.EsdBank
    pcs: _v1_pb2_1.ThreePhasePcsPart
    off_grid: _v1_pb2_1.ThreePhaseGridPart
    on_grid: _v1_pb2_1.ThreePhaseGridPart
    pv: _v1_pb2_1_1.PvLine
    def __init__(self, battery: _Optional[_Union[_v1_pb2.EsdBank, _Mapping]] = ..., pcs: _Optional[_Union[_v1_pb2_1.ThreePhasePcsPart, _Mapping]] = ..., off_grid: _Optional[_Union[_v1_pb2_1.ThreePhaseGridPart, _Mapping]] = ..., on_grid: _Optional[_Union[_v1_pb2_1.ThreePhaseGridPart, _Mapping]] = ..., pv: _Optional[_Union[_v1_pb2_1_1.PvLine, _Mapping]] = ...) -> None: ...

class HybridBessMeasure(_message.Message):
    __slots__ = ("timestamp", "data")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    data: HybridBess
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data: _Optional[_Union[HybridBess, _Mapping]] = ...) -> None: ...
