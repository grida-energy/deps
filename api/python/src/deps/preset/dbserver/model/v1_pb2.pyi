from deps.model.nameplate.v2 import nameplate_pb2 as _nameplate_pb2
from deps.model.tsdb.model import v1_pb2 as _v1_pb2
from deps.rpc.header import v1_pb2 as _v1_pb2_1
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Query(_message.Message):
    __slots__ = ("measure_info", "measure", "log")
    class MeasureInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    MEASURE_INFO_FIELD_NUMBER: _ClassVar[int]
    MEASURE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    measure_info: Query.MeasureInfo
    measure: _v1_pb2.MeasureConstraint
    log: _v1_pb2.LogConstraint
    def __init__(self, measure_info: _Optional[_Union[Query.MeasureInfo, _Mapping]] = ..., measure: _Optional[_Union[_v1_pb2.MeasureConstraint, _Mapping]] = ..., log: _Optional[_Union[_v1_pb2.LogConstraint, _Mapping]] = ...) -> None: ...

class Answer(_message.Message):
    __slots__ = ("measure_info", "measure", "log")
    class MeasureMeta(_message.Message):
        __slots__ = ("name", "nodetype", "extra_kind")
        NAME_FIELD_NUMBER: _ClassVar[int]
        NODETYPE_FIELD_NUMBER: _ClassVar[int]
        EXTRA_KIND_FIELD_NUMBER: _ClassVar[int]
        name: str
        nodetype: _nameplate_pb2.Wknt
        extra_kind: str
        def __init__(self, name: _Optional[str] = ..., nodetype: _Optional[_Union[_nameplate_pb2.Wknt, str]] = ..., extra_kind: _Optional[str] = ...) -> None: ...
    class MeasureInfo(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[Answer.MeasureMeta]
        def __init__(self, values: _Optional[_Iterable[_Union[Answer.MeasureMeta, _Mapping]]] = ...) -> None: ...
    class Measure(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
        def __init__(self, values: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]] = ...) -> None: ...
    class Log(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.LogItem]
        def __init__(self, values: _Optional[_Iterable[_Union[_v1_pb2.LogItem, _Mapping]]] = ...) -> None: ...
    MEASURE_INFO_FIELD_NUMBER: _ClassVar[int]
    MEASURE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    measure_info: Answer.MeasureInfo
    measure: Answer.Measure
    log: Answer.Log
    def __init__(self, measure_info: _Optional[_Union[Answer.MeasureInfo, _Mapping]] = ..., measure: _Optional[_Union[Answer.Measure, _Mapping]] = ..., log: _Optional[_Union[Answer.Log, _Mapping]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class QueryRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1.Request
        payload: _containers.RepeatedCompositeFieldContainer[Query]
        def __init__(self, header: _Optional[_Union[_v1_pb2_1.Request, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[Query, _Mapping]]] = ...) -> None: ...
    class QueryResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1.Response
        payload: _containers.RepeatedCompositeFieldContainer[Answer]
        def __init__(self, header: _Optional[_Union[_v1_pb2_1.Response, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[Answer, _Mapping]]] = ...) -> None: ...
    class PullLogRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1.Request
        payload: _v1_pb2.LogConstraint
        def __init__(self, header: _Optional[_Union[_v1_pb2_1.Request, _Mapping]] = ..., payload: _Optional[_Union[_v1_pb2.LogConstraint, _Mapping]] = ...) -> None: ...
    class PullLogResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1.Response
        payload: _containers.RepeatedCompositeFieldContainer[_v1_pb2.LogItem]
        def __init__(self, header: _Optional[_Union[_v1_pb2_1.Response, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[_v1_pb2.LogItem, _Mapping]]] = ...) -> None: ...
    class PullMeasureRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1.Request
        payload: _v1_pb2.MeasureConstraint
        def __init__(self, header: _Optional[_Union[_v1_pb2_1.Request, _Mapping]] = ..., payload: _Optional[_Union[_v1_pb2.MeasureConstraint, _Mapping]] = ...) -> None: ...
    class PullMeasureResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2_1.Response
        payload: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
        def __init__(self, header: _Optional[_Union[_v1_pb2_1.Response, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
