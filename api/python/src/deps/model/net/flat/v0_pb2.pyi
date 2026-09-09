from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FlatMeterSinglePhase(_message.Message):
    __slots__ = ("a", "v", "w", "va", "var", "pf", "hz", "tot_wh_imp", "tot_wh_exp")
    A_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    TOT_WH_IMP_FIELD_NUMBER: _ClassVar[int]
    TOT_WH_EXP_FIELD_NUMBER: _ClassVar[int]
    a: float
    v: float
    w: float
    va: float
    var: float
    pf: float
    hz: float
    tot_wh_imp: float
    tot_wh_exp: float
    def __init__(self, a: _Optional[float] = ..., v: _Optional[float] = ..., w: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., hz: _Optional[float] = ..., tot_wh_imp: _Optional[float] = ..., tot_wh_exp: _Optional[float] = ...) -> None: ...
