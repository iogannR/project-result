import logging

from fastapi import APIRouter, HTTPException, Response, status
from dishka.integrations.fastapi import FromDishka, inject

from app.application.dto.user_dto import LoginUserRequest
from app.application.use_cases.auth_use_cases import LoginUserUseCase


logger = logging.getLogger(__name__)

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=str)
@inject
async def login_user(
    request: LoginUserRequest,
    user_auth_use_case: FromDishka[LoginUserUseCase],
    response: Response,
):
    logger.info("Entering...")
    access_token = await user_auth_use_case(request)
    response.set_cookie(
        key="access_token",
        value=f"Bearer: {access_token}",
        httponly=True,
    )
    return access_token