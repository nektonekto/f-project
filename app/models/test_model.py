from pydantic import BaseModel
from typing import Union, List, Tuple


class TestModel(BaseModel):
    param1: Union[int, None]
    param2: int
    param3: List[dict]