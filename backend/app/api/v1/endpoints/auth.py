"""
Authentication endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.models.users import User

router = APIRouter()

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """User login endpoint"""
    
    # For demo purposes, create a mock user
    # In production, you would query the database
    if form_data.username == "admin" and form_data.password == "admin123":
        access_token = create_access_token(
            data={"sub": form_data.username}
        )
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "username": form_data.username,
                "role": "executive",
                "full_name": "Executive User"
            }
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

@router.get("/me")
async def get_current_user_info(
    current_user: dict = Depends(get_current_user)
):
    """Get current user information"""
    
    return {
        "user_id": current_user["user_id"],
        "username": current_user["token_data"].get("sub"),
        "role": "executive"
    } 