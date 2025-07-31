from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.translate import translate_router
from app.routes.user import user_router
from app.routes.token import token_router
from transformers import pipeline

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

app.include_router(translate_router, prefix="/translate", tags=["translate"])
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(token_router, prefix="/token", tags=["token"])

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
