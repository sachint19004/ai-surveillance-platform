from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.account import Account
from app.api.dependencies import get_current_user
from app.database.session import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.services.auth.auth_service import create_account
from app.schemas.account import (
    AccountCreate,
    AccountLogin,
    AccountResponse,
    TokenResponse,
)

from app.services.auth.auth_service import (
    create_account,
    login_account,
)

#testing
from app.core.authorization import require_admin


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=AccountResponse,
    status_code=201,
)
def register(
    account: AccountCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_account(db, account)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    
@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    account: AccountLogin,
    db: Session = Depends(get_db),
):
    try:
        return login_account(
            db,
            account.email,
            account.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )
    
@router.get(
    "/me",
    response_model=AccountResponse,
)
def get_me(
    current_user: Account = Depends(get_current_user),
):
    return current_user

#testing
@router.get("/admin-test")
def admin_test(
    current_user: Account = Depends(require_admin),
):
    return {
        "message": "Welcome Admin"
    }