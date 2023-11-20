from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import ShowUser
from db.session import get_db
from app.actions.user import _get_user_by_id
import asyncio

db_route = APIRouter()


@db_route.post('/get-users', response_model=ShowUser)
async def get_user_by_id(user_id: int,
                         db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _get_user_by_id(user_id=user_id, session=db)



# from fastapi import APIRouter
# from app.ml_schemas.db_info_model import DBConnectModel,DBConnectResponceModel
# from app.services.db_info_service import DBService
# from db.session import get_db
#
# db_route = APIRouter()
#
#
# @db_route.post('/databases', response_model=DBConnectResponceModel)
# async def get_databases(data: DBConnectModel) -> DBConnectResponceModel:
#     """Return a list of all databases
#
#     Args:
#         data (DBConnectModel): Database connection parameters
#
#     Returns:
#         DBConnectResponceModel: Database list
#     """
#     db = get_db()
#     return await DBService().get_all_databases()
#
#
# @db_route.post('/connect-database', response_model=DBConnectResponceModel)
# async def connect_database(data: DBConnectModel) -> DBConnectResponceModel:
#     """Connect ot the database
#
#     Args:
#         data (DBConnectModel): Database connection parameters
#
#     Returns:
#         DBConnectResponceModel: Connection object
#     """
#     new_connection = DBService(data)
#     new_connection.connect()
#     return await new_connection.check_connect()
#
