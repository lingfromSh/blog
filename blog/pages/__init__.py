from fastapi import APIRouter
from .pages import router as page_router

router = APIRouter()
router.include_router(page_router)
