from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

class PublicController():
    def top(request):
        return templates.TemplateResponse(
            "top.html",
            {
                "request": request,
            }
        )
