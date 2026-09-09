from deps.model.nameplate.v2 import nameplate_pb2 as _nameplate_pb2
from deps.rpc.header import v1_pb2 as _v1_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("header", "payload")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    header: _v1_pb2.Request
    payload: _nameplate_pb2.NameplateFilter
    def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Union[_nameplate_pb2.NameplateFilter, _Mapping]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("header", "payload")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    header: _v1_pb2.Response
    payload: _nameplate_pb2.Nameplate
    def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[_Union[_nameplate_pb2.Nameplate, _Mapping]] = ...) -> None: ...
