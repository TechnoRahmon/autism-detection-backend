from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers import model_route

app = FastAPI()


app.include_router(model_route.router)

@app.get("/")
async def root():
    return RedirectResponse('/docs')
