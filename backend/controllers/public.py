from jinja import templates


class PublicController():
    def top(request):
        return templates.TemplateResponse(
            "top.html",
            {
                "request": request,
            }
        )
