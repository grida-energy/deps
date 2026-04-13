from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALARM_TYPE_UNSPECIFIED: _ClassVar[AlarmType]
    ALARM_TYPE_STATUS: _ClassVar[AlarmType]
    ALARM_TYPE_WARNING: _ClassVar[AlarmType]
    ALARM_TYPE_FAULT: _ClassVar[AlarmType]
ALARM_TYPE_UNSPECIFIED: AlarmType
ALARM_TYPE_STATUS: AlarmType
ALARM_TYPE_WARNING: AlarmType
ALARM_TYPE_FAULT: AlarmType

class AlarmMeta(_message.Message):
    __slots__ = ("status", "warning", "fault")
    class StatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class WarningEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class FaultEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    status: _containers.ScalarMap[int, str]
    warning: _containers.ScalarMap[int, str]
    fault: _containers.ScalarMap[int, str]
    def __init__(self, status: _Optional[_Mapping[int, str]] = ..., warning: _Optional[_Mapping[int, str]] = ..., fault: _Optional[_Mapping[int, str]] = ...) -> None: ...

class AlarmData(_message.Message):
    __slots__ = ("status", "warning", "fault")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedScalarFieldContainer[bool]
    warning: _containers.RepeatedScalarFieldContainer[bool]
    fault: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, status: _Optional[_Iterable[bool]] = ..., warning: _Optional[_Iterable[bool]] = ..., fault: _Optional[_Iterable[bool]] = ...) -> None: ...
