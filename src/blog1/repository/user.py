from sqlalchemy.orm import session, joinedload
from src.blog1 import blog_models,blog_schemas
from src.utils.hashing import Hash


def create(request: blog_schemas.User, db : session , Hash):
    new_user = blog_models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password), address = request.address, phone = request.phone, code = request.code)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def get(db : session, id : int):
    user = db.query(blog_models.User).options(joinedload(blog_models.User.blogs)).filter(blog_models.User.id == id).first()
    db.commit()
    db.refresh(user)
    return user
