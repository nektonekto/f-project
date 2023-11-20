from sqlalchemy.ext.asyncio import AsyncSession, async_session
from app.services.database import DBServices


async def _show_all_databases(session: AsyncSession):
    async with session.begin():
        db_action = UserServices(session)
        result = await db_action.show_all_db()