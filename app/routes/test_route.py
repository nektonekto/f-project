import json
from fastapi import APIRouter
# from ml_schemas.test_model import TestModel
from typing import Dict, Any, Annotated, List
from app.ml_schemas.test_model import TestModel
from fastapi import Query, Path
from fastapi.responses import RedirectResponse


test_route = APIRouter()


# @test_route.post('/')
# def test_r(data: TestModel):
#     return test_func(data)
from pydantic import BaseModel
class One(BaseModel):
    value: int | str


from app.ml_schemas.svm_model import SVModelSettings
from app.ml_schemas.abs_model import AbstractModelSettingsInput


@test_route.post("/test-uni")
def check_union(model_data: One):
    if One.model_validate(model_data):
        return {
            "success": True
        }
    else:
        return {
            "error": True
        }

@test_route.post("/union-test")
def check_union(model_data: AbstractModelSettingsInput):
    if SVModelSettings.model_validate(model_data.settings):
        return {
            "success": True
        }
    else:
        return {
            "error": True
        }
@test_route.get("/teleport")
def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


@test_route.post('/model-from-gns')
def get_model_from_gns(data: Dict[str, Any]):
    if data.get('settings') is not None:
        print(data.get('settings'))
        return {'success': True,
                'settings': data.get('settings')}
    else:
        return {'success': False}


@test_route.post('/test-request/{check_id}')
def test_request(
        check_id: Annotated[int,
                            Path(
                                   title='id your buy',
                                ge=1,
                                gt=0,
                                le=1000
                            )],
        products: Annotated[List[str] | None,
                            Query(
                                alias='product-list',
                                title='Prod',
                                description='Your list of products',
                                min_length=0,
                                max_length=20
                            )] = None
):

    return {
        'message': f'Your check_id {check_id} is ready. Products: {products} '
    }
