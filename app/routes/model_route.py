from fastapi import APIRouter, Depends
from typing import Dict, Any

from pydantic import ValidationError
from app.schemes.SVModel import SVModelInput, SVModelOut

model_route = APIRouter()


@model_route.put('/model_settings/model_id={model_id}', response_model=SVModelOut)
def get_model_settings(model_id: int, data: Dict[str, Any]) -> SVModelOut:
    """Loading hyperparameters of the model.

    :param model_id: id model.
    :param data: json hyperparametes.
    :return: WIP...
    """
    # settings = data.get('settings')
    new_model = SVModelInput.model_validate(data.get('settings'))
    print(new_model)
    return SVModelOut(
        id=model_id,
        methodTraining=new_model.description,
        score=[0.44]
    )
