from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes

app = FastAPI(title="PocketSmart AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes.init_routes(app)

@app.get("/")
def root():
    return {"message": "Welcome to PocketSmart AI"}
