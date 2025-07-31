from fastapi import APIRouter
from app.schemas.translation import Translation
from app.ai.translate import load_translator

translate_router = APIRouter()

translator = load_translator()

@translate_router.post("/")
def translate(source: Translation):
    translated_text = translator(source.text)[0]["translation_text"]
    return 0
