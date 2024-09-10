from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import verify_token_and_get_user
from app.crud.user import update_user
from app.schemas.user import UserUpdate, UserInDB
from app.db.database import get_db

router = APIRouter()


@router.get("/me", response_model=UserInDB)
async def read_user_me(current_user: UserInDB = Depends(verify_token_and_get_user)):
    return current_user


@router.put("/me", response_model=UserInDB)
async def update_user_me(
    user_update: UserUpdate,
    current_user: UserInDB = Depends(verify_token_and_get_user),
    db: Session = Depends(get_db),
):
    updated_user = update_user(db, current_user.id, user_update)
    return updated_user
