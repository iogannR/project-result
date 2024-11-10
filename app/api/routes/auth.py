import logging

from fastapi import APIRouter, Response
from dishka.integrations.fastapi import FromDishka, inject

from app.application.dto.user_dto import LoginUserRequest
from app.application.use_cases.auth_use_cases import CreateAccessTokenUseCase, LoginUserUseCase


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=str)
@inject
async def login_user(
    request: LoginUserRequest,
    user_auth_use_case: FromDishka[LoginUserUseCase],
    create_access_token_use_case: FromDishka[CreateAccessTokenUseCase],
    response: Response,
):
    logger.info("Entering...")
    user = await user_auth_use_case(request)
    if user:
        access_token = await create_access_token_use_case(user.id)
        response.set_cookie(
            key="access_token",
            value=f"Bearer: {access_token}",
            httponly=True,
        )
        return access_token