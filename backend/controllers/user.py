from fastapi.responses import JSONResponse


def users(self):
    return JSONResponse(content={"data": "ok"})
