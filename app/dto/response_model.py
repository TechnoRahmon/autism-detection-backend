from typing import Any, Union
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status: bool


class AnyResponse(BaseModel):
    data: list[Any]
    status: bool



protected_responses = {
    200: {"description": "Success", "model": Union[AnyResponse]},
    404: {"description": "Not found", "model": ErrorResponse}
}
