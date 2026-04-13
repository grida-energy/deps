import datetime

from deps.rpc.header import v1_pb2 as _v1_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeItem(_message.Message):
    __slots__ = ("node_id", "kind", "path_prefix", "args")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    kind: str
    path_prefix: str
    args: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, node_id: _Optional[str] = ..., kind: _Optional[str] = ..., path_prefix: _Optional[str] = ..., args: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class DeleteNode(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    def __init__(self, node_id: _Optional[str] = ...) -> None: ...

class MeasureRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocalRms(_message.Message):
    __slots__ = ("nodes",)
    class Command(_message.Message):
        __slots__ = ("create_node", "delete_node", "measure_request")
        CREATE_NODE_FIELD_NUMBER: _ClassVar[int]
        DELETE_NODE_FIELD_NUMBER: _ClassVar[int]
        MEASURE_REQUEST_FIELD_NUMBER: _ClassVar[int]
        create_node: NodeItem
        delete_node: DeleteNode
        measure_request: MeasureRequest
        def __init__(self, create_node: _Optional[_Union[NodeItem, _Mapping]] = ..., delete_node: _Optional[_Union[DeleteNode, _Mapping]] = ..., measure_request: _Optional[_Union[MeasureRequest, _Mapping]] = ...) -> None: ...
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[NodeItem]
    def __init__(self, nodes: _Optional[_Iterable[_Union[NodeItem, _Mapping]]] = ...) -> None: ...

class Rpc(_message.Message):
    __slots__ = ()
    class MeasureResponse(_message.Message):
        __slots__ = ("timestamp", "payload")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        payload: LocalRms
        def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[LocalRms, _Mapping]] = ...) -> None: ...
    class CommandRequest(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Request
        payload: _containers.RepeatedCompositeFieldContainer[LocalRms.Command]
        def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[LocalRms.Command, _Mapping]]] = ...) -> None: ...
    class CommandResponse(_message.Message):
        __slots__ = ("header", "payload")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        header: _v1_pb2.Response
        payload: int
        def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
