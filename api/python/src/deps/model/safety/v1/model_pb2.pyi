from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImdMeasurement(_message.Message):
    __slots__ = ("kohm_ir",)
    KOHM_IR_FIELD_NUMBER: _ClassVar[int]
    kohm_ir: float
    def __init__(self, kohm_ir: _Optional[float] = ...) -> None: ...

class Safety(_message.Message):
    __slots__ = ("st", "status", "fault", "warning", "imd")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_UNSPECIFIED: _ClassVar[Safety.St]
    ST_UNSPECIFIED: Safety.St
    class Status(_message.Message):
        __slots__ = ("other",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        other: bool
        def __init__(self, other: _Optional[bool] = ...) -> None: ...
    class Fault(_message.Message):
        __slots__ = ("other",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        other: bool
        def __init__(self, other: _Optional[bool] = ...) -> None: ...
    class Warning(_message.Message):
        __slots__ = ("other",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        other: bool
        def __init__(self, other: _Optional[bool] = ...) -> None: ...
    ST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    IMD_FIELD_NUMBER: _ClassVar[int]
    st: Safety.St
    status: Safety.Status
    fault: Safety.Fault
    warning: Safety.Warning
    imd: ImdMeasurement
    def __init__(self, st: _Optional[_Union[Safety.St, str]] = ..., status: _Optional[_Union[Safety.Status, _Mapping]] = ..., fault: _Optional[_Union[Safety.Fault, _Mapping]] = ..., warning: _Optional[_Union[Safety.Warning, _Mapping]] = ..., imd: _Optional[_Union[ImdMeasurement, _Mapping]] = ...) -> None: ...
