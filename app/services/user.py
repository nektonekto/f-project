from sqlalchemy import select
from db.models import User


class UserServices:
    def __init__(self, db_session):
        self.db_session = db_session

    async def get_user_by_id(self, user_id: int):
        query = select(User).where(User.users_id == user_id)
        res = await self.db_session.execute(query)
        user_list = res.fetchone()

        if user_list is not None:
            return user_list[0]