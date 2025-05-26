from fastapi import FastAPI
import uvicorn
from fastapi.exceptions import RequestValidationError
from containers import Container
from starlette.responses import JSONResponse
from fastapi.requests import Request
from user.interface.controllers.user_controller import router as user_routers
import user.interface.controllers.user_controller as user_controller_module

app = FastAPI()
container = Container()
"""
현재 이렇게 해줘야 해결이 되는거 같다
나중에 lifespan 설정해서 하는 방법도 찾아보자.
"""
container.wire(modules=[user_controller_module])
app.container = container
app.include_router(user_routers)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content=exc.errors()
    )


@app.get("/")
def hello():
    return {"Hello": "FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)