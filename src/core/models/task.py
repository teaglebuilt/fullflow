from typing import Dict, Union
from pydantic import BaseModel, Field


class Task(BaseModel):
    input: Union[str, List[str], None] = Field