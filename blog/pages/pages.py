from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from conf import settings
from core import exceptions
from sql.crud import get_posts_of_user, get_post
from sql.schemas import PostBase

router = APIRouter()
templates = settings.templates


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    首页
    """
    posts = get_posts_of_user(user_id=1)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "posts": [post for post in posts],
        },
    )


@router.get("/post/{id}", response_class=HTMLResponse)
async def post(request: Request, id: int):
    """
    文章详情页
    """
    post = get_post(post_id=id)
    return templates.TemplateResponse(
        "post.html",
        {"request": request, "post": post},
    )


@router.get("/post-manager/", response_class=HTMLResponse)
async def post_manager(request: Request):
    """
    文章编辑器
    """
    return templates.TemplateResponse("post-manager.html", {"request": request})
