from pydantic import BaseModel, ConfigDict
from numpy.random import RandomState
from typing import Mapping, Literal, Sequence, Optional
from app._types import Int, Float


# TODO: Необходимо будет проверить типы параметров и реализовать преобразование в numpy-типы
class DecisionTreeBaseModelSettings(BaseModel):
    """Class for declaring the base DecisionTreeSettings model"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: str | None = None
    criterion: list
    splitter: Literal["best", "random", "best"] = "best"
    max_depth: Int | None = None
    min_samples_split: float | int = 2
    min_samples_leaf: float | int = 1
    min_weight_fraction_leaf: Float = 0.0
    max_features: float | None | Literal["auto", "sqrt", "log2"] | int = None
    random_state: RandomState | None | Int = None
    max_leaf_nodes: Int | None = None
    min_impurity_decrease: Float = 0.0
    class_weight: None | Mapping | str | Sequence[Mapping] = None
    ccp_alpha: float = 0.0


class DecisionTreeClassifierModelSettings(DecisionTreeBaseModelSettings):
    """Class for declaring the DecisionTreeClassifier model"""

    criterion: Literal["gini", "entropy", "log_loss", "gini"] = "gini"
    class_weight: None | Mapping | str | Sequence[Mapping] = None


class DecisionTreeRegressorModelSettings(DecisionTreeBaseModelSettings):
    """Class for declaring the DecisionTreeRegressor model"""

    criterion: Literal[
                "squared_error",
                "friedman_mse",
                "absolute_error",
                "poisson",
                "squared_error",
            ] = "squared_error"
