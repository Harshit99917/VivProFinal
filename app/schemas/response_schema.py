
from typing import Optional, Any
from pydantic import BaseModel


class StandardResponse(BaseModel):
    status: str  # "success" or "error"
    message: str
    data: Optional[Any] = None
