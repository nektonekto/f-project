import psycopg2
from app.schemes.db_info_models import DBConnectResponceModel


class DBService:
    def __init__(self, data):
        self.database = data.database
        self.user = data.user
        self.password = data.password
        self.host = data.host
        self.port = data.port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except Exception as e:
            return DBConnectResponceModel(
                message=f'Ошибка подключения:{e}',
                error=True
            )
        
    def disconnect(self):
        if self.conn:
            self.conn.close()
    
    def get_db_list(self):
        if not self.conn:
            self.connect()
    
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f'SELECT * FROM pg_database')
                return {
                    'success': True,
                    'result': cursor.fetchall()
                }
        except Exception as e:
            return {
                'success': False,
                'error': {e}
            }
        
    def check_connect(self):
        if self.conn:
            return DBConnectResponceModel(
                message=f'Соединение установлено.'
                        f'Объект соединения: {self.conn}',
                error=False
            )
        else:
            return DBConnectResponceModel(
                message=f'Соединение не установлено.'
                        f'Объект соединения: {self.conn}',
                error=True
            )



