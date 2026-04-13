import datetime

from deps.vnd.alarm import v1_pb2 as _v1_pb2
from deps.vnd.parameter import v1_pb2 as _v1_pb2_1
from deps.rpc.header import v1_pb2 as _v1_pb2_1_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Rpc(_message.Message):
    __slots__ = ()
    class AlarmResponse(_message.Message):
        __slots__ = ("timestamp", "payload")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        payload: _v1_pb2.AlarmData
        def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_v1_pb2.AlarmData, _Mapping]] = ...) -> None: ...
    class ParamReadWriteRequest(_message.Message):
        __slots__ = ("reads", "writes")
        READS_FIELD_NUMBER: _ClassVar[int]
        WRITES_FIELD_NUMBER: _ClassVar[int]
        reads: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.ParamIdRange]
        writes: _v1_pb2_1.ParamBlock
        def __init__(self, reads: _Optional[_Iterable[_Union[_v1_pb2_1.ParamIdRange, _Mapping]]] = ..., writes: _Optional[_Union[_v1_pb2_1.ParamBlock, _Mapping]] = ...) -> None: ...
    class ParamReadWriteResponse(_message.Message):
        __slots__ = ("reads", "writes")
        READS_FIELD_NUMBER: _ClassVar[int]
        WRITES_FIELD_NUMBER: _ClassVar[int]
        reads: _v1_pb2_1.ParamBlock
        writes: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.ParamIdRange]
        def __init__(self, reads: _Optional[_Union[_v1_pb2_1.ParamBlock, _Mapping]] = ..., writes: _Optional[_Iterable[_Union[_v1_pb2_1.ParamIdRange, _Mapping]]] = ...) -> None: ...
    class ParamRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1_1.Request
        payload: Rpc.ParamReadWriteRequest
        def __init__(self, header: _Optional[_Union[_v1_pb2_1_1.Request, _Mapping]] = ..., payload: _Optional[_Union[Rpc.ParamReadWriteRequest, _Mapping]] = ...) -> None: ...
    class ParamResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1_1.Response
        payload: Rpc.ParamReadWriteResponse
        def __init__(self, header: _Optional[_Union[_v1_pb2_1_1.Response, _Mapping]] = ..., payload: _Optional[_Union[Rpc.ParamReadWriteResponse, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
