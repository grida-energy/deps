import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_ASC: _ClassVar[Order]
    ORDER_DESC: _ClassVar[Order]

class LogKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_KIND_EVENT: _ClassVar[LogKind]
    LOG_KIND_ALARM: _ClassVar[LogKind]
    LOG_KIND_COMMAND: _ClassVar[LogKind]

class AlarmKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALARM_KIND_STATUS: _ClassVar[AlarmKind]
    ALARM_KIND_WARNING: _ClassVar[AlarmKind]
    ALARM_KIND_FAULT: _ClassVar[AlarmKind]

class AlarmStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALARM_STATUS_CLEAR: _ClassVar[AlarmStatus]
    ALARM_STATUS_TRIGGER: _ClassVar[AlarmStatus]
ORDER_ASC: Order
ORDER_DESC: Order
LOG_KIND_EVENT: LogKind
LOG_KIND_ALARM: LogKind
LOG_KIND_COMMAND: LogKind
ALARM_KIND_STATUS: AlarmKind
ALARM_KIND_WARNING: AlarmKind
ALARM_KIND_FAULT: AlarmKind
ALARM_STATUS_CLEAR: AlarmStatus
ALARM_STATUS_TRIGGER: AlarmStatus

class LogMatch(_message.Message):
    __slots__ = ("log_kind", "source_like", "name_like", "alarm_kind", "target_like", "alarm_status")
    LOG_KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LIKE_FIELD_NUMBER: _ClassVar[int]
    NAME_LIKE_FIELD_NUMBER: _ClassVar[int]
    ALARM_KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIKE_FIELD_NUMBER: _ClassVar[int]
    ALARM_STATUS_FIELD_NUMBER: _ClassVar[int]
    log_kind: LogKind
    source_like: str
    name_like: str
    alarm_kind: AlarmKind
    target_like: str
    alarm_status: AlarmStatus
    def __init__(self, log_kind: _Optional[_Union[LogKind, str]] = ..., source_like: _Optional[str] = ..., name_like: _Optional[str] = ..., alarm_kind: _Optional[_Union[AlarmKind, str]] = ..., target_like: _Optional[str] = ..., alarm_status: _Optional[_Union[AlarmStatus, str]] = ...) -> None: ...

class LogConstraint(_message.Message):
    __slots__ = ("start", "end", "matches", "limit", "order")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    matches: _containers.RepeatedCompositeFieldContainer[LogMatch]
    limit: int
    order: Order
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., matches: _Optional[_Iterable[_Union[LogMatch, _Mapping]]] = ..., limit: _Optional[int] = ..., order: _Optional[_Union[Order, str]] = ...) -> None: ...

class EventExtra(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _struct_pb2.Struct
    def __init__(self, tags: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class AlarmExtra(_message.Message):
    __slots__ = ("kind", "status")
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    kind: AlarmKind
    status: AlarmStatus
    def __init__(self, kind: _Optional[_Union[AlarmKind, str]] = ..., status: _Optional[_Union[AlarmStatus, str]] = ...) -> None: ...

class CommandExtra(_message.Message):
    __slots__ = ("target", "parameters")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    target: str
    parameters: _struct_pb2.Struct
    def __init__(self, target: _Optional[str] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class LogItem(_message.Message):
    __slots__ = ("timestamp", "source", "name", "event", "alarm", "command")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ALARM_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    source: str
    name: str
    event: EventExtra
    alarm: AlarmExtra
    command: CommandExtra
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[str] = ..., name: _Optional[str] = ..., event: _Optional[_Union[EventExtra, _Mapping]] = ..., alarm: _Optional[_Union[AlarmExtra, _Mapping]] = ..., command: _Optional[_Union[CommandExtra, _Mapping]] = ...) -> None: ...

class MeasureId(_message.Message):
    __slots__ = ("source", "paths")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    source: str
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, source: _Optional[str] = ..., paths: _Optional[_Iterable[str]] = ...) -> None: ...

class MeasureConstraint(_message.Message):
    __slots__ = ("start", "end", "measures", "limit", "order")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    MEASURES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    measures: _containers.RepeatedCompositeFieldContainer[MeasureId]
    limit: int
    order: Order
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., measures: _Optional[_Iterable[_Union[MeasureId, _Mapping]]] = ..., limit: _Optional[int] = ..., order: _Optional[_Union[Order, str]] = ...) -> None: ...
