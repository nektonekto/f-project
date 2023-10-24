from fastapi import APIRouter, Depends
from typing import Dict, Any

from pydantic import ValidationError
from app.services.SVModel_service import svm_training
from app.schemes.SVModel import SVModelInput, SVModelOut

model_route = APIRouter()


@model_route.put('/model_settings/model_id={model_id}', response_model=SVModelOut)
def get_model_settings(model_id: int,
                       data: Dict[str, Any]) -> SVModelOut:
    settings = data.get('settings')
    # new_model = SVModelInput(**settings)
    new_model = SVModelInput.model_validate(settings)

    return svm_training(model_id, new_model)