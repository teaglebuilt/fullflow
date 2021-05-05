from typing import Dict
from pydantic import BaseModel, Field


class Client(BaseModel):

    name: str = Field(..., description="Name of client")