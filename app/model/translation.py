from pydantic import BaseModel

class SourceLanguage(BaseModel):
    text: str

class TargetLanguage(BaseModel):
    text: str
