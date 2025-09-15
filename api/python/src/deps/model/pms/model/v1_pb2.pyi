import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookupInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOKUP_INPUT_TYPE_NA: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_TIME_SEC: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_TIME_MIN: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_TIME_HOUR: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_TIME_SEC_SINCE_SEQUENCE: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_TIME_SEC_SINCE_CHAIN: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_SOC: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_SOC_PU: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_TMP: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_PRICE: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_W_SRC: _ClassVar[LookupInputType]
    LOOKUP_INPUT_TYPE_W_CUT: _ClassVar[LookupInputType]

class LookupOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOKUP_OUTPUT_TYPE_NA: _ClassVar[LookupOutputType]
    LOOKUP_OUTPUT_TYPE_W_CMD: _ClassVar[LookupOutputType]
    LOOKUP_OUTPUT_TYPE_W_ABS: _ClassVar[LookupOutputType]
    LOOKUP_OUTPUT_TYPE_W_MAX_POS: _ClassVar[LookupOutputType]
    LOOKUP_OUTPUT_TYPE_W_MAX_NEG: _ClassVar[LookupOutputType]
    LOOKUP_OUTPUT_TYPE_VA_CMD: _ClassVar[LookupOutputType]

class OutputBlendMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_BLEND_MODE_OVERRIDE: _ClassVar[OutputBlendMode]
    OUTPUT_BLEND_MODE_CLAMP_ZERO: _ClassVar[OutputBlendMode]
    OUTPUT_BLEND_MODE_ADDITION: _ClassVar[OutputBlendMode]
    OUTPUT_BLEND_MODE_SUBTRACT: _ClassVar[OutputBlendMode]
    OUTPUT_BLEND_MODE_MULTIPLY: _ClassVar[OutputBlendMode]
    OUTPUT_BLEND_MODE_MUL_MASK_ZPOS: _ClassVar[OutputBlendMode]
    OUTPUT_BLEND_MODE_OVERRIDE_SOME: _ClassVar[OutputBlendMode]
LOOKUP_INPUT_TYPE_NA: LookupInputType
LOOKUP_INPUT_TYPE_TIME_SEC: LookupInputType
LOOKUP_INPUT_TYPE_TIME_MIN: LookupInputType
LOOKUP_INPUT_TYPE_TIME_HOUR: LookupInputType
LOOKUP_INPUT_TYPE_TIME_SEC_SINCE_SEQUENCE: LookupInputType
LOOKUP_INPUT_TYPE_TIME_SEC_SINCE_CHAIN: LookupInputType
LOOKUP_INPUT_TYPE_SOC: LookupInputType
LOOKUP_INPUT_TYPE_SOC_PU: LookupInputType
LOOKUP_INPUT_TYPE_TMP: LookupInputType
LOOKUP_INPUT_TYPE_PRICE: LookupInputType
LOOKUP_INPUT_TYPE_W_SRC: LookupInputType
LOOKUP_INPUT_TYPE_W_CUT: LookupInputType
LOOKUP_OUTPUT_TYPE_NA: LookupOutputType
LOOKUP_OUTPUT_TYPE_W_CMD: LookupOutputType
LOOKUP_OUTPUT_TYPE_W_ABS: LookupOutputType
LOOKUP_OUTPUT_TYPE_W_MAX_POS: LookupOutputType
LOOKUP_OUTPUT_TYPE_W_MAX_NEG: LookupOutputType
LOOKUP_OUTPUT_TYPE_VA_CMD: LookupOutputType
OUTPUT_BLEND_MODE_OVERRIDE: OutputBlendMode
OUTPUT_BLEND_MODE_CLAMP_ZERO: OutputBlendMode
OUTPUT_BLEND_MODE_ADDITION: OutputBlendMode
OUTPUT_BLEND_MODE_SUBTRACT: OutputBlendMode
OUTPUT_BLEND_MODE_MULTIPLY: OutputBlendMode
OUTPUT_BLEND_MODE_MUL_MASK_ZPOS: OutputBlendMode
OUTPUT_BLEND_MODE_OVERRIDE_SOME: OutputBlendMode

