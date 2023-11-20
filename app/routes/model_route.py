from fastapi import APIRouter, Depends, Query
from typing import Annotated

from app.ml_schemas.abs_model import AbstractModelSettingsInput, AbstractModelSettingsOut
from enum import Enum
import asyncio

model_route = APIRouter()


class ModelID(int, Enum):
    svm = 1
    ngbrs = 2


@model_route.post('/model_settings/model_id={model_id}', response_model=AbstractModelSettingsOut)
async def get_model_settings(model_id: ModelID, data: AbstractModelSettingsInput) -> AbstractModelSettingsOut:
    """Transmitting model parameters for training
    ____
    Args:

    model_id: id model \n
    data: all parameters for the model in the current project
    _______
    Returns:

    AbstractModelSettingsOut: the result of training the model
    """

    # model_settings = data.settings

    res = await get_model(data)

    return await AbstractModelSettingsOut(
        id=model_id,
        type_model=res,
        model_settings=data.settings,
        score=[0.44]
    )


from app.services.svm_model_service import SVCModel, SVRModel
from app.services.kneighbors_model_service import KNeighborsClassifierModel, KNeighborsRegressorModel


async def get_model(data):
    print(data.settings.description)
    if data.settings.description == "SVC-method":
        model = SVCModel(data.settings)
        return await model.get_parameters()
    elif data.settings.description == "SVR-method":
        model = SVRModel(data.settings)
        return await model.get_parameters()
    elif data.settings.description == "KNC-method":
        model = KNeighborsClassifierModel(data.settings)
        return await model.get_parameters()
    elif data.settings.description == "KNR-method":
        model = KNeighborsRegressorModel(data.settings)
        return await model.get_parameters()
