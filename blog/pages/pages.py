from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from conf import settings
from core import exceptions
from sql.crud import get_posts_of_user

router = APIRouter()
templates = settings.templates


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    print(request)
    posts = get_posts_of_user(user_id=1)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "posts": [{"id": 1, "title": "数字电路", "summary": "Hello,World!"}],
        },
    )


@router.get("/post/{id}", response_class=HTMLResponse)
async def post(request: Request):
    return templates.TemplateResponse(
        "post.html",
        {
            "request": request,
            "post": {
                "id": 1,
                "title": "数字电路",
                "summary": "Hello,World!",
                "content": "XXX",
            },
        },
    )