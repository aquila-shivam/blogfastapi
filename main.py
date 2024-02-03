# main.py
from fastapi import FastAPI
from api.auth import router as auth_router
from api.blog import router as blog_router

app = FastAPI()

app.include_router(auth_router, prefix="", tags=["auth"])
app.include_router(blog_router, prefix="", tags=["blogs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


