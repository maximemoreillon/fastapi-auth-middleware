from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from authMiddleware import AuthMiddleware

url = 'https://api.authentication.maximemoreillon.com/whoami'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    AuthMiddleware,
    options={"url": url}
)

@app.get("/")
async def root():
    return {
    "application_name": "Authentication middlware experiment",
    }
