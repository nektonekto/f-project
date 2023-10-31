from pydantic import BaseModel, ConfigDict
from typing import Literal
from numpy.random import RandomState

class IsolationForestModelSettings(BaseModel):
    """Class for declaring the IForest-model"""
    model_config = ConfigDict(arbitrary_types_allowed=True)

    n_estimators: int = 100
    max_samples: float | Literal["auto", "auto"] | int = "auto"
    contamination: float | str = "auto"
    max_features: float | int = 1.0
    bootstrap: bool = False
    n_jobs: None | int = None
    random_state: RandomState | None | int = None
    verbose: int = 0
    warm_start: bool = False
