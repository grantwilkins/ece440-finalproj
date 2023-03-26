from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LightReply(_message.Message):
    __slots__ = ["light_id", "user_id"]
    LIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    light_id: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., light_id: _Optional[int] = ...) -> None: ...

class LightRequest(_message.Message):
    __slots__ = ["light_id", "user_id"]
    LIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    light_id: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., light_id: _Optional[int] = ...) -> None: ...
