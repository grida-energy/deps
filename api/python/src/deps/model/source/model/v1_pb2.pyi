from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PvString(_message.Message):
    __slots__ = ("v", "a", "w")
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    v: float
    a: float
    w: float
    def __init__(self, v: _Optional[float] = ..., a: _Optional[float] = ..., w: _Optional[float] = ...) -> None: ...

class PvLine(_message.Message):
    __slots__ = ("strings",)
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    strings: _containers.RepeatedCompositeFieldContainer[PvString]
    def __init__(self, strings: _Optional[_Iterable[_Union[PvString, _Mapping]]] = ...) -> None: ...
