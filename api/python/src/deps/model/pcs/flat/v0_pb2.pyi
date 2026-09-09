from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlatConn(_message.Message):
    __slots__ = ("conn_win_tms", "conn_rvrt_tms", "conn")
    CONN_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    CONN_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    CONN_FIELD_NUMBER: _ClassVar[int]
    conn_win_tms: float
    conn_rvrt_tms: float
    conn: ImmediatePcsControl.Conn
    def __init__(self, conn_win_tms: _Optional[float] = ..., conn_rvrt_tms: _Optional[float] = ..., conn: _Optional[_Union[ImmediatePcsControl.Conn, str]] = ...) -> None: ...

class FlatWMaxLimPct(_message.Message):
    __slots__ = ("w_max_lim_pct", "w_max_lim_pct_win_tms", "w_max_lim_pct_rvrt_tms", "w_max_lim_pct_rmp_tms", "w_max_lim_ena")
    W_MAX_LIM_PCT_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_ENA_FIELD_NUMBER: _ClassVar[int]
    w_max_lim_pct: float
    w_max_lim_pct_win_tms: float
    w_max_lim_pct_rvrt_tms: float
    w_max_lim_pct_rmp_tms: float
    w_max_lim_ena: ImmediatePcsControl.Ena
    def __init__(self, w_max_lim_pct: _Optional[float] = ..., w_max_lim_pct_win_tms: _Optional[float] = ..., w_max_lim_pct_rvrt_tms: _Optional[float] = ..., w_max_lim_pct_rmp_tms: _Optional[float] = ..., w_max_lim_ena: _Optional[_Union[ImmediatePcsControl.Ena, str]] = ...) -> None: ...

class FlatOutPfSet(_message.Message):
    __slots__ = ("out_pf_set", "out_pf_set_win_tms", "out_pf_set_rvrt_tms", "out_pf_set_rmp_tms", "out_pf_set_ena")
    OUT_PF_SET_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_ENA_FIELD_NUMBER: _ClassVar[int]
    out_pf_set: float
    out_pf_set_win_tms: float
    out_pf_set_rvrt_tms: float
    out_pf_set_rmp_tms: float
    out_pf_set_ena: ImmediatePcsControl.Ena
    def __init__(self, out_pf_set: _Optional[float] = ..., out_pf_set_win_tms: _Optional[float] = ..., out_pf_set_rvrt_tms: _Optional[float] = ..., out_pf_set_rmp_tms: _Optional[float] = ..., out_pf_set_ena: _Optional[_Union[ImmediatePcsControl.Ena, str]] = ...) -> None: ...

class FlatVarWMaxPct(_message.Message):
    __slots__ = ("var_w_max_pct", "var_max_pct", "var_aval_pct", "var_pct_win_tms", "var_pct_rvrt_tms", "var_pct_rmp_tms", "var_pct_mod", "var_pct_ena")
    VAR_W_MAX_PCT_FIELD_NUMBER: _ClassVar[int]
    VAR_MAX_PCT_FIELD_NUMBER: _ClassVar[int]
    VAR_AVAL_PCT_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_MOD_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_ENA_FIELD_NUMBER: _ClassVar[int]
    var_w_max_pct: float
    var_max_pct: float
    var_aval_pct: float
    var_pct_win_tms: float
    var_pct_rvrt_tms: float
    var_pct_rmp_tms: float
    var_pct_mod: ImmediatePcsControl.VArPctMod
    var_pct_ena: ImmediatePcsControl.Ena
    def __init__(self, var_w_max_pct: _Optional[float] = ..., var_max_pct: _Optional[float] = ..., var_aval_pct: _Optional[float] = ..., var_pct_win_tms: _Optional[float] = ..., var_pct_rvrt_tms: _Optional[float] = ..., var_pct_rmp_tms: _Optional[float] = ..., var_pct_mod: _Optional[_Union[ImmediatePcsControl.VArPctMod, str]] = ..., var_pct_ena: _Optional[_Union[ImmediatePcsControl.Ena, str]] = ...) -> None: ...

class FlatCommands(_message.Message):
    __slots__ = ("conn", "w_max_lim_pct", "out_pf_set", "var_w_max_pct")
    CONN_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_FIELD_NUMBER: _ClassVar[int]
    VAR_W_MAX_PCT_FIELD_NUMBER: _ClassVar[int]
    conn: FlatConn
    w_max_lim_pct: FlatWMaxLimPct
    out_pf_set: FlatOutPfSet
    var_w_max_pct: FlatVarWMaxPct
    def __init__(self, conn: _Optional[_Union[FlatConn, _Mapping]] = ..., w_max_lim_pct: _Optional[_Union[FlatWMaxLimPct, _Mapping]] = ..., out_pf_set: _Optional[_Union[FlatOutPfSet, _Mapping]] = ..., var_w_max_pct: _Optional[_Union[FlatVarWMaxPct, _Mapping]] = ...) -> None: ...

