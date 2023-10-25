from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from database import get_database_session
from models import UserModel
from schema import User

user_router = APIRouter(prefix="/user")


@user_router.post("/create")
async def create_user(
    user_to_create: User,
    database_session=Depends(get_database_session),
):
    created_user = UserModel(username=user_to_create.username)
    database_session.add(created_user)

    return Response(status_code=200)


@user_router.get("/get/{user_id}")
async def get_user(
    user_id: int, database_session: AsyncSession = Depends(get_database_session)
):
    query = select(UserModel).where(UserModel.id == user_id)
    result = await database_session.execute(query)
    user_result = result.scalar_one_or_none()

    if user_result is None:
        return Response(status_code=404)

    return User(username=user_result.username)
