from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


class GameController():
    def index(request):
        return templates.TemplateResponse(
            "game.html",
            {
                "request": request,
            }
        )
