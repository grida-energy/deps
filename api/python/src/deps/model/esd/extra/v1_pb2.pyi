from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChaLimit(_message.Message):
    __slots__ = ("soc_max", "soc_min")
    SOC_MAX_FIELD_NUMBER: _ClassVar[int]
    SOC_MIN_FIELD_NUMBER: _ClassVar[int]
    soc_max: float
    soc_min: float
    def __init__(self, soc_max: _Optional[float] = ..., soc_min: _Optional[float] = ...) -> None: ...

class Conn(_message.Message):
    __slots__ = ("conn",)
    class Conn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISCONNECT: _ClassVar[Conn.Conn]
        CONNECT: _ClassVar[Conn.Conn]
    DISCONNECT: Conn.Conn
    CONNECT: Conn.Conn
    CONN_FIELD_NUMBER: _ClassVar[int]
    conn: Conn.Conn
    def __init__(self, conn: _Optional[_Union[Conn.Conn, str]] = ...) -> None: ...