class ImmediatePcsControl(_message.Message):
    __slots__ = ("conn_win_tms", "conn_rvrt_tms", "conn", "w_max_lim_pct", "w_max_lim_pct_win_tms", "w_max_lim_pct_rvrt_tms", "w_max_lim_pct_rmp_tms", "w_max_lim_ena", "out_pf_set", "out_pf_set_win_tms", "out_pf_set_rvrt_tms", "out_pf_set_rmp_tms", "out_pf_set_ena", "var_w_max_pct", "var_max_pct", "var_aval_pct", "var_pct_win_tms", "var_pct_rvrt_tms", "var_pct_rmp_tms", "var_pct_mod", "var_pct_ena")
    class Conn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISCONNECT: _ClassVar[ImmediatePcsControl.Conn]
        CONNECT: _ClassVar[ImmediatePcsControl.Conn]
    DISCONNECT: ImmediatePcsControl.Conn
    CONNECT: ImmediatePcsControl.Conn
    class Ena(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISABLED: _ClassVar[ImmediatePcsControl.Ena]
        ENABLED: _ClassVar[ImmediatePcsControl.Ena]
    DISABLED: ImmediatePcsControl.Ena
    ENABLED: ImmediatePcsControl.Ena
    class VArPctMod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ImmediatePcsControl.VArPctMod]
        W_MAX: _ClassVar[ImmediatePcsControl.VArPctMod]
        VAR_MAX: _ClassVar[ImmediatePcsControl.VArPctMod]
        VAR_AVAL: _ClassVar[ImmediatePcsControl.VArPctMod]
    NONE: ImmediatePcsControl.VArPctMod
    W_MAX: ImmediatePcsControl.VArPctMod
    VAR_MAX: ImmediatePcsControl.VArPctMod
    VAR_AVAL: ImmediatePcsControl.VArPctMod
    CONN_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    CONN_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    CONN_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_PCT_RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_LIM_ENA_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    OUT_PF_SET_ENA_FIELD_NUMBER: _ClassVar[int]
    VAR_W_MAX_PCT_FIELD_NUMBER: _ClassVar[int]
    VAR_MAX_PCT_FIELD_NUMBER: _ClassVar[int]
    VAR_AVAL_PCT_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_RVRT_TMS_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_MOD_FIELD_NUMBER: _ClassVar[int]
    VAR_PCT_ENA_FIELD_NUMBER: _ClassVar[int]
    conn_win_tms: float
    conn_rvrt_tms: float
    conn: ImmediatePcsControl.Conn
    w_max_lim_pct: float
    w_max_lim_pct_win_tms: float
    w_max_lim_pct_rvrt_tms: float
    w_max_lim_pct_rmp_tms: float
    w_max_lim_ena: ImmediatePcsControl.Ena
    out_pf_set: float
    out_pf_set_win_tms: float
    out_pf_set_rvrt_tms: float
    out_pf_set_rmp_tms: float
    out_pf_set_ena: ImmediatePcsControl.Ena
    var_w_max_pct: float
    var_max_pct: float
    var_aval_pct: float
    var_pct_win_tms: float
    var_pct_rvrt_tms: float
    var_pct_rmp_tms: float
    var_pct_mod: ImmediatePcsControl.VArPctMod
    var_pct_ena: ImmediatePcsControl.Ena
    def __init__(self, conn_win_tms: _Optional[float] = ..., conn_rvrt_tms: _Optional[float] = ..., conn: _Optional[_Union[ImmediatePcsControl.Conn, str]] = ..., w_max_lim_pct: _Optional[float] = ..., w_max_lim_pct_win_tms: _Optional[float] = ..., w_max_lim_pct_rvrt_tms: _Optional[float] = ..., w_max_lim_pct_rmp_tms: _Optional[float] = ..., w_max_lim_ena: _Optional[_Union[ImmediatePcsControl.Ena, str]] = ..., out_pf_set: _Optional[float] = ..., out_pf_set_win_tms: _Optional[float] = ..., out_pf_set_rvrt_tms: _Optional[float] = ..., out_pf_set_rmp_tms: _Optional[float] = ..., out_pf_set_ena: _Optional[_Union[ImmediatePcsControl.Ena, str]] = ..., var_w_max_pct: _Optional[float] = ..., var_max_pct: _Optional[float] = ..., var_aval_pct: _Optional[float] = ..., var_pct_win_tms: _Optional[float] = ..., var_pct_rvrt_tms: _Optional[float] = ..., var_pct_rmp_tms: _Optional[float] = ..., var_pct_mod: _Optional[_Union[ImmediatePcsControl.VArPctMod, str]] = ..., var_pct_ena: _Optional[_Union[ImmediatePcsControl.Ena, str]] = ...) -> None: ...

