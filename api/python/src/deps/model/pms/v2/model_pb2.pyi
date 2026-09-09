import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_INPUT_TYPE_UNSPECIFIED: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_TIME_SEC: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_TIME_MIN: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_TIME_HOUR: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_SOC: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_SOC_PU: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_TMP: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_PRICE: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_W_SRC: _ClassVar[NodeInputType]
    NODE_INPUT_TYPE_W_CUT: _ClassVar[NodeInputType]

class NodeOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_OUTPUT_TYPE_UNSPECIFIED: _ClassVar[NodeOutputType]
    NODE_OUTPUT_TYPE_W_CMD: _ClassVar[NodeOutputType]
    NODE_OUTPUT_TYPE_W_ABS: _ClassVar[NodeOutputType]
    NODE_OUTPUT_TYPE_W_MAX_POS: _ClassVar[NodeOutputType]
    NODE_OUTPUT_TYPE_W_MAX_NEG: _ClassVar[NodeOutputType]
    NODE_OUTPUT_TYPE_VA_CMD: _ClassVar[NodeOutputType]

class NodeOutputBlendMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_OUTPUT_BLEND_MODE_UNSPECIFIED: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_OVERRIDE: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_CLAMP_ZERO: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_ADDITION: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_SUBTRACT: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_MULTIPLY: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_MUL_MASK_ZPOS: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_OVERRIDE_SOME: _ClassVar[NodeOutputBlendMode]
    NODE_OUTPUT_BLEND_MODE_FILTER_NONZERO_ADDITION: _ClassVar[NodeOutputBlendMode]
NODE_INPUT_TYPE_UNSPECIFIED: NodeInputType
NODE_INPUT_TYPE_TIME_SEC: NodeInputType
NODE_INPUT_TYPE_TIME_MIN: NodeInputType
NODE_INPUT_TYPE_TIME_HOUR: NodeInputType
NODE_INPUT_TYPE_SOC: NodeInputType
NODE_INPUT_TYPE_SOC_PU: NodeInputType
NODE_INPUT_TYPE_TMP: NodeInputType
NODE_INPUT_TYPE_PRICE: NodeInputType
NODE_INPUT_TYPE_W_SRC: NodeInputType
NODE_INPUT_TYPE_W_CUT: NodeInputType
NODE_OUTPUT_TYPE_UNSPECIFIED: NodeOutputType
NODE_OUTPUT_TYPE_W_CMD: NodeOutputType
NODE_OUTPUT_TYPE_W_ABS: NodeOutputType
NODE_OUTPUT_TYPE_W_MAX_POS: NodeOutputType
NODE_OUTPUT_TYPE_W_MAX_NEG: NodeOutputType
NODE_OUTPUT_TYPE_VA_CMD: NodeOutputType
NODE_OUTPUT_BLEND_MODE_UNSPECIFIED: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_OVERRIDE: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_CLAMP_ZERO: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_ADDITION: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_SUBTRACT: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_MULTIPLY: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_MUL_MASK_ZPOS: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_OVERRIDE_SOME: NodeOutputBlendMode
NODE_OUTPUT_BLEND_MODE_FILTER_NONZERO_ADDITION: NodeOutputBlendMode

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

class SystemInput(_message.Message):
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

class SystemOutput(_message.Message):
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

class InputId(_message.Message):
    __slots__ = ("node_id", "value_index")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_INDEX_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    value_index: int
    def __init__(self, node_id: _Optional[str] = ..., value_index: _Optional[int] = ...) -> None: ...

