from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JWTError
import httpx

from sqlalchemy.orm import Session
from app.crud.user import get_user, create_user
from app.db.database import get_db
from app.schemas.user import UserCreate

from app.core.config import settings

token_auth_scheme = HTTPBearer()


async def get_auth0_public_key():
    url = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        jwks = resp.json()
    return jwks


async def verify_token(
    token: HTTPAuthorizationCredentials = Depends(token_auth_scheme),
):
    try:
        jwks = await get_auth0_public_key()
        unverified_header = jwt.get_unverified_header(token.credentials)
        rsa_key = next(
            (key for key in jwks["keys"] if key["kid"] == unverified_header["kid"]),
            None,
        )

        if not rsa_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        payload = jwt.decode(
            token.credentials,
            rsa_key,
            algorithms=settings.ALGORITHMS,
            audience=settings.AUTH0_AUDIENCE,
            issuer=f"https://{settings.AUTH0_DOMAIN}/",
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


async def get_or_create_user(payload: dict, db: Session):
    user_id = payload["sub"]
    db_user = get_user(db, user_id)
    if not db_user:
        user_data = UserCreate(name=payload.get("name", ""))
        db_user = create_user(db, user_id, user_data)
    return db_user


async def verify_token_and_get_user(
    token: HTTPAuthorizationCredentials = Depends(token_auth_scheme),
    db: Session = Depends(get_db),
):
    payload = await verify_token(token)
    user = await get_or_create_user(payload, db)
    return user
