from fastapi import APIRouter, Depends, Query
from typing import Annotated

from app.models.abs_model import AbstractModelSettingsInput, AbstractModelSettingsOut
from enum import Enum

model_route = APIRouter()


class ModelID(int, Enum):
    svm = 1
    ngbrs = 2


@model_route.post('/model_settings/model_id={model_id}', response_model=AbstractModelSettingsOut)
def get_model_settings(model_id: ModelID, data: AbstractModelSettingsInput) -> AbstractModelSettingsOut:
    """Transmitting model parameters for training
    ____
    Args:

    model_id: id model \n
    data: all parameters for the model in the current project
    _______
    Returns:

    AbstractModelSettingsOut: the result of training the model
    """
    from app.services.svm_model_service import SVCModel
    model_settings = data.settings
    print(model_settings.description)
    svm_model = SVCModel(model_settings)
    print(svm_model.get_parameters())

    return AbstractModelSettingsOut(
        id=model_id,
        model_settings=data.settings,
        score=[0.44]
    )
