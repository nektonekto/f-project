import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from app.routes.db_info_route import db_route
from app.routes.test_route import test_route
from app.routes.model_route import model_route


app = FastAPI()


main_api_router = APIRouter()

main_api_router.include_router(db_route, prefix='/db', tags=['db'])
main_api_router.include_router(test_route, prefix='/tst', tags=['tst'])
main_api_router.include_router(model_route, prefix='/model', tags=['mdl'])
app.include_router(main_api_router)

#
# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)



# ------------Примеры использования responce_model-----------
# def connect_v1():
#     return {
#         'succes': True,
#         'error': False
#     }


# def connect_v2():
#     return DBResponceModel(
#         success=False,
#         error=True
#     )


# @app.post('/connect-database', response_model=DBResponceModel)
# def get_db_v1():
#     # ?connect = DBService(db_data)
#     result_connection = connect_v1()
#     return DBResponceModel(**result_connection)


# @app.post('/connect-database-v2', response_model=DBResponceModel)
# def get_db_v2():
#     # ?connect = DBService(db_data)
#     return connect_v2()

# 
# -------------------------------------------------------------