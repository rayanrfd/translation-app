from fastapi import APIRouter
import app.routes.translate as translate

router = APIRouter()
router.include_router(translate.router, prefix="/translate", tags=["translate"])
