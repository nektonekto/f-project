from fastapi import APIRouter
from app.services.db_info import DBService
from app.schemes.db_info_models import DBConnectModel,DBConnectResponceModel


db_router = APIRouter()


@db_router.post('/databases', response_model=DBConnectResponceModel)
def get_databases(data: DBConnectModel) -> DBConnectResponceModel:
    """Return a list of all databases

    Args:
        data (DBConnectModel): Database connection parameters

    Returns:
        DBConnectResponceModel: Database list
    """
    new_connection = DBService(data)
    return new_connection.get_db_list()
    

@db_router.post('/connect-database', response_model=DBConnectResponceModel)
def connect_database(data: DBConnectModel) -> DBConnectResponceModel:
    """Connect ot the database

    Args:
        data (DBConnectModel): Database connection parameters

    Returns:
        DBConnectResponceModel: Connection object
    """
    new_connection = DBService(data)
    new_connection.connect()
    return new_connection.check_connect()

