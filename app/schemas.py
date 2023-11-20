from pydantic import BaseModel


class DBConnectModel(BaseModel):
    database: str
    user: str
    password: str
    host: str = 'localhost'
    port: int = 5432


class DBConnectResponceModel(BaseModel):
    message: str
    error: bool


class ShowUser(BaseModel):
    user_id: int
    user_name: str
    user_last_name: str
    user_email: str
    user_password: str