# main.py
from fastapi import FastAPI
from api.auth import router as auth_router
from api.blog import router as blog_router

app = FastAPI()

# Welcome Page Route
@app.get("/", response_class=HTMLResponse)
async def welcome_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to My FastAPI App</title>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>This is a FastAPI application.</p>
        <p>Check out our <a href="/docs">API Documentation</a>.</p>
    </body>
    </html>
    """

app.include_router(auth_router, prefix="", tags=["auth"])
app.include_router(blog_router, prefix="", tags=["blogs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