class Kits(_message.Message):
    __slots__ = ()
    class InequalitySymbol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INEQUALITY_SYMBOL_UNSPECIFIED: _ClassVar[Kits.InequalitySymbol]
        INEQUALITY_SYMBOL_LT: _ClassVar[Kits.InequalitySymbol]
        INEQUALITY_SYMBOL_LE: _ClassVar[Kits.InequalitySymbol]
        INEQUALITY_SYMBOL_EQ: _ClassVar[Kits.InequalitySymbol]
        INEQUALITY_SYMBOL_GE: _ClassVar[Kits.InequalitySymbol]
        INEQUALITY_SYMBOL_GT: _ClassVar[Kits.InequalitySymbol]
    INEQUALITY_SYMBOL_UNSPECIFIED: Kits.InequalitySymbol
    INEQUALITY_SYMBOL_LT: Kits.InequalitySymbol
    INEQUALITY_SYMBOL_LE: Kits.InequalitySymbol
    INEQUALITY_SYMBOL_EQ: Kits.InequalitySymbol
    INEQUALITY_SYMBOL_GE: Kits.InequalitySymbol
    INEQUALITY_SYMBOL_GT: Kits.InequalitySymbol
    class BooleanOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOOLEAN_OPERATION_UNSPECIFIED: _ClassVar[Kits.BooleanOperation]
        BOOLEAN_OPERATION_AND: _ClassVar[Kits.BooleanOperation]
        BOOLEAN_OPERATION_OR: _ClassVar[Kits.BooleanOperation]
    BOOLEAN_OPERATION_UNSPECIFIED: Kits.BooleanOperation
    BOOLEAN_OPERATION_AND: Kits.BooleanOperation
    BOOLEAN_OPERATION_OR: Kits.BooleanOperation
    class ArithmeticSymbol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARITHMETIC_SYMBOL_UNSPECIFIED: _ClassVar[Kits.ArithmeticSymbol]
        ARITHMETIC_SYMBOL_ADD: _ClassVar[Kits.ArithmeticSymbol]
        ARITHMETIC_SYMBOL_SUBTRACT: _ClassVar[Kits.ArithmeticSymbol]
        ARITHMETIC_SYMBOL_MULTIPLY: _ClassVar[Kits.ArithmeticSymbol]
        ARITHMETIC_SYMBOL_DIVIDE: _ClassVar[Kits.ArithmeticSymbol]
    ARITHMETIC_SYMBOL_UNSPECIFIED: Kits.ArithmeticSymbol
    ARITHMETIC_SYMBOL_ADD: Kits.ArithmeticSymbol
    ARITHMETIC_SYMBOL_SUBTRACT: Kits.ArithmeticSymbol
    ARITHMETIC_SYMBOL_MULTIPLY: Kits.ArithmeticSymbol
    ARITHMETIC_SYMBOL_DIVIDE: Kits.ArithmeticSymbol
    class Inequality(_message.Message):
        __slots__ = ("symbol", "value")
        SYMBOL_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        symbol: Kits.InequalitySymbol
        value: float
        def __init__(self, symbol: _Optional[_Union[Kits.InequalitySymbol, str]] = ..., value: _Optional[float] = ...) -> None: ...
    def __init__(self) -> None: ...

