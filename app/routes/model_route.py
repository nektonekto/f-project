from fastapi import APIRouter, Depends
from typing import Dict, Any

from pydantic import ValidationError
from app.schemes.ml_model import SVModel

model_route = APIRouter()


@model_route.put('/model_settings/model_id={model_id}', response_model=SVModel)
def get_model_settings(model_id: int, data: Dict[str, Any]) -> SVModel:
    if data.get('settings') is not None:
        try:
            return get_settings_from_json(data)
        except ValidationError as e:
            return {'success': False,
                    'error': e}
        # res = data.get('settings')
        # return {'success': True,
        #         'model_id': model_id,
        #         'model_settings': res,
        #         'type': res['type']
        #         }
    



# не работает
# @model_route.post('/model_settings/model_id={model_id}')
# def get_model_settings(model_id: int, data: SVModel = Depends(get_settings_from_json)):
# # def get_model_settings(model_id: int, data: Dict[str, Any]):
#     # if data.get('settings') is not None:
#     #     return {'success': True,
#     #             'model_id': model_id,
#     #             'model_params': data.get('settings')}
#     return {'result': data}

def get_settings_from_json(data):
    settings = data.get('settings')
    return SVModel(
        type=settings['type'],
        beta1=settings['beta1'],
        beta2=settings['beta2']
    )