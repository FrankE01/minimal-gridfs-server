from fastapi import FastAPI
from api.v1.routes import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
