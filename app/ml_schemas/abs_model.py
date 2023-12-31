from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Union, Any

from app.ml_schemas.svm_model import SVModelSettings
from app.ml_schemas.kneighbors_model import KNeighborsModelSettings
from app.ml_schemas.decision_tree_model import DecisionTreeClassifierModelSettings, DecisionTreeRegressorModelSettings
from app.ml_schemas.iforest_model import IsolationForestModelSettings
from app.ml_schemas.gaussiannb_model import GaussianNBModelSettings
from app.ml_schemas.dbscan_model import DBSCANModelSettings
from app.ml_schemas.kmeans_model import KMeansModelSettings


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class AbstractModelSettingsInput(BaseModel):
    uuid: str
    url: str
    name: str
    descr: str
    project: str
    parent: Optional[str]
    settings: Union[KNeighborsModelSettings | DecisionTreeClassifierModelSettings |
                    DecisionTreeRegressorModelSettings | IsolationForestModelSettings | GaussianNBModelSettings |
                    DBSCANModelSettings | KMeansModelSettings]
    created: str
    updated: str
    started: Optional[str]
    finished: Optional[str]
    owner: str
    owner_name: str
    status: str
    progress: float
    division: float
    train_dataset: str
    train_dataset_name: str
    val_dataset: str
    val_dataset_name: str
    test_dataset: Optional[str]
    test_dataset_name: str
    test_settings: Union[SVModelSettings | KNeighborsModelSettings | DecisionTreeClassifierModelSettings |
                         DecisionTreeRegressorModelSettings | IsolationForestModelSettings | GaussianNBModelSettings |
                         DBSCANModelSettings | KMeansModelSettings]
    test_started: Optional[str]
    test_updated: Optional[str]
    test_finished: Optional[str]
    test_status: str
    test_progress: float
    test_accuracy: float
    checkpoints: list
    hpo_exists: bool
    nas_exists: bool



from app.services.svm_model_service import SVCModel
class AbstractModelSettingsOut(BaseModel):
    id: int
    type_model: str
    model_settings: (SVModelSettings | KNeighborsModelSettings | DecisionTreeClassifierModelSettings |
                     DecisionTreeRegressorModelSettings | IsolationForestModelSettings | GaussianNBModelSettings |
                     DBSCANModelSettings | KMeansModelSettings)
    score: list

