from fastapi import APIRouter, Depends, HTTPException, status
from .. import blog_schemas, blog_models, token 
from src.utils import db
from sqlalchemy.orm import session
from src.utils.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


authentication_router = APIRouter(
    tags = ["Authentication"]
)

@authentication_router.post("/login")
def login(request : OAuth2PasswordRequestForm = Depends() , db : session = Depends(db.get_db)):
    user = db.query(blog_models.User).filter(blog_models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = "invalid credentials")
    if not  Hash.verify(user.password , request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "incorrect password.")
    
    access_token = token.create_access_token(data = {"sub":user.email})
    return {"access_token" : access_token, "token_type" : "bearer"}