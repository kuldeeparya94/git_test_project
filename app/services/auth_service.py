def authenticate_user(email: str, password: str):
    if email == "user@example.com" and password == "password123":
        return {"message": "Login successful", "email": email, "token": "mock_token_123"}
    return None
