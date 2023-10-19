from pydantic import BaseModel


class DBConnectModel(BaseModel):

    # __slots__ = ('database', 'user', 'password', 'host', 'port')

    database: str
    user: str
    password: str
    host: str = 'localhost'
    port: int = 5432


class DBConnectResponceModel(BaseModel):
    message: str
    error: bool
