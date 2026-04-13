import datetime

from deps.model.esd.model import v1_pb2 as _v1_pb2
from deps.model.pcs.model import v1_pb2 as _v1_pb2_1
from deps.model.source.model import v1_pb2 as _v1_pb2_1_1
from deps.rpc.header import v1_pb2 as _v1_pb2_1_1_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bess(_message.Message):
    __slots__ = ("bank", "pcs", "off_grid", "on_grid", "dcdc", "pv")
    BANK_FIELD_NUMBER: _ClassVar[int]
    PCS_FIELD_NUMBER: _ClassVar[int]
    OFF_GRID_FIELD_NUMBER: _ClassVar[int]
    ON_GRID_FIELD_NUMBER: _ClassVar[int]
    DCDC_FIELD_NUMBER: _ClassVar[int]
    PV_FIELD_NUMBER: _ClassVar[int]
    bank: _v1_pb2.EsdBank
    pcs: _v1_pb2_1.ThreePhasePcsPart
    off_grid: _v1_pb2_1.ThreePhaseGridPart
    on_grid: _v1_pb2_1.ThreePhaseGridPart
    dcdc: _v1_pb2_1.DcDcConverter
    pv: _v1_pb2_1_1.PvLine
    def __init__(self, bank: _Optional[_Union[_v1_pb2.EsdBank, _Mapping]] = ..., pcs: _Optional[_Union[_v1_pb2_1.ThreePhasePcsPart, _Mapping]] = ..., off_grid: _Optional[_Union[_v1_pb2_1.ThreePhaseGridPart, _Mapping]] = ..., on_grid: _Optional[_Union[_v1_pb2_1.ThreePhaseGridPart, _Mapping]] = ..., dcdc: _Optional[_Union[_v1_pb2_1.DcDcConverter, _Mapping]] = ..., pv: _Optional[_Union[_v1_pb2_1_1.PvLine, _Mapping]] = ...) -> None: ...

class BessCommand(_message.Message):
    __slots__ = ("bank", "pcs", "dcdc")
    BANK_FIELD_NUMBER: _ClassVar[int]
    PCS_FIELD_NUMBER: _ClassVar[int]
    DCDC_FIELD_NUMBER: _ClassVar[int]
    bank: _v1_pb2.EsdBank.Command
    pcs: _v1_pb2_1.ThreePhasePcsPart.Command
    dcdc: _v1_pb2_1.DcDcConverter.Command
    def __init__(self, bank: _Optional[_Union[_v1_pb2.EsdBank.Command, _Mapping]] = ..., pcs: _Optional[_Union[_v1_pb2_1.ThreePhasePcsPart.Command, _Mapping]] = ..., dcdc: _Optional[_Union[_v1_pb2_1.DcDcConverter.Command, _Mapping]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class MeasureResponse(_message.Message):
        __slots__ = ("timestamp", "payload")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        payload: Bess
        def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[Bess, _Mapping]] = ...) -> None: ...
    class CommandRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1_1_1.Request
        payload: _containers.RepeatedCompositeFieldContainer[BessCommand]
        def __init__(self, header: _Optional[_Union[_v1_pb2_1_1_1.Request, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[BessCommand, _Mapping]]] = ...) -> None: ...
    class CommandResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1_1_1.Response
        payload: int
        def __init__(self, header: _Optional[_Union[_v1_pb2_1_1_1.Response, _Mapping]] = ..., payload: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
