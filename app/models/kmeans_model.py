from pydantic import BaseModel, ConfigDict
from typing import Callable, Literal
from app._types import Int, Float, MatrixLike
from numpy.random import RandomState


class KMeansModelSettings(BaseModel):
    """Class for declaring KMeans-model"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    n_clusters: Int = 8
    init: MatrixLike | Callable | Literal["random", "k-means++", "k-means++"] = "k-means++"
    n_init: Literal["auto", "warn"] | int = "warn"
    max_iter: Int = 300
    tol: Float = 1e-4
    verbose: Int = 0
    random_state: RandomState | None | Int = None
    copy_x: bool = True
    algorithm: Literal["lloyd", "elkan", "auto", "full", "lloyd"] = "lloyd"


