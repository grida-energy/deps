from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Id(_message.Message):
    __slots__ = ("vendor", "model", "serial", "sw_version", "hw_version")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SW_VERSION_FIELD_NUMBER: _ClassVar[int]
    HW_VERSION_FIELD_NUMBER: _ClassVar[int]
    vendor: str
    model: str
    serial: str
    sw_version: str
    hw_version: str
    def __init__(self, vendor: _Optional[str] = ..., model: _Optional[str] = ..., serial: _Optional[str] = ..., sw_version: _Optional[str] = ..., hw_version: _Optional[str] = ...) -> None: ...

class NetworkConfig(_message.Message):
    __slots__ = ("ips",)
    class IpsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    IPS_FIELD_NUMBER: _ClassVar[int]
    ips: _containers.ScalarMap[str, str]
    def __init__(self, ips: _Optional[_Mapping[str, str]] = ...) -> None: ...
