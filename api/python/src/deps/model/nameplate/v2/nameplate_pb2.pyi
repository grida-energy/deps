from deps.vnd.alarm import v1_pb2 as _v1_pb2
from deps.vnd.parameter import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Wknt(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WKNT_UNSPECIFIED: _ClassVar[Wknt]
    WKNT_BESS_V1: _ClassVar[Wknt]
    WKNT_UPMS_V1: _ClassVar[Wknt]
    WKNT_DBSERVER_V1: _ClassVar[Wknt]
    WKNT_ESD_BANK_V1: _ClassVar[Wknt]
    WKNT_PCS_PH3_PCS_V1: _ClassVar[Wknt]
    WKNT_NET_METER_PH3_V1: _ClassVar[Wknt]
    WKNT_RMS_V1: _ClassVar[Wknt]
WKNT_UNSPECIFIED: Wknt
WKNT_BESS_V1: Wknt
WKNT_UPMS_V1: Wknt
WKNT_DBSERVER_V1: Wknt
WKNT_ESD_BANK_V1: Wknt
WKNT_PCS_PH3_PCS_V1: Wknt
WKNT_NET_METER_PH3_V1: Wknt
WKNT_RMS_V1: Wknt

class Quadrant(_message.Message):
    __slots__ = ("q1", "q2", "q3", "q4")
    Q1_FIELD_NUMBER: _ClassVar[int]
    Q2_FIELD_NUMBER: _ClassVar[int]
    Q3_FIELD_NUMBER: _ClassVar[int]
    Q4_FIELD_NUMBER: _ClassVar[int]
    q1: float
    q2: float
    q3: float
    q4: float
    def __init__(self, q1: _Optional[float] = ..., q2: _Optional[float] = ..., q3: _Optional[float] = ..., q4: _Optional[float] = ...) -> None: ...

class NameplateFilter(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Nameplate(_message.Message):
    __slots__ = ("alarm_meta", "param_meta", "wknt", "ratings")
    ALARM_META_FIELD_NUMBER: _ClassVar[int]
    PARAM_META_FIELD_NUMBER: _ClassVar[int]
    WKNT_FIELD_NUMBER: _ClassVar[int]
    RATINGS_FIELD_NUMBER: _ClassVar[int]
    alarm_meta: _v1_pb2.AlarmMeta
    param_meta: _v1_pb2_1.ParamMeta
    wknt: Wknt
    ratings: EndPointRatings
    def __init__(self, alarm_meta: _Optional[_Union[_v1_pb2.AlarmMeta, _Mapping]] = ..., param_meta: _Optional[_Union[_v1_pb2_1.ParamMeta, _Mapping]] = ..., wknt: _Optional[_Union[Wknt, str]] = ..., ratings: _Optional[_Union[EndPointRatings, _Mapping]] = ...) -> None: ...

class DeviceRatings(_message.Message):
    __slots__ = ("storage", "pcs")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    PCS_FIELD_NUMBER: _ClassVar[int]
    storage: StorageRatings
    pcs: PcsRatings
    def __init__(self, storage: _Optional[_Union[StorageRatings, _Mapping]] = ..., pcs: _Optional[_Union[PcsRatings, _Mapping]] = ...) -> None: ...

class EndPointRatings(_message.Message):
    __slots__ = ("total", "storage_devices", "pcs_devices")
    class StorageDevicesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StorageRatings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StorageRatings, _Mapping]] = ...) -> None: ...
    class PcsDevicesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PcsRatings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PcsRatings, _Mapping]] = ...) -> None: ...
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    PCS_DEVICES_FIELD_NUMBER: _ClassVar[int]
    total: DeviceRatings
    storage_devices: _containers.MessageMap[str, StorageRatings]
    pcs_devices: _containers.MessageMap[str, PcsRatings]
    def __init__(self, total: _Optional[_Union[DeviceRatings, _Mapping]] = ..., storage_devices: _Optional[_Mapping[str, StorageRatings]] = ..., pcs_devices: _Optional[_Mapping[str, PcsRatings]] = ...) -> None: ...

class StorageRatings(_message.Message):
    __slots__ = ("wh", "ahr")
    WH_FIELD_NUMBER: _ClassVar[int]
    AHR_FIELD_NUMBER: _ClassVar[int]
    wh: float
    ahr: float
    def __init__(self, wh: _Optional[float] = ..., ahr: _Optional[float] = ...) -> None: ...

class PcsRatings(_message.Message):
    __slots__ = ("w", "va", "var", "a", "pf")
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    w: float
    va: float
    var: Quadrant
    a: float
    pf: Quadrant
    def __init__(self, w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[_Union[Quadrant, _Mapping]] = ..., a: _Optional[float] = ..., pf: _Optional[_Union[Quadrant, _Mapping]] = ...) -> None: ...
