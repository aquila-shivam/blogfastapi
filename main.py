from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333333;
                text-align: center;
            }
            p {
                color: #666666;
                text-align: center;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My FastAPI App</h1>
            <p>This is a zupay assesment.</p>
            <p>Check out our <a href="/docs">API Documentation to test api's</a>.</p>
        </div>
    </body>
    </html>
    """

# Include Routers
app.include_router(auth_router, prefix="", tags=["auth"])
app.include_router(blog_router, prefix="", tags=["blogs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
