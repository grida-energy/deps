import datetime

from deps.model.hvac.v1 import model_pb2 as _model_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MeasureResponse(_message.Message):
    __slots__ = ("timestamp", "payload")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    payload: _model_pb2.Hvac
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[_Union[_model_pb2.Hvac, _Mapping]] = ...) -> None: ...
