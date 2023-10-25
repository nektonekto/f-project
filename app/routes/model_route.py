from fastapi import APIRouter, Depends

from app.models.ml_model import AbstractModelSettingsInput, AbstractModelSettingsOut

model_route = APIRouter()


@model_route.put('/model_settings/model_id={model_id}', response_model=AbstractModelSettingsOut)
def get_model_settings(model_id: int, data: AbstractModelSettingsInput) -> AbstractModelSettingsOut:
    """Loading hyperparameters of the model.

    :param model_id: id model.
    :param data: json hyperparametes.
    :return: WIP...
    """

    return AbstractModelSettingsOut(
        id=model_id,
        model_settings=data.settings,
        score=[0.44]
    )