class Nodes(_message.Message):
    __slots__ = ()
    class InputNode(_message.Message):
        __slots__ = ("builtin_input",)
        class State(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _struct_pb2.Value
            def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        BUILTIN_INPUT_FIELD_NUMBER: _ClassVar[int]
        builtin_input: NodeInputType
        def __init__(self, builtin_input: _Optional[_Union[NodeInputType, str]] = ...) -> None: ...
    class OutputNode(_message.Message):
        __slots__ = ("input_id", "output", "blend_mode")
        class State(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _struct_pb2.Value
            def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        INPUT_ID_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        BLEND_MODE_FIELD_NUMBER: _ClassVar[int]
        input_id: InputId
        output: NodeOutputType
        blend_mode: NodeOutputBlendMode
        def __init__(self, input_id: _Optional[_Union[InputId, _Mapping]] = ..., output: _Optional[_Union[NodeOutputType, str]] = ..., blend_mode: _Optional[_Union[NodeOutputBlendMode, str]] = ...) -> None: ...
    class ConstantNode(_message.Message):
        __slots__ = ("value",)
        class State(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _struct_pb2.Value
            def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _struct_pb2.Value
        def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class ParameterNode(_message.Message):
        __slots__ = ("default_value", "parameter_name")
        class State(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _struct_pb2.Value
            def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
        default_value: _struct_pb2.Value
        parameter_name: str
        def __init__(self, default_value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., parameter_name: _Optional[str] = ...) -> None: ...
    class RuleNode(_message.Message):
        __slots__ = ("rule_id", "input_ena", "input_parameters")
        RULE_ID_FIELD_NUMBER: _ClassVar[int]
        INPUT_ENA_FIELD_NUMBER: _ClassVar[int]
        INPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        rule_id: str
        input_ena: InputId
        input_parameters: _containers.RepeatedCompositeFieldContainer[InputId]
        def __init__(self, rule_id: _Optional[str] = ..., input_ena: _Optional[_Union[InputId, _Mapping]] = ..., input_parameters: _Optional[_Iterable[_Union[InputId, _Mapping]]] = ...) -> None: ...
    class CompareNode(_message.Message):
        __slots__ = ("input_id", "reduce_operation", "conditions")
        class State(_message.Message):
            __slots__ = ("compares", "sum")
            COMPARES_FIELD_NUMBER: _ClassVar[int]
            SUM_FIELD_NUMBER: _ClassVar[int]
            compares: _containers.RepeatedScalarFieldContainer[bool]
            sum: bool
            def __init__(self, compares: _Optional[_Iterable[bool]] = ..., sum: _Optional[bool] = ...) -> None: ...
        INPUT_ID_FIELD_NUMBER: _ClassVar[int]
        REDUCE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        input_id: InputId
        reduce_operation: Kits.BooleanOperation
        conditions: _containers.RepeatedCompositeFieldContainer[Kits.Inequality]
        def __init__(self, input_id: _Optional[_Union[InputId, _Mapping]] = ..., reduce_operation: _Optional[_Union[Kits.BooleanOperation, str]] = ..., conditions: _Optional[_Iterable[_Union[Kits.Inequality, _Mapping]]] = ...) -> None: ...
    class BooleanReducerNode(_message.Message):
        __slots__ = ("operation", "input_ids")
        class State(_message.Message):
            __slots__ = ("result",)
            RESULT_FIELD_NUMBER: _ClassVar[int]
            result: _containers.RepeatedScalarFieldContainer[bool]
            def __init__(self, result: _Optional[_Iterable[bool]] = ...) -> None: ...
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        INPUT_IDS_FIELD_NUMBER: _ClassVar[int]
        operation: Kits.BooleanOperation
        input_ids: _containers.RepeatedCompositeFieldContainer[InputId]
        def __init__(self, operation: _Optional[_Union[Kits.BooleanOperation, str]] = ..., input_ids: _Optional[_Iterable[_Union[InputId, _Mapping]]] = ...) -> None: ...
    class ArithmeticNode(_message.Message):
        __slots__ = ("first_id", "second_id", "operation")
        class State(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _struct_pb2.Value
            def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        FIRST_ID_FIELD_NUMBER: _ClassVar[int]
        SECOND_ID_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        first_id: InputId
        second_id: InputId
        operation: Kits.ArithmeticSymbol
        def __init__(self, first_id: _Optional[_Union[InputId, _Mapping]] = ..., second_id: _Optional[_Union[InputId, _Mapping]] = ..., operation: _Optional[_Union[Kits.ArithmeticSymbol, str]] = ...) -> None: ...
    class HysteresisNode(_message.Message):
        __slots__ = ("input_id", "lower_threshold", "upper_threshold")
        class State(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: bool
            def __init__(self, value: _Optional[bool] = ...) -> None: ...
        INPUT_ID_FIELD_NUMBER: _ClassVar[int]
        LOWER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        UPPER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        input_id: InputId
        lower_threshold: float
        upper_threshold: float
        def __init__(self, input_id: _Optional[_Union[InputId, _Mapping]] = ..., lower_threshold: _Optional[float] = ..., upper_threshold: _Optional[float] = ...) -> None: ...
    def __init__(self) -> None: ...

class NodeItem(_message.Message):
    __slots__ = ("input_node", "output_node", "constant_node", "parameter_node", "rule_node", "compare_node", "boolean_reducer_node", "arithmetic_node", "hysteresis_node", "meta")
    INPUT_NODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NODE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_NODE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NODE_FIELD_NUMBER: _ClassVar[int]
    RULE_NODE_FIELD_NUMBER: _ClassVar[int]
    COMPARE_NODE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_REDUCER_NODE_FIELD_NUMBER: _ClassVar[int]
    ARITHMETIC_NODE_FIELD_NUMBER: _ClassVar[int]
    HYSTERESIS_NODE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    input_node: Nodes.InputNode
    output_node: Nodes.OutputNode
    constant_node: Nodes.ConstantNode
    parameter_node: Nodes.ParameterNode
    rule_node: Nodes.RuleNode
    compare_node: Nodes.CompareNode
    boolean_reducer_node: Nodes.BooleanReducerNode
    arithmetic_node: Nodes.ArithmeticNode
    hysteresis_node: Nodes.HysteresisNode
    meta: str
    def __init__(self, input_node: _Optional[_Union[Nodes.InputNode, _Mapping]] = ..., output_node: _Optional[_Union[Nodes.OutputNode, _Mapping]] = ..., constant_node: _Optional[_Union[Nodes.ConstantNode, _Mapping]] = ..., parameter_node: _Optional[_Union[Nodes.ParameterNode, _Mapping]] = ..., rule_node: _Optional[_Union[Nodes.RuleNode, _Mapping]] = ..., compare_node: _Optional[_Union[Nodes.CompareNode, _Mapping]] = ..., boolean_reducer_node: _Optional[_Union[Nodes.BooleanReducerNode, _Mapping]] = ..., arithmetic_node: _Optional[_Union[Nodes.ArithmeticNode, _Mapping]] = ..., hysteresis_node: _Optional[_Union[Nodes.HysteresisNode, _Mapping]] = ..., meta: _Optional[str] = ...) -> None: ...

class NodeState(_message.Message):
    __slots__ = ("input_node_state", "output_node_state", "constant_node_state", "parameter_node_state", "compare_node_state", "boolean_reducer_node_state", "arithmetic_node_state", "hysteresis_node_state")
    INPUT_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    COMPARE_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_REDUCER_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    ARITHMETIC_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    HYSTERESIS_NODE_STATE_FIELD_NUMBER: _ClassVar[int]
    input_node_state: Nodes.InputNode.State
    output_node_state: Nodes.OutputNode.State
    constant_node_state: Nodes.ConstantNode.State
    parameter_node_state: Nodes.ParameterNode.State
    compare_node_state: Nodes.CompareNode.State
    boolean_reducer_node_state: Nodes.BooleanReducerNode.State
    arithmetic_node_state: Nodes.ArithmeticNode.State
    hysteresis_node_state: Nodes.HysteresisNode.State
    def __init__(self, input_node_state: _Optional[_Union[Nodes.InputNode.State, _Mapping]] = ..., output_node_state: _Optional[_Union[Nodes.OutputNode.State, _Mapping]] = ..., constant_node_state: _Optional[_Union[Nodes.ConstantNode.State, _Mapping]] = ..., parameter_node_state: _Optional[_Union[Nodes.ParameterNode.State, _Mapping]] = ..., compare_node_state: _Optional[_Union[Nodes.CompareNode.State, _Mapping]] = ..., boolean_reducer_node_state: _Optional[_Union[Nodes.BooleanReducerNode.State, _Mapping]] = ..., arithmetic_node_state: _Optional[_Union[Nodes.ArithmeticNode.State, _Mapping]] = ..., hysteresis_node_state: _Optional[_Union[Nodes.HysteresisNode.State, _Mapping]] = ...) -> None: ...

class NodeRuleConfig(_message.Message):
    __slots__ = ("name", "description", "ena", "items")
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NodeItem
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NodeItem, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    ena: bool
    items: _containers.MessageMap[str, NodeItem]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., ena: _Optional[bool] = ..., items: _Optional[_Mapping[str, NodeItem]] = ...) -> None: ...

class NodeRuleState(_message.Message):
    __slots__ = ("ena", "items", "error")
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NodeState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NodeState, _Mapping]] = ...) -> None: ...
    ENA_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ena: bool
    items: _containers.MessageMap[str, NodeState]
    error: str
    def __init__(self, ena: _Optional[bool] = ..., items: _Optional[_Mapping[str, NodeState]] = ..., error: _Optional[str] = ...) -> None: ...

class RootConfig(_message.Message):
    __slots__ = ("ena_root", "rules")
    ENA_ROOT_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    ena_root: bool
    rules: _containers.RepeatedCompositeFieldContainer[NodeRuleConfig]
    def __init__(self, ena_root: _Optional[bool] = ..., rules: _Optional[_Iterable[_Union[NodeRuleConfig, _Mapping]]] = ...) -> None: ...

class RootState(_message.Message):
    __slots__ = ("ena_root", "rules")
    ENA_ROOT_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    ena_root: bool
    rules: _containers.RepeatedCompositeFieldContainer[NodeRuleState]
    def __init__(self, ena_root: _Optional[bool] = ..., rules: _Optional[_Iterable[_Union[NodeRuleState, _Mapping]]] = ...) -> None: ...
