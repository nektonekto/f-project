from pydantic import BaseModel, ConfigDict
from typing import Callable, Literal
from app._types import Int, Float, MatrixLike
from numpy.random import RandomState


class DBSCANModelSettings(BaseModel):
    """Class for declaring DBSCAN-model"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: str = "DBSCAN-method"
    eps: Float = 0.5
    min_samples: Int = 5
    metric: str | Callable = "euclidean"
    metric_params: dict | None
    algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto"
    leaf_size: Int = 30
    p: Float | None = None
    n_jobs: Int | None = None


