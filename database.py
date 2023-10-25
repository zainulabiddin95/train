from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession

from settings import settings

async_engine: AsyncEngine = create_async_engine(
    url=settings.async_database_url,
    pool_pre_ping=True,
)


async def get_database_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(bind=async_engine) as async_session:
        async with async_session.begin():
            yield async_session
