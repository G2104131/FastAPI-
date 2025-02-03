from fastapi import APIRouter, Depends
from src.blog1 import blog_schemas, blog_models
from src.utils.db import get_db
from src.utils.hashing import Hash
from sqlalchemy.orm import session, joinedload
from ..repository import user

user_router = APIRouter(prefix="/user",
                        tags = ["Users"])



@user_router.post("/", response_model=blog_schemas.ShowUser)
def create_user(request : blog_schemas.User, db : session= Depends(get_db)):
    return user.create(request, db, Hash)

@user_router.get("/{id}")
def get_user(id : int, db : session = Depends(get_db)):
    return user.get(db, id)
