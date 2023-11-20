# import psycopg2
# from app.ml_schemas.db_info_model import DBConnectResponceModel
#
#
# class DBService:
#     def __init__(self, data):
#         self.database = data.database
#         self.user = data.user
#         self.password = data.password
#         self.host = data.host
#         self.port = data.port
#         self.conn = None
#
#     def connect(self):
#         try:
#             self.conn = psycopg2.connect(
#                 dbname=self.database,
#                 user=self.user,
#                 password=self.password,
#                 host=self.host,
#                 port=self.port
#             )
#         except Exception as e:
#             return DBConnectResponceModel(
#                 message=f'Ошибка подключения:{e}',
#                 error=True
#             )
#
#     def disconnect(self):
#         if self.conn:
#             self.conn.close()
#
#     def get_db_list(self):
#         if not self.conn:
#             self.connect()
#
#         try:
#             with self.conn.cursor() as cursor:
#                 cursor.execute(f'SELECT * FROM pg_database')
#                 return DBConnectResponceModel(
#                     message=f'Соединение установлено.'
#                             f'Список баз данных:: {cursor.fetchall()}',
#                     error=False
#                     )
#
#         except Exception as e:
#             return DBConnectResponceModel(
#                 message=f'Ошибка получения списка БД',
#                 error=True
#             )
#
#     async def check_connect(self):
#         if self.conn:
#             return DBConnectResponceModel(
#                 message=f'Соединение установлено.'
#                         f'Объект соединения: {self.conn}',
#                 error=False
#             )
#         else:
#             return DBConnectResponceModel(
#                 message=f'Соединение не установлено.'
#                         f'Объект соединения: {self.conn}',
#                 error=True
#             )
#
#
#

#
# from sqlalchemy.ext.asyncio import AsyncSession
#
# class DBServices:
#     def __init__(self, db_session: AsyncSession):
#         self.db_session = db_session
#
#
#     # def show_all_databases(self):
#     #     with self.db_session.cursor() as cursor:
#
#
#
#     async def _get_list_databases(self):
