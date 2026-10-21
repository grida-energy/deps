import datetime

from deps.model.cast.v2 import model_pb2 as _model_pb2
from deps.rpc.header import v1_pb2 as _v1_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DailyDemandCastResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.EnergyCast
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.EnergyCast, _Mapping]] = ...) -> None: ...

class DailyReGenerationCastResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.EnergyCast
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.EnergyCast, _Mapping]] = ...) -> None: ...

class TodayGridOperationResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.GridOperation
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.GridOperation, _Mapping]] = ...) -> None: ...

class DailyGridOutputControlCastResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.GridOutputControl
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.GridOutputControl, _Mapping]] = ...) -> None: ...

class HgSystemResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.HgSystemInformation
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.HgSystemInformation, _Mapping]] = ...) -> None: ...

class HgControlResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.HgControlFeedback
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.HgControlFeedback, _Mapping]] = ...) -> None: ...

class HgCommandRequest(_message.Message):
    __slots__ = ("header", "payload")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    header: _v1_pb2.Request
    payload: _containers.RepeatedCompositeFieldContainer[_model_pb2.HgControl]
    def __init__(self, header: _Optional[_Union[_v1_pb2.Request, _Mapping]] = ..., payload: _Optional[_Iterable[_Union[_model_pb2.HgControl, _Mapping]]] = ...) -> None: ...

class HgCommandResponse(_message.Message):
    __slots__ = ("header", "payload")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    header: _v1_pb2.Response
    payload: int
    def __init__(self, header: _Optional[_Union[_v1_pb2.Response, _Mapping]] = ..., payload: _Optional[int] = ...) -> None: ...

class HgMeasureResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.HgMeasure
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.HgMeasure, _Mapping]] = ...) -> None: ...

class WeekilyReGenerationCast(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.EnergyCast
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.EnergyCast, _Mapping]] = ...) -> None: ...

class DailyReGenerationCastPerFuel(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.EnergyCast
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.EnergyCast, _Mapping]] = ...) -> None: ...

class WeeklyDemandCast(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.EnergyCast
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.EnergyCast, _Mapping]] = ...) -> None: ...

class KpxCast(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.KpxCast
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.KpxCast, _Mapping]] = ...) -> None: ...

class KpxSmp(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: KpxSmp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[KpxSmp, _Mapping]] = ...) -> None: ...
