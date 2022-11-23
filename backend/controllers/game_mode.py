from jinja import templates


class GameModeController():
    def index(request):
        return templates.TemplateResponse(
            "game-mode.html",
            {
                "request": request,
            }
        )
