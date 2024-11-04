import uuid

from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, inject

from app.application.dto.user_dto import CreateUserRequest, UserResponse
from app.application.use_cases.user_use_cases import (
    CreateUserUseCase, 
    DeleteUserByIdUseCase, 
    GetAllUsersUseCase, 
    GetUserByEmailUseCase, 
    GetUserByIdUseCase,
)

router = APIRouter(tags=["Users"])


@router.post("/", response_model=UserResponse)
@inject
async def create_user(
    request: CreateUserRequest,
    create_user_use_case: FromDishka[CreateUserUseCase],
):
    return await create_user_use_case(request)


@router.get("/", response_model=list[UserResponse])
@inject
async def get_all_users(
    get_all_users_user_case: FromDishka[GetAllUsersUseCase],
):
    return await get_all_users_user_case()


@router.get("/{id_}", response_model=UserResponse)
@inject
async def get_user_by_id(
    id_: uuid.UUID,
    get_user_by_id_use_case: FromDishka[GetUserByIdUseCase],
) -> UserResponse | None:
    return await get_user_by_id_use_case(id_)


@router.get("/by-email/{email}", response_model=UserResponse)
@inject
async def get_user_by_email(
    email: str,
    get_user_by_email_use_case: FromDishka[GetUserByEmailUseCase],
) -> UserResponse | None:
    return await get_user_by_email_use_case(email)


@router.delete("/delete/{id_}")
@inject
async def delete_user_by_id(
    id_: uuid.UUID,
    delete_user_by_id_use_case: FromDishka[DeleteUserByIdUseCase],
) -> None:
    return await delete_user_by_id_use_case(id_)