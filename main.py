import json
from fastapi import FastAPI
from app.services.db_info import DBService
from app.schemes.db_info_models import DBConnectModel
from app.schemes.db_info_models import DBConnectResponceModel
# from app.schemes.test import connection

app = FastAPI()


@app.post('/databases-list')
def index(data: DBConnectModel):
    new_connection = DBService(data)
    new_connection.connect()
    return new_connection.get_db_list()
    


@app.get('/databases')
def databases():
    return {'None databases'}


@app.post('/connect_database', response_model=DBConnectResponceModel)
def connect_database(data: DBConnectModel) -> DBConnectResponceModel:
    new_connection = DBService(data)
    new_connection.connect()
    return new_connection.check_connect()




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