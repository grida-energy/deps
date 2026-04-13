from deps.rpc.header import v1_pb2 as _v1_pb2
from deps.model.tsdb.model import v1_pb2 as _v1_pb2_1
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class rpc(_message.Message):
    __slots__ = ()
    class PullLogRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Request
        payload: _v1_pb2_1.LogConstraint
        def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Union[_v1_pb2_1.LogConstraint, _Mapping]] = ...) -> None: ...
    class PullLogResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Response
        payload: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.LogItem]
        def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[_v1_pb2_1.LogItem, _Mapping]]] = ...) -> None: ...
    class PullMeasureRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Request
        payload: _v1_pb2_1.MeasureConstraint
        def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Union[_v1_pb2_1.MeasureConstraint, _Mapping]] = ...) -> None: ...
    class PullMeasureResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Response
        payload: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
        def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
