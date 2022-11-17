from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


class GameModeController():
    def index(request):
        return templates.TemplateResponse(
            "game-mode.html",
            {
                "request": request,
            }
        )
