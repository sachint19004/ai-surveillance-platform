from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.services.auth.auth_service import create_account

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