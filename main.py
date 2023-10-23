from fastapi import FastAPI
from fastapi import APIRouter
from app.routes.db_info_route import db_router
import uvicorn

from app.services.db_info import DBService
from app.schemes.db_info_models import DBConnectModel
from app.schemes.db_info_models import DBConnectResponceModel


app = FastAPI()


main_api_router = APIRouter()

main_api_router.include_router(db_router, prefix='/db', tags=['db'])
app.include_router(main_api_router)


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