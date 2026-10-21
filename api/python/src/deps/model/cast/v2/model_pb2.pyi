import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CastKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAST_KIND_UNSPECIFIED: _ClassVar[CastKind]
    CAST_KIND_MIDTERM: _ClassVar[CastKind]
    CAST_KIND_LONGTERM: _ClassVar[CastKind]

class TradeCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_CODE_UNSPECIFIED: _ClassVar[TradeCode]
    TRADE_CODE_POWER_MARGET: _ClassVar[TradeCode]

class EnergySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_SOURCE_UNSPECIFIED: _ClassVar[EnergySource]
    ENERGY_SOURCE_PV: _ClassVar[EnergySource]
    ENERGY_SOURCE_WIND: _ClassVar[EnergySource]

class AreaCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AREA_CODE_UNSPECIFIED: _ClassVar[AreaCode]
    AREA_CODE_LAND: _ClassVar[AreaCode]
    AREA_CODE_ISLAND: _ClassVar[AreaCode]

class HgControlKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HG_CONTROL_KIND_UNSPECIFIED: _ClassVar[HgControlKind]
    HG_CONTROL_KIND_NORMAL: _ClassVar[HgControlKind]
    HG_CONTROL_KIND_STOP: _ClassVar[HgControlKind]
    HG_CONTROL_KIND_PLUS_DR: _ClassVar[HgControlKind]
    HG_CONTROL_KIND_REDUCE: _ClassVar[HgControlKind]
CAST_KIND_UNSPECIFIED: CastKind
CAST_KIND_MIDTERM: CastKind
CAST_KIND_LONGTERM: CastKind
TRADE_CODE_UNSPECIFIED: TradeCode
TRADE_CODE_POWER_MARGET: TradeCode
ENERGY_SOURCE_UNSPECIFIED: EnergySource
ENERGY_SOURCE_PV: EnergySource
ENERGY_SOURCE_WIND: EnergySource
AREA_CODE_UNSPECIFIED: AreaCode
AREA_CODE_LAND: AreaCode
AREA_CODE_ISLAND: AreaCode
HG_CONTROL_KIND_UNSPECIFIED: HgControlKind
HG_CONTROL_KIND_NORMAL: HgControlKind
HG_CONTROL_KIND_STOP: HgControlKind
HG_CONTROL_KIND_PLUS_DR: HgControlKind
HG_CONTROL_KIND_REDUCE: HgControlKind

class CastHeader(_message.Message):
    __slots__ = ("stamp_cast", "stamp_point", "du_lead", "kind")
    STAMP_CAST_FIELD_NUMBER: _ClassVar[int]
    STAMP_POINT_FIELD_NUMBER: _ClassVar[int]
    DU_LEAD_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    stamp_cast: _timestamp_pb2.Timestamp
    stamp_point: _timestamp_pb2.Timestamp
    du_lead: _duration_pb2.Duration
    kind: CastKind
    def __init__(self, stamp_cast: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_point: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., du_lead: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., kind: _Optional[_Union[CastKind, str]] = ...) -> None: ...

class KindTag(_message.Message):
    __slots__ = ("trade", "source")
    TRADE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    trade: TradeCode
    source: EnergySource
    def __init__(self, trade: _Optional[_Union[TradeCode, str]] = ..., source: _Optional[_Union[EnergySource, str]] = ...) -> None: ...

class StatisticsWh(_message.Message):
    __slots__ = ("w_cap", "wh_tot", "wh_min", "wh_max")
    W_CAP_FIELD_NUMBER: _ClassVar[int]
    WH_TOT_FIELD_NUMBER: _ClassVar[int]
    WH_MIN_FIELD_NUMBER: _ClassVar[int]
    WH_MAX_FIELD_NUMBER: _ClassVar[int]
    w_cap: int
    wh_tot: float
    wh_min: float
    wh_max: float
    def __init__(self, w_cap: _Optional[int] = ..., wh_tot: _Optional[float] = ..., wh_min: _Optional[float] = ..., wh_max: _Optional[float] = ...) -> None: ...

class StatisticsWhEss(_message.Message):
    __slots__ = ("w_cap", "wh_cha", "wh_discha")
    W_CAP_FIELD_NUMBER: _ClassVar[int]
    WH_CHA_FIELD_NUMBER: _ClassVar[int]
    WH_DISCHA_FIELD_NUMBER: _ClassVar[int]
    w_cap: int
    wh_cha: float
    wh_discha: float
    def __init__(self, w_cap: _Optional[int] = ..., wh_cha: _Optional[float] = ..., wh_discha: _Optional[float] = ...) -> None: ...

