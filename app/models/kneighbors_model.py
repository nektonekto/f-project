from pydantic import BaseModel
from typing import List, Optional, Union, Dict


class KNeighborsModelSettings(BaseModel):
    """Class for declaring KNeighborsClassifier model"""
    n_neighbors: int
    weights: str
    algorithm: str
    leaf_size: int
    p: int
    metric: str
    metric_params: dict
    n_jobs: int


