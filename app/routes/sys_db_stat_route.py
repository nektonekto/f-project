from fastapi import APIRouter
from app.services.db_info import DBService
from app.schemes.sys_db_stat_schema import DBConnectModel,DBConnectResponceModel


db_router = APIRouter()


@db_router.post('/databases', response_model=DBConnectResponceModel)
def get_databases(data: DBConnectModel):
    new_connection = DBService(data)
    # new_connection.connect()
    return new_connection.get_db_list()
    

@db_router.post('/connect-database', response_model=DBConnectResponceModel)
def connect_database(data: DBConnectModel) -> DBConnectResponceModel:
    new_connection = DBService(data)
    new_connection.connect()
    return new_connection.check_connect()

