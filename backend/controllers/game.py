from jinja import templates


class GameController():
    def index(request):
        return templates.TemplateResponse(
            "game.html",
            {
                "request": request,
            }
        )
