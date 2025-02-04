from fastapi import FastAPI
from src.blog1 import blog_models
import uvicorn

# ! Database
from src.utils.db import engine

#? routers
from src.blog1.Routes.authentication import authentication_router
from src.blog1.Routes.blog_routers import blog_router
from src.blog1.Routes.user_routers import user_router

app = FastAPI()

blog_models.Base.metadata.create_all(bind = engine)

# ? include routers
app.include_router(authentication_router)
app.include_router(blog_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1" , port = 8000 )