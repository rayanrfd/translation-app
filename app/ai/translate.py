from transformers import pipeline
import app.config as config
from functools import lru_cache

@lru_cache
def load_translator():
    translator = pipeline("translation", config.MODEL_CHECKPOINT)
    return translator
