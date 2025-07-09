from fastapi import APIRouter
from app.model.translation import SourceLanguage, TargetLanguage
from app.ai.translate import load_translator

router = APIRouter()

translator = load_translator()

@router.post("/", response_model=TargetLanguage)
def translate(source: SourceLanguage):
    translated_text = translator(source.text)[0]["translation_text"]
    return TargetLanguage(text=translated_text)
