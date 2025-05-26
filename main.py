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
# Wire the user_controller module explicitly for dependency injection
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