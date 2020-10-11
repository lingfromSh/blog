from fastapi.templating import Jinja2Templates

########################
#     SITE SECRET
########################

SECRET_KEY = "/miYgoSd07eD/+BbQqFx4RUTaSZgVt9+FaVIBTR6Y8UXEIValHnyCxJI7sy+AgLk"

########################
#    INIT DATABASE
########################

DATABASE_SETTINGS = {"type": "sqlite", "url": "blog.db"}

########################
#     APPLICATION
########################

app = "conf.application:app"

#########################
#      Templates
#########################

from jinja_markdown import MarkdownExtension

templates = Jinja2Templates(directory="template")
templates.env.add_extension(MarkdownExtension)