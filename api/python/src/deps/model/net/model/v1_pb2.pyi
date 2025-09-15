from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AcLine(_message.Message):
    __slots__ = ("v", "a", "hz", "w", "va", "var", "pf")
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    v: float
    a: float
    hz: float
    w: float
    va: float
    var: float
    pf: float
    def __init__(self, v: _Optional[float] = ..., a: _Optional[float] = ..., hz: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ...) -> None: ...

class AcLineSum(_message.Message):
    __slots__ = ("a", "hz", "w", "va", "var", "pf")
    A_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    a: float
    hz: float
    w: float
    va: float
    var: float
    pf: float
    def __init__(self, a: _Optional[float] = ..., hz: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ...) -> None: ...

class Energy(_message.Message):
    __slots__ = ("exported", "imported")
    EXPORTED_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FIELD_NUMBER: _ClassVar[int]
    exported: float
    imported: float
    def __init__(self, exported: _Optional[float] = ..., imported: _Optional[float] = ...) -> None: ...
