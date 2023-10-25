import json
from fastapi import APIRouter
# from models.test_model import TestModel
from typing import Dict, Any
from app.models.test_model import TestModel

test_route = APIRouter()


# @test_route.post('/')
# def test_r(data: TestModel):
#     return test_func(data)    


@test_route.post('/model-from-gns')
def get_model_from_gns(data: Dict[str, Any]):
    if data.get('settings') is not None:
        print(data.get('settings'))
        return {'success': True,
                'settings': data.get('settings')}
    else: return {'success': False}