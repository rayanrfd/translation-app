from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.router import router as process_router
from transformers import pipeline

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

app.include_router(process_router)

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
