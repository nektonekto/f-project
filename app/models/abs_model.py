from pydantic import BaseModel
from typing import Optional, List, Union

from app.models.svm_model import SVModelSettings
from app.models.kneighbors_model import KNeighborsModelSettings
from app.models.decision_tree_model import DecisionTreeClassifierModelSettings, DecisionTreeRegressorModelSettings
from app.models.iforest_model import IsolationForestModelSettings
from app.models.gaussiannb_model import GaussianNBModelSettings
from app.models.dbscan_model import DBSCANModelSettings
from app.models.kmeans_model import KMeansModelSettings


class AbstractModelSettingsInput(BaseModel):
    uuid: str
    url: str
    name: str
    descr: str
    project: str
    parent: Optional[str]
    settings: (SVModelSettings | KNeighborsModelSettings | DecisionTreeClassifierModelSettings |
               DecisionTreeRegressorModelSettings | IsolationForestModelSettings | GaussianNBModelSettings |
               DBSCANModelSettings | KMeansModelSettings)
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
    test_settings: (SVModelSettings | KNeighborsModelSettings | DecisionTreeClassifierModelSettings |
                    DecisionTreeRegressorModelSettings | IsolationForestModelSettings | GaussianNBModelSettings |
                    DBSCANModelSettings | KMeansModelSettings)
    test_started: Optional[str]
    test_updated: Optional[str]
    test_finished: Optional[str]
    test_status: str
    test_progress: float
    test_accuracy: float
    checkpoints: list
    hpo_exists: bool
    nas_exists: bool


class AbstractModelSettingsOut(BaseModel):
    id: int
    model_settings: (SVModelSettings | KNeighborsModelSettings | DecisionTreeClassifierModelSettings |
                     DecisionTreeRegressorModelSettings | IsolationForestModelSettings | GaussianNBModelSettings |
                     DBSCANModelSettings | KMeansModelSettings)
    score: List
