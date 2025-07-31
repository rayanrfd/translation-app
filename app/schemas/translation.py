from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Translation(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    input: str
    output: str
    user_name: str
