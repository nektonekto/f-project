from pydantic import BaseModel, ConfigDict
from app._types import MatrixLike, ArrayLike, Float, Int


class GaussianNBModelSettings(BaseModel):
    """Class for declaring the GaussianNB-model"""

    model_config = ConfigDict(arbitrary_types_allowed=True)


    priors: ArrayLike | None = None
    var_smoothing: Float = 1e-9