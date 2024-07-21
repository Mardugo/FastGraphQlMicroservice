from fastapi import FastAPI
from app.controller.schema import graphql_app

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def read_root():
    return {"Status": "This API is working!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info")