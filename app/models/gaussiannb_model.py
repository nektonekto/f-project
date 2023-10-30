from pydantic import BaseModel
from app._types import MatrixLike, ArrayLike, Float, Int


class GaussianNBModelSettings(BaseModel):
    """Class for declaring the GaussianNB-model"""

    priors: ArrayLike | None = None
    var_smoothing: Float = 1e-9