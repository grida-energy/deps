from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Line(_message.Message):
    __slots__ = ("v", "a", "w", "wh")
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    v: float
    a: float
    w: float
    wh: Energy
    def __init__(self, v: _Optional[float] = ..., a: _Optional[float] = ..., w: _Optional[float] = ..., wh: _Optional[_Union[Energy, _Mapping]] = ...) -> None: ...

class AcLine(_message.Message):
    __slots__ = ("v", "a", "hz", "w", "va", "var", "pf", "wh")
    V_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    v: float
    a: float
    hz: float
    w: float
    va: float
    var: float
    pf: float
    wh: Energy
    def __init__(self, v: _Optional[float] = ..., a: _Optional[float] = ..., hz: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., wh: _Optional[_Union[Energy, _Mapping]] = ...) -> None: ...

class AcLineSum(_message.Message):
    __slots__ = ("a", "hz", "w", "va", "var", "pf", "wh")
    A_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    a: float
    hz: float
    w: float
    va: float
    var: float
    pf: float
    wh: Energy
    def __init__(self, a: _Optional[float] = ..., hz: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., wh: _Optional[_Union[Energy, _Mapping]] = ...) -> None: ...

class Energy(_message.Message):
    __slots__ = ("exported", "imported")
    EXPORTED_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FIELD_NUMBER: _ClassVar[int]
    exported: float
    imported: float
    def __init__(self, exported: _Optional[float] = ..., imported: _Optional[float] = ...) -> None: ...
