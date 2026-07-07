from fastapi import Depends, HTTPException, status

from app.api.dependencies import get_current_user
from app.models.account import Account


def require_admin(
    current_user: Account = Depends(get_current_user),
):
    if current_user.role.value != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )

    return current_user


def require_security(
    current_user: Account = Depends(get_current_user),
):
    if current_user.role.value not in ["admin", "security"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Security privileges required",
        )

    return current_user