class MinMax(_message.Message):
    __slots__ = ("min", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class Point2D(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class LookupItemAnchor(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class LookupItemAxisRange(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: MinMax
    y: MinMax
    def __init__(self, x: _Optional[_Union[MinMax, _Mapping]] = ..., y: _Optional[_Union[MinMax, _Mapping]] = ...) -> None: ...

class ChartFn(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[Point2D]
    def __init__(self, points: _Optional[_Iterable[_Union[Point2D, _Mapping]]] = ...) -> None: ...

class ChainFn(_message.Message):
    __slots__ = ("charts",)
    CHARTS_FIELD_NUMBER: _ClassVar[int]
    charts: _containers.RepeatedCompositeFieldContainer[ChartFn]
    def __init__(self, charts: _Optional[_Iterable[_Union[ChartFn, _Mapping]]] = ...) -> None: ...

class LookupComplete(_message.Message):
    __slots__ = ("ranges", "win_tms")
    RANGES_FIELD_NUMBER: _ClassVar[int]
    WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[Point2D]
    win_tms: float
    def __init__(self, ranges: _Optional[_Iterable[_Union[Point2D, _Mapping]]] = ..., win_tms: _Optional[float] = ...) -> None: ...

class LookupItem(_message.Message):
    __slots__ = ("anchor", "axis_range", "in_type", "out_type", "chain_fn", "blend_mode", "win_tms", "rmp_tms", "complete")
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    AXIS_RANGE_FIELD_NUMBER: _ClassVar[int]
    IN_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAIN_FN_FIELD_NUMBER: _ClassVar[int]
    BLEND_MODE_FIELD_NUMBER: _ClassVar[int]
    WIN_TMS_FIELD_NUMBER: _ClassVar[int]
    RMP_TMS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    anchor: LookupItemAnchor
    axis_range: _containers.RepeatedCompositeFieldContainer[LookupItemAxisRange]
    in_type: LookupInputType
    out_type: LookupOutputType
    chain_fn: ChainFn
    blend_mode: OutputBlendMode
    win_tms: float
    rmp_tms: float
    complete: LookupComplete
    def __init__(self, anchor: _Optional[_Union[LookupItemAnchor, _Mapping]] = ..., axis_range: _Optional[_Iterable[_Union[LookupItemAxisRange, _Mapping]]] = ..., in_type: _Optional[_Union[LookupInputType, str]] = ..., out_type: _Optional[_Union[LookupOutputType, str]] = ..., chain_fn: _Optional[_Union[ChainFn, _Mapping]] = ..., blend_mode: _Optional[_Union[OutputBlendMode, str]] = ..., win_tms: _Optional[float] = ..., rmp_tms: _Optional[float] = ..., complete: _Optional[_Union[LookupComplete, _Mapping]] = ...) -> None: ...

class LookupSequenceState(_message.Message):
    __slots__ = ("io_snapshot", "completed", "stamp_complete_check", "stamp_sequence_enter", "stamp_chain_enter", "error")
    IO_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    STAMP_COMPLETE_CHECK_FIELD_NUMBER: _ClassVar[int]
    STAMP_SEQUENCE_ENTER_FIELD_NUMBER: _ClassVar[int]
    STAMP_CHAIN_ENTER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    io_snapshot: _containers.RepeatedCompositeFieldContainer[LookupItemAnchor]
    completed: _containers.RepeatedScalarFieldContainer[bool]
    stamp_complete_check: _timestamp_pb2.Timestamp
    stamp_sequence_enter: _timestamp_pb2.Timestamp
    stamp_chain_enter: _timestamp_pb2.Timestamp
    error: str
    def __init__(self, io_snapshot: _Optional[_Iterable[_Union[LookupItemAnchor, _Mapping]]] = ..., completed: _Optional[_Iterable[bool]] = ..., stamp_complete_check: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_sequence_enter: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stamp_chain_enter: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...

class LookupSequence(_message.Message):
    __slots__ = ("ena", "name", "sequence", "state")
    ENA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ena: bool
    name: str
    sequence: _containers.RepeatedCompositeFieldContainer[LookupItem]
    state: LookupSequenceState
    def __init__(self, ena: _Optional[bool] = ..., name: _Optional[str] = ..., sequence: _Optional[_Iterable[_Union[LookupItem, _Mapping]]] = ..., state: _Optional[_Union[LookupSequenceState, _Mapping]] = ...) -> None: ...

class LookupInput(_message.Message):
    __slots__ = ("stamp", "soc", "tmp", "price", "w_src", "w_cut")
    STAMP_FIELD_NUMBER: _ClassVar[int]
    SOC_FIELD_NUMBER: _ClassVar[int]
    TMP_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    W_SRC_FIELD_NUMBER: _ClassVar[int]
    W_CUT_FIELD_NUMBER: _ClassVar[int]
    stamp: _timestamp_pb2.Timestamp
    soc: float
    tmp: float
    price: float
    w_src: float
    w_cut: float
    def __init__(self, stamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., soc: _Optional[float] = ..., tmp: _Optional[float] = ..., price: _Optional[float] = ..., w_src: _Optional[float] = ..., w_cut: _Optional[float] = ...) -> None: ...

class LookupOutput(_message.Message):
    __slots__ = ("w_cmd", "w_max_pos", "w_max_neg", "va_abs")
    W_CMD_FIELD_NUMBER: _ClassVar[int]
    W_MAX_POS_FIELD_NUMBER: _ClassVar[int]
    W_MAX_NEG_FIELD_NUMBER: _ClassVar[int]
    VA_ABS_FIELD_NUMBER: _ClassVar[int]
    w_cmd: float
    w_max_pos: float
    w_max_neg: float
    va_abs: float
    def __init__(self, w_cmd: _Optional[float] = ..., w_max_pos: _Optional[float] = ..., w_max_neg: _Optional[float] = ..., va_abs: _Optional[float] = ...) -> None: ...

class LookupRule(_message.Message):
    __slots__ = ("ena", "rules", "forced")
    class St(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ST_NA: _ClassVar[LookupRule.St]
    ST_NA: LookupRule.St
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
    class Status(_message.Message):
        __slots__ = ("other",)
        OTHER_FIELD_NUMBER: _ClassVar[int]
        other: bool
        def __init__(self, other: _Optional[bool] = ...) -> None: ...
    class Command(_message.Message):
        __slots__ = ("ena", "ena_rule", "add", "delete", "clear", "overwrite")
        class EnaRule(_message.Message):
            __slots__ = ("name", "ena")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ENA_FIELD_NUMBER: _ClassVar[int]
            name: str
            ena: bool
            def __init__(self, name: _Optional[str] = ..., ena: _Optional[bool] = ...) -> None: ...
        class AddRule(_message.Message):
            __slots__ = ("name", "items", "upsert")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            UPSERT_FIELD_NUMBER: _ClassVar[int]
            name: str
            items: _containers.RepeatedCompositeFieldContainer[LookupItem]
            upsert: bool
            def __init__(self, name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[LookupItem, _Mapping]]] = ..., upsert: _Optional[bool] = ...) -> None: ...
        class DeleteRule(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        class ClearRules(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class OverwriteRules(_message.Message):
            __slots__ = ("rules",)
            RULES_FIELD_NUMBER: _ClassVar[int]
            rules: _containers.RepeatedCompositeFieldContainer[LookupSequence]
            def __init__(self, rules: _Optional[_Iterable[_Union[LookupSequence, _Mapping]]] = ...) -> None: ...
        ENA_FIELD_NUMBER: _ClassVar[int]
        ENA_RULE_FIELD_NUMBER: _ClassVar[int]
        ADD_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        CLEAR_FIELD_NUMBER: _ClassVar[int]
        OVERWRITE_FIELD_NUMBER: _ClassVar[int]
        ena: bool
        ena_rule: LookupRule.Command.EnaRule
        add: LookupRule.Command.AddRule
        delete: LookupRule.Command.DeleteRule
        clear: LookupRule.Command.ClearRules
        overwrite: LookupRule.Command.OverwriteRules
        def __init__(self, ena: _Optional[bool] = ..., ena_rule: _Optional[_Union[LookupRule.Command.EnaRule, _Mapping]] = ..., add: _Optional[_Union[LookupRule.Command.AddRule, _Mapping]] = ..., delete: _Optional[_Union[LookupRule.Command.DeleteRule, _Mapping]] = ..., clear: _Optional[_Union[LookupRule.Command.ClearRules, _Mapping]] = ..., overwrite: _Optional[_Union[LookupRule.Command.OverwriteRules, _Mapping]] = ...) -> None: ...
    ENA_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    FORCED_FIELD_NUMBER: _ClassVar[int]
    ena: bool
    rules: _containers.RepeatedCompositeFieldContainer[LookupSequence]
    forced: _containers.RepeatedCompositeFieldContainer[LookupSequence]
    def __init__(self, ena: _Optional[bool] = ..., rules: _Optional[_Iterable[_Union[LookupSequence, _Mapping]]] = ..., forced: _Optional[_Iterable[_Union[LookupSequence, _Mapping]]] = ...) -> None: ...
