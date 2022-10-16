
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import user,post,auth,vote
from .config import settings
#alembic creating table and column
# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = [
    "https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#request from url '/'
my_posts = [{"title":"title of post 1","content":"content if post 1","id":2},{"title":"favorite foods","content":"I like pizza","id":1}]

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to API!!"}