class EnergyCast(_message.Message):
    __slots__ = ("header", "tag", "wh", "stats_wh", "wh_ess", "stats_wh_ess")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    WH_FIELD_NUMBER: _ClassVar[int]
    STATS_WH_FIELD_NUMBER: _ClassVar[int]
    WH_ESS_FIELD_NUMBER: _ClassVar[int]
    STATS_WH_ESS_FIELD_NUMBER: _ClassVar[int]
    header: CastHeader
    tag: KindTag
    wh: _containers.RepeatedScalarFieldContainer[float]
    stats_wh: StatisticsWh
    wh_ess: _containers.RepeatedScalarFieldContainer[float]
    stats_wh_ess: StatisticsWhEss
    def __init__(self, header: _Optional[_Union[CastHeader, _Mapping]] = ..., tag: _Optional[_Union[KindTag, _Mapping]] = ..., wh: _Optional[_Iterable[float]] = ..., stats_wh: _Optional[_Union[StatisticsWh, _Mapping]] = ..., wh_ess: _Optional[_Iterable[float]] = ..., stats_wh_ess: _Optional[_Union[StatisticsWhEss, _Mapping]] = ...) -> None: ...

class GridOperation(_message.Message):
    __slots__ = ("stamp", "w_dmnd", "w_pv", "w_wind", "w_tot_re", "w_cap_sup")
    STAMP_FIELD_NUMBER: _ClassVar[int]
    W_DMND_FIELD_NUMBER: _ClassVar[int]
    W_PV_FIELD_NUMBER: _ClassVar[int]
    W_WIND_FIELD_NUMBER: _ClassVar[int]
    W_TOT_RE_FIELD_NUMBER: _ClassVar[int]
    W_CAP_SUP_FIELD_NUMBER: _ClassVar[int]
    stamp: _timestamp_pb2.Timestamp
    w_dmnd: float
    w_pv: float
    w_wind: float
    w_tot_re: float
    w_cap_sup: int
    def __init__(self, stamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., w_dmnd: _Optional[float] = ..., w_pv: _Optional[float] = ..., w_wind: _Optional[float] = ..., w_tot_re: _Optional[float] = ..., w_cap_sup: _Optional[int] = ...) -> None: ...

class GridOutputControl(_message.Message):
    __slots__ = ("header", "w_ctl", "w_min")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    W_CTL_FIELD_NUMBER: _ClassVar[int]
    W_MIN_FIELD_NUMBER: _ClassVar[int]
    header: CastHeader
    w_ctl: float
    w_min: float
    def __init__(self, header: _Optional[_Union[CastHeader, _Mapping]] = ..., w_ctl: _Optional[float] = ..., w_min: _Optional[float] = ...) -> None: ...

class KpxCast(_message.Message):
    __slots__ = ("stamp_trade", "area", "demands")
    STAMP_TRADE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    DEMANDS_FIELD_NUMBER: _ClassVar[int]
    stamp_trade: _timestamp_pb2.Timestamp
    area: AreaCode
    demands: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, stamp_trade: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., area: _Optional[_Union[AreaCode, str]] = ..., demands: _Optional[_Iterable[float]] = ...) -> None: ...

class KpxSmp(_message.Message):
    __slots__ = ("stamp_trade", "area", "smp")
    STAMP_TRADE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    SMP_FIELD_NUMBER: _ClassVar[int]
    stamp_trade: _timestamp_pb2.Timestamp
    area: AreaCode
    smp: float
    def __init__(self, stamp_trade: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., area: _Optional[_Union[AreaCode, str]] = ..., smp: _Optional[float] = ...) -> None: ...

class HgSystemInformation(_message.Message):
    __slots__ = ("id", "stamp_start", "stamp_cursor", "nm3_bg_stored", "kg_hg_stored", "kg_hg_gen_day", "nm3_per_kg", "kwh_per_kg", "kg_per_h_max", "nm3_refill_threshold", "nm3_refill_target", "kg_hg_cap")
    ID_FIELD_NUMBER: _ClassVar[int]
    STAMP_START_FIELD_NUMBER: _ClassVar[int]
    STAMP_CURSOR_FIELD_NUMBER: _ClassVar[int]
    NM3_BG_STORED_FIELD_NUMBER: _ClassVar[int]
    KG_HG_STORED_FIELD_NUMBER: _ClassVar[int]
    KG_HG_GEN_DAY_FIELD_NUMBER: _ClassVar[int]
    NM3_PER_KG_FIELD_NUMBER: _ClassVar[int]
    KWH_PER_KG_FIELD_NUMBER: _ClassVar[int]
    KG_PER_H_MAX_FIELD_NUMBER: _ClassVar[int]
    NM3_REFILL_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NM3_REFILL_TARGET_FIELD_NUMBER: _ClassVar[int]
    KG_HG_CAP_FIELD_NUMBER: _ClassVar[int]
    id: str
    stamp_start: _timestamp_pb2.Timestamp
    stamp_cursor: _timestamp_pb2.Timestamp
    nm3_bg_stored: float
    kg_hg_stored: float
    kg_hg_gen_day: float
    nm3_per_kg: float
    kwh_per_kg: float
    kg_per_h_max: float
    nm3_refill_threshold: float
    nm3_refill_target: float
    kg_hg_cap: float
    def __init__(self, id: _Optional[str] = ..., stamp_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_cursor: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., nm3_bg_stored: _Optional[float] = ..., kg_hg_stored: _Optional[float] = ..., kg_hg_gen_day: _Optional[float] = ..., nm3_per_kg: _Optional[float] = ..., kwh_per_kg: _Optional[float] = ..., kg_per_h_max: _Optional[float] = ..., nm3_refill_threshold: _Optional[float] = ..., nm3_refill_target: _Optional[float] = ..., kg_hg_cap: _Optional[float] = ...) -> None: ...

