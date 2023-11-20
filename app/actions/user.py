from sqlalchemy.ext.asyncio import AsyncSession, async_session
from app.services.user import UserServices
from app.schemas import ShowUser


async def _get_user_by_id(user_id: int, session: AsyncSession):
    async with session.begin():
        user_action = UserServices(session)
        user = await user_action.get_user_by_id(
            user_id=user_id
        )
        if user is not None:
            return ShowUser(
                user_id=user.users_id,
                user_name=user.users_name,
                user_last_name=user.users_last_name,
                user_email=user.users_email,
                user_password=user.users_password
            )
