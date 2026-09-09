from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Heating(_message.Message):
    __slots__ = ("st", "status", "fault", "warning")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_UNSPECIFIED: _ClassVar[Heating.St]
    ST_UNSPECIFIED: Heating.St
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
    st: Heating.St
    status: Heating.Status
    fault: Heating.Fault
    warning: Heating.Warning
    def __init__(self, st: _Optional[_Union[Heating.St, str]] = ..., status: _Optional[_Union[Heating.Status, _Mapping]] = ..., fault: _Optional[_Union[Heating.Fault, _Mapping]] = ..., warning: _Optional[_Union[Heating.Warning, _Mapping]] = ...) -> None: ...

class Ventilation(_message.Message):
    __slots__ = ("st", "status", "fault", "warning")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_UNSPECIFIED: _ClassVar[Ventilation.St]
    ST_UNSPECIFIED: Ventilation.St
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
    st: Ventilation.St
    status: Ventilation.Status
    fault: Ventilation.Fault
    warning: Ventilation.Warning
    def __init__(self, st: _Optional[_Union[Ventilation.St, str]] = ..., status: _Optional[_Union[Ventilation.Status, _Mapping]] = ..., fault: _Optional[_Union[Ventilation.Fault, _Mapping]] = ..., warning: _Optional[_Union[Ventilation.Warning, _Mapping]] = ...) -> None: ...

class AirConditioning(_message.Message):
    __slots__ = ("st", "status", "fault", "warning", "tmp", "rh", "tmp_ex", "tmp_set", "rh_set", "w_import")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_UNSPECIFIED: _ClassVar[AirConditioning.St]
        ST_STOP: _ClassVar[AirConditioning.St]
        ST_OPERATION: _ClassVar[AirConditioning.St]
    ST_UNSPECIFIED: AirConditioning.St
    ST_STOP: AirConditioning.St
    ST_OPERATION: AirConditioning.St
    class Status(_message.Message):
        __slots__ = ("other", "cool", "heat", "dry", "fan", "auto")
        OTHER_FIELD_NUMBER: _ClassVar[int]
        COOL_FIELD_NUMBER: _ClassVar[int]
        HEAT_FIELD_NUMBER: _ClassVar[int]
        DRY_FIELD_NUMBER: _ClassVar[int]
        FAN_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        other: bool
        cool: bool
        heat: bool
        dry: bool
        fan: bool
        auto: bool
        def __init__(self, other: _Optional[bool] = ..., cool: _Optional[bool] = ..., heat: _Optional[bool] = ..., dry: _Optional[bool] = ..., fan: _Optional[bool] = ..., auto: _Optional[bool] = ...) -> None: ...
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
    TMP_FIELD_NUMBER: _ClassVar[int]
    RH_FIELD_NUMBER: _ClassVar[int]
    TMP_EX_FIELD_NUMBER: _ClassVar[int]
    TMP_SET_FIELD_NUMBER: _ClassVar[int]
    RH_SET_FIELD_NUMBER: _ClassVar[int]
    W_IMPORT_FIELD_NUMBER: _ClassVar[int]
    st: AirConditioning.St
    status: AirConditioning.Status
    fault: AirConditioning.Fault
    warning: AirConditioning.Warning
    tmp: float
    rh: float
    tmp_ex: float
    tmp_set: float
    rh_set: float
    w_import: float
    def __init__(self, st: _Optional[_Union[AirConditioning.St, str]] = ..., status: _Optional[_Union[AirConditioning.Status, _Mapping]] = ..., fault: _Optional[_Union[AirConditioning.Fault, _Mapping]] = ..., warning: _Optional[_Union[AirConditioning.Warning, _Mapping]] = ..., tmp: _Optional[float] = ..., rh: _Optional[float] = ..., tmp_ex: _Optional[float] = ..., tmp_set: _Optional[float] = ..., rh_set: _Optional[float] = ..., w_import: _Optional[float] = ...) -> None: ...

class Hvac(_message.Message):
    __slots__ = ("heating", "ventilation", "air_conditioning")
    HEATING_FIELD_NUMBER: _ClassVar[int]
    VENTILATION_FIELD_NUMBER: _ClassVar[int]
    AIR_CONDITIONING_FIELD_NUMBER: _ClassVar[int]
    heating: Heating
    ventilation: Ventilation
    air_conditioning: AirConditioning
    def __init__(self, heating: _Optional[_Union[Heating, _Mapping]] = ..., ventilation: _Optional[_Union[Ventilation, _Mapping]] = ..., air_conditioning: _Optional[_Union[AirConditioning, _Mapping]] = ...) -> None: ...
