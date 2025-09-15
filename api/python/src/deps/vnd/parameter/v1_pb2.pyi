from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParamInfo(_message.Message):
    __slots__ = ("param_name", "description", "unit", "min_max", "pick")
    class MinMax(_message.Message):
        __slots__ = ("min", "max")
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        min: float
        max: float
        def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...
    class Enum(_message.Message):
        __slots__ = ("collections",)
        class CollectionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: str
            def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
        COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
        collections: _containers.ScalarMap[int, str]
        def __init__(self, collections: _Optional[_Mapping[int, str]] = ...) -> None: ...
    PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    MIN_MAX_FIELD_NUMBER: _ClassVar[int]
    PICK_FIELD_NUMBER: _ClassVar[int]
    param_name: str
    description: str
    unit: str
    min_max: ParamInfo.MinMax
    pick: ParamInfo.Enum
    def __init__(self, param_name: _Optional[str] = ..., description: _Optional[str] = ..., unit: _Optional[str] = ..., min_max: _Optional[_Union[ParamInfo.MinMax, _Mapping]] = ..., pick: _Optional[_Union[ParamInfo.Enum, _Mapping]] = ...) -> None: ...

class ParamMeta(_message.Message):
    __slots__ = ("param_infos",)
    class ParamInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ParamInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ParamInfo, _Mapping]] = ...) -> None: ...
    PARAM_INFOS_FIELD_NUMBER: _ClassVar[int]
    param_infos: _containers.MessageMap[int, ParamInfo]
    def __init__(self, param_infos: _Optional[_Mapping[int, ParamInfo]] = ...) -> None: ...

class ParamIdRange(_message.Message):
    __slots__ = ("start", "length")
    START_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    start: int
    length: int
    def __init__(self, start: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ParamBlock(_message.Message):
    __slots__ = ("ranges", "values")
    RANGES_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[ParamIdRange]
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    def __init__(self, ranges: _Optional[_Iterable[_Union[ParamIdRange, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ...) -> None: ...
