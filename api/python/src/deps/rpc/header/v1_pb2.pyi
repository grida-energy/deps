from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("uuid", "resp_topic")
    UUID_FIELD_NUMBER: _ClassVar[int]
    RESP_TOPIC_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    resp_topic: str
    def __init__(self, uuid: _Optional[str] = ..., resp_topic: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("uuid", "error")
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_SUCCESS: _ClassVar[Response.ErrorCode]
        ERROR_CODE_NOT_IMPLEMENTED: _ClassVar[Response.ErrorCode]
        ERROR_CODE_NOT_SUPPORTED_MESSAGE: _ClassVar[Response.ErrorCode]
        ERROR_CODE_INVALID_PARAMETER: _ClassVar[Response.ErrorCode]
        ERROR_CODE_NOT_APPLICABLE: _ClassVar[Response.ErrorCode]
        ERROR_CODE_INTERNAL_ERROR: _ClassVar[Response.ErrorCode]
    ERROR_CODE_SUCCESS: Response.ErrorCode
    ERROR_CODE_NOT_IMPLEMENTED: Response.ErrorCode
    ERROR_CODE_NOT_SUPPORTED_MESSAGE: Response.ErrorCode
    ERROR_CODE_INVALID_PARAMETER: Response.ErrorCode
    ERROR_CODE_NOT_APPLICABLE: Response.ErrorCode
    ERROR_CODE_INTERNAL_ERROR: Response.ErrorCode
    class Error(_message.Message):
        __slots__ = ("code", "detail")
        CODE_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        code: Response.ErrorCode
        detail: str
        def __init__(self, code: _Optional[_Union[Response.ErrorCode, str]] = ..., detail: _Optional[str] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    error: Response.Error
    def __init__(self, uuid: _Optional[str] = ..., error: _Optional[_Union[Response.Error, _Mapping]] = ...) -> None: ...
