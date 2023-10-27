import json
from fastapi import APIRouter
# from models.test_model import TestModel
from typing import Dict, Any, Annotated, List
from app.models.test_model import TestModel
from fastapi import Query, Path

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
        'message': f'Your check {check_id} is ready. Products: {products} '
    }
