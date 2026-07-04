from sqlalchemy.orm import Session

from app.models.account import Account
from app.schemas.account import AccountCreate
from app.services.auth.password import hash_password


def create_account(db: Session, account: AccountCreate) -> Account:
    # Check duplicate email
    existing = db.query(Account).filter(Account.email == account.email).first()

    if existing:
        raise ValueError("Email already registered")

    # Check duplicate username
    existing = db.query(Account).filter(Account.username == account.username).first()

    if existing:
        raise ValueError("Username already exists")

    user = Account(
        username=account.username,
        email=account.email,
        hashed_password=hash_password(account.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user