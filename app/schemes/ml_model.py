from pydantic import BaseModel
from typing import List, Optional, Union


class SVModel(BaseModel):
    type: str
    beta1: float
    beta2: float

# class ModelOut(BaseModel):
#     """Class for returning the training model"""

#     id: int
#     projectID: int
#     methodTrainingID: int
#     params: List[dict]
#     name: Union[str, None]
#     status: Union[str, None]
#     fileData: Union[dict, None]
#     score: List[dict]


# class ResultTrainingModelOut(BaseModel):
#     """Class for returning model training results"""

#     id: int
#     modelID: int
#     methodTrainingID: int
#     score: List[dict]

