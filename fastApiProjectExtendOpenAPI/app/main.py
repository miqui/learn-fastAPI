import os
from os import path
from pathlib import Path

from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

path_str = path.dirname(path.realpath(__file__))
#print(logger.logger.info("relative path of static folder: %s", path_str))
print(path_str)
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))

BASE_DIR2 = os.getcwd()

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=Path(BASE_DIR2, 'static')), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(

        openapi_url=app.openapi_url,

        title=app.title + " - ReDoc",

        redoc_js_url="/static/redoc.standalone.js",

    )


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hey {username}"}