class PcsThreePhase(_message.Message):
    __slots__ = ("a", "a_ph_a", "a_ph_b", "a_ph_c", "pp_v_ph_ab", "pp_v_ph_bc", "pp_v_ph_ca", "ph_v_ph_a", "ph_v_ph_b", "ph_v_ph_c", "w", "hz", "va", "var", "pf", "wh", "dca", "dcv", "dcw", "tmp_cab", "tmp_snk", "tmp_trns", "tmp_ot", "st", "st_vnd", "evt1", "evt2", "evt_vnd1", "evt_vnd2", "evt_vnd3", "evt_vnd4")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NA_ST: _ClassVar[PcsThreePhase.St]
        OFF: _ClassVar[PcsThreePhase.St]
        SLEEPING: _ClassVar[PcsThreePhase.St]
        STARTING: _ClassVar[PcsThreePhase.St]
        MPPT: _ClassVar[PcsThreePhase.St]
        THROTTLED: _ClassVar[PcsThreePhase.St]
        SHUTTING_DOWN: _ClassVar[PcsThreePhase.St]
        FAULT: _ClassVar[PcsThreePhase.St]
        STANDBY: _ClassVar[PcsThreePhase.St]
    NA_ST: PcsThreePhase.St
    OFF: PcsThreePhase.St
    SLEEPING: PcsThreePhase.St
    STARTING: PcsThreePhase.St
    MPPT: PcsThreePhase.St
    THROTTLED: PcsThreePhase.St
    SHUTTING_DOWN: PcsThreePhase.St
    FAULT: PcsThreePhase.St
    STANDBY: PcsThreePhase.St
    class Evt1(_message.Message):
        __slots__ = ("GROUND_FAULT", "DC_OVER_VOLT", "AC_DISCONNECT", "DC_DISCONNECT", "GRID_DISCONNECT", "CABINET_OPEN", "MANUAL_SHUTDOWN", "OVER_TEMP", "OVER_FREQUENCY", "UNDER_FREQUENCY", "AC_OVER_VOLT", "AC_UNDER_VOLT", "BLOWN_STRING_FUSE", "UNDER_TEMP", "MEMORY_LOSS", "HW_TEST_FAILURE")
        GROUND_FAULT_FIELD_NUMBER: _ClassVar[int]
        DC_OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        AC_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
        DC_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
        GRID_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
        CABINET_OPEN_FIELD_NUMBER: _ClassVar[int]
        MANUAL_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        OVER_TEMP_FIELD_NUMBER: _ClassVar[int]
        OVER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        UNDER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        AC_OVER_VOLT_FIELD_NUMBER: _ClassVar[int]
        AC_UNDER_VOLT_FIELD_NUMBER: _ClassVar[int]
        BLOWN_STRING_FUSE_FIELD_NUMBER: _ClassVar[int]
        UNDER_TEMP_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LOSS_FIELD_NUMBER: _ClassVar[int]
        HW_TEST_FAILURE_FIELD_NUMBER: _ClassVar[int]
        GROUND_FAULT: bool
        DC_OVER_VOLT: bool
        AC_DISCONNECT: bool
        DC_DISCONNECT: bool
        GRID_DISCONNECT: bool
        CABINET_OPEN: bool
        MANUAL_SHUTDOWN: bool
        OVER_TEMP: bool
        OVER_FREQUENCY: bool
        UNDER_FREQUENCY: bool
        AC_OVER_VOLT: bool
        AC_UNDER_VOLT: bool
        BLOWN_STRING_FUSE: bool
        UNDER_TEMP: bool
        MEMORY_LOSS: bool
        HW_TEST_FAILURE: bool
        def __init__(self, GROUND_FAULT: _Optional[bool] = ..., DC_OVER_VOLT: _Optional[bool] = ..., AC_DISCONNECT: _Optional[bool] = ..., DC_DISCONNECT: _Optional[bool] = ..., GRID_DISCONNECT: _Optional[bool] = ..., CABINET_OPEN: _Optional[bool] = ..., MANUAL_SHUTDOWN: _Optional[bool] = ..., OVER_TEMP: _Optional[bool] = ..., OVER_FREQUENCY: _Optional[bool] = ..., UNDER_FREQUENCY: _Optional[bool] = ..., AC_OVER_VOLT: _Optional[bool] = ..., AC_UNDER_VOLT: _Optional[bool] = ..., BLOWN_STRING_FUSE: _Optional[bool] = ..., UNDER_TEMP: _Optional[bool] = ..., MEMORY_LOSS: _Optional[bool] = ..., HW_TEST_FAILURE: _Optional[bool] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    A_PH_A_FIELD_NUMBER: _ClassVar[int]
    A_PH_B_FIELD_NUMBER: _ClassVar[int]
    A_PH_C_FIELD_NUMBER: _ClassVar[int]
    PP_V_PH_AB_FIELD_NUMBER: _ClassVar[int]
    PP_V_PH_BC_FIELD_NUMBER: _ClassVar[int]
    PP_V_PH_CA_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_A_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_B_FIELD_NUMBER: _ClassVar[int]
    PH_V_PH_C_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    HZ_FIELD_NUMBER: _ClassVar[int]
    VA_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    PF_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    DCA_FIELD_NUMBER: _ClassVar[int]
    DCV_FIELD_NUMBER: _ClassVar[int]
    DCW_FIELD_NUMBER: _ClassVar[int]
    TMP_CAB_FIELD_NUMBER: _ClassVar[int]
    TMP_SNK_FIELD_NUMBER: _ClassVar[int]
    TMP_TRNS_FIELD_NUMBER: _ClassVar[int]
    TMP_OT_FIELD_NUMBER: _ClassVar[int]
    ST_FIELD_NUMBER: _ClassVar[int]
    ST_VND_FIELD_NUMBER: _ClassVar[int]
    EVT1_FIELD_NUMBER: _ClassVar[int]
    EVT2_FIELD_NUMBER: _ClassVar[int]
    EVT_VND1_FIELD_NUMBER: _ClassVar[int]
    EVT_VND2_FIELD_NUMBER: _ClassVar[int]
    EVT_VND3_FIELD_NUMBER: _ClassVar[int]
    EVT_VND4_FIELD_NUMBER: _ClassVar[int]
    a: float
    a_ph_a: float
    a_ph_b: float
    a_ph_c: float
    pp_v_ph_ab: float
    pp_v_ph_bc: float
    pp_v_ph_ca: float
    ph_v_ph_a: float
    ph_v_ph_b: float
    ph_v_ph_c: float
    w: float
    hz: float
    va: float
    var: float
    pf: float
    wh: float
    dca: float
    dcv: float
    dcw: float
    tmp_cab: float
    tmp_snk: float
    tmp_trns: float
    tmp_ot: float
    st: PcsThreePhase.St
    st_vnd: int
    evt1: PcsThreePhase.Evt1
    evt2: int
    evt_vnd1: int
    evt_vnd2: int
    evt_vnd3: int
    evt_vnd4: int
    def __init__(self, a: _Optional[float] = ..., a_ph_a: _Optional[float] = ..., a_ph_b: _Optional[float] = ..., a_ph_c: _Optional[float] = ..., pp_v_ph_ab: _Optional[float] = ..., pp_v_ph_bc: _Optional[float] = ..., pp_v_ph_ca: _Optional[float] = ..., ph_v_ph_a: _Optional[float] = ..., ph_v_ph_b: _Optional[float] = ..., ph_v_ph_c: _Optional[float] = ..., w: _Optional[float] = ..., hz: _Optional[float] = ..., va: _Optional[float] = ..., var: _Optional[float] = ..., pf: _Optional[float] = ..., wh: _Optional[float] = ..., dca: _Optional[float] = ..., dcv: _Optional[float] = ..., dcw: _Optional[float] = ..., tmp_cab: _Optional[float] = ..., tmp_snk: _Optional[float] = ..., tmp_trns: _Optional[float] = ..., tmp_ot: _Optional[float] = ..., st: _Optional[_Union[PcsThreePhase.St, str]] = ..., st_vnd: _Optional[int] = ..., evt1: _Optional[_Union[PcsThreePhase.Evt1, _Mapping]] = ..., evt2: _Optional[int] = ..., evt_vnd1: _Optional[int] = ..., evt_vnd2: _Optional[int] = ..., evt_vnd3: _Optional[int] = ..., evt_vnd4: _Optional[int] = ...) -> None: ...
