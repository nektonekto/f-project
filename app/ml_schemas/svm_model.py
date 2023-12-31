from pydantic import BaseModel
from typing import List, Optional, Union, Dict


class SVModelSettings(BaseModel):
    """Class for declaring SVM-model"""
    description: str = "SV-method"
    C: float
    kernel: str
    degree: int
    gamma: str
    coef0: float
    shrinking: bool
    probability: bool
    tol: float
    cache_size: float
    class_weight: dict
    verbose: bool
    decision_function_shape: str
    break_ties: bool
    random_state: int
    epsilon: Union[float, None]
    max_iter: Union[int, None]


# class SVModelOut(BaseModel):
#     id: int
#     methodTraining: str
#     score: List