class HgControl(_message.Message):
    __slots__ = ("id", "kind", "pct", "stamp_eff")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PCT_FIELD_NUMBER: _ClassVar[int]
    STAMP_EFF_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: HgControlKind
    pct: float
    stamp_eff: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[HgControlKind, str]] = ..., pct: _Optional[float] = ..., stamp_eff: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class HgControlFeedback(_message.Message):
    __slots__ = ("control", "seq_cmd", "stamp_req", "stamp_rcv")
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    SEQ_CMD_FIELD_NUMBER: _ClassVar[int]
    STAMP_REQ_FIELD_NUMBER: _ClassVar[int]
    STAMP_RCV_FIELD_NUMBER: _ClassVar[int]
    control: HgControl
    seq_cmd: int
    stamp_req: _timestamp_pb2.Timestamp
    stamp_rcv: _timestamp_pb2.Timestamp
    def __init__(self, control: _Optional[_Union[HgControl, _Mapping]] = ..., seq_cmd: _Optional[int] = ..., stamp_req: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_rcv: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DurationOperation(_message.Message):
    __slots__ = ("dr", "stop", "reduced")
    DR_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    REDUCED_FIELD_NUMBER: _ClassVar[int]
    dr: _duration_pb2.Duration
    stop: _duration_pb2.Duration
    reduced: _duration_pb2.Duration
    def __init__(self, dr: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., stop: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., reduced: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class HgMeasure(_message.Message):
    __slots__ = ("stamp_calc", "stamp_start", "stamp_end", "du", "kg_prod_norm", "kg_prod_dr", "kg_prod_reduced", "kg_prod_tot", "kwh", "nm3_open", "nm3_refilled", "nm3_used", "nm3_stored", "kg_open", "kg_stored", "kg_shipped", "n_shipped", "du_op")
    STAMP_CALC_FIELD_NUMBER: _ClassVar[int]
    STAMP_START_FIELD_NUMBER: _ClassVar[int]
    STAMP_END_FIELD_NUMBER: _ClassVar[int]
    DU_FIELD_NUMBER: _ClassVar[int]
    KG_PROD_NORM_FIELD_NUMBER: _ClassVar[int]
    KG_PROD_DR_FIELD_NUMBER: _ClassVar[int]
    KG_PROD_REDUCED_FIELD_NUMBER: _ClassVar[int]
    KG_PROD_TOT_FIELD_NUMBER: _ClassVar[int]
    KWH_FIELD_NUMBER: _ClassVar[int]
    NM3_OPEN_FIELD_NUMBER: _ClassVar[int]
    NM3_REFILLED_FIELD_NUMBER: _ClassVar[int]
    NM3_USED_FIELD_NUMBER: _ClassVar[int]
    NM3_STORED_FIELD_NUMBER: _ClassVar[int]
    KG_OPEN_FIELD_NUMBER: _ClassVar[int]
    KG_STORED_FIELD_NUMBER: _ClassVar[int]
    KG_SHIPPED_FIELD_NUMBER: _ClassVar[int]
    N_SHIPPED_FIELD_NUMBER: _ClassVar[int]
    DU_OP_FIELD_NUMBER: _ClassVar[int]
    stamp_calc: _timestamp_pb2.Timestamp
    stamp_start: _timestamp_pb2.Timestamp
    stamp_end: _timestamp_pb2.Timestamp
    du: _duration_pb2.Duration
    kg_prod_norm: float
    kg_prod_dr: float
    kg_prod_reduced: float
    kg_prod_tot: float
    kwh: float
    nm3_open: float
    nm3_refilled: float
    nm3_used: float
    nm3_stored: float
    kg_open: float
    kg_stored: float
    kg_shipped: float
    n_shipped: int
    du_op: DurationOperation
    def __init__(self, stamp_calc: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., du: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., kg_prod_norm: _Optional[float] = ..., kg_prod_dr: _Optional[float] = ..., kg_prod_reduced: _Optional[float] = ..., kg_prod_tot: _Optional[float] = ..., kwh: _Optional[float] = ..., nm3_open: _Optional[float] = ..., nm3_refilled: _Optional[float] = ..., nm3_used: _Optional[float] = ..., nm3_stored: _Optional[float] = ..., kg_open: _Optional[float] = ..., kg_stored: _Optional[float] = ..., kg_shipped: _Optional[float] = ..., n_shipped: _Optional[int] = ..., du_op: _Optional[_Union[DurationOperation, _Mapping]] = ...) -> None: ...
