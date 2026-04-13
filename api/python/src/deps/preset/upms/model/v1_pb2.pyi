import datetime

from deps.rpc.header import v1_pb2 as _v1_pb2
from deps.model.pms.model import v1_pb2 as _v1_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PmsCommand(_message.Message):
    __slots__ = ("lookup",)
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    lookup: _v1_pb2_1.LookupRule.Command
    def __init__(self, lookup: _Optional[_Union[_v1_pb2_1.LookupRule.Command, _Mapping]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class MeasureResponse(_message.Message):
        __slots__ = ("timestamp", "lookup", "input", "output")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        LOOKUP_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        lookup: _v1_pb2_1.LookupRule
        input: _v1_pb2_1.LookupInput
        output: _v1_pb2_1.LookupOutput
        def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., lookup: _Optional[_Union[_v1_pb2_1.LookupRule, _Mapping]] = ..., input: _Optional[_Union[_v1_pb2_1.LookupInput, _Mapping]] = ..., output: _Optional[_Union[_v1_pb2_1.LookupOutput, _Mapping]] = ...) -> None: ...
    class CommandRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Request
        payload: _containers.RepeatedCompositeFieldContainer[PmsCommand]
        def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[PmsCommand, _Mapping]]] = ...) -> None: ...
    class CommandResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Response
        payload: int
        def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
