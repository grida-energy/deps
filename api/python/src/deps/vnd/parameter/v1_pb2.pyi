from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParamInfo(_message.Message):
    __slots__ = ("param_name", "description", "unit", "min_max", "pick", "schema", "accepts")
    class ParamKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARAM_KIND_NA: _ClassVar[ParamInfo.ParamKind]
        PARAM_KIND_NULL: _ClassVar[ParamInfo.ParamKind]
        PARAM_KIND_NUMBER: _ClassVar[ParamInfo.ParamKind]
        PARAM_KIND_STRING: _ClassVar[ParamInfo.ParamKind]
        PARAM_KIND_BOOL: _ClassVar[ParamInfo.ParamKind]
        PARAM_KIND_STRUCT: _ClassVar[ParamInfo.ParamKind]
        PARAM_KIND_LIST: _ClassVar[ParamInfo.ParamKind]
    PARAM_KIND_NA: ParamInfo.ParamKind
    PARAM_KIND_NULL: ParamInfo.ParamKind
    PARAM_KIND_NUMBER: ParamInfo.ParamKind
    PARAM_KIND_STRING: ParamInfo.ParamKind
    PARAM_KIND_BOOL: ParamInfo.ParamKind
    PARAM_KIND_STRUCT: ParamInfo.ParamKind
    PARAM_KIND_LIST: ParamInfo.ParamKind
    class MinMax(_message.Message):
        __slots__ = ("min", "max", "exclusive_min", "exclusive_max")
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        EXCLUSIVE_MIN_FIELD_NUMBER: _ClassVar[int]
        EXCLUSIVE_MAX_FIELD_NUMBER: _ClassVar[int]
        min: float
        max: float
        exclusive_min: bool
        exclusive_max: bool
        def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., exclusive_min: _Optional[bool] = ..., exclusive_max: _Optional[bool] = ...) -> None: ...
    class OneOfPick(_message.Message):
        __slots__ = ("options",)
        class OptionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: float
            def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        options: _containers.ScalarMap[str, float]
        def __init__(self, options: _Optional[_Mapping[str, float]] = ...) -> None: ...
    PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    MIN_MAX_FIELD_NUMBER: _ClassVar[int]
    PICK_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ACCEPTS_FIELD_NUMBER: _ClassVar[int]
    param_name: str
    description: str
    unit: str
    min_max: ParamInfo.MinMax
    pick: ParamInfo.OneOfPick
    schema: _descriptor_pb2.FileDescriptorSet
    accepts: _containers.RepeatedScalarFieldContainer[ParamInfo.ParamKind]
    def __init__(self, param_name: _Optional[str] = ..., description: _Optional[str] = ..., unit: _Optional[str] = ..., min_max: _Optional[_Union[ParamInfo.MinMax, _Mapping]] = ..., pick: _Optional[_Union[ParamInfo.OneOfPick, _Mapping]] = ..., schema: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ..., accepts: _Optional[_Iterable[_Union[ParamInfo.ParamKind, str]]] = ...) -> None: ...

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
