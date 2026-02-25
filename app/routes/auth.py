from fastapi import APIRouter, HTTPException
from app.models.auth import LoginRequest
from app.services.auth_service import authenticate_user

router = APIRouter()

@router.post('/login')
def login(request: LoginRequest):
    user = authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
