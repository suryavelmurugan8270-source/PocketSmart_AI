from fastapi import UploadFile
from gemini_utils import call_gemini

def init_routes(app):

    @app.post("/generate-home")
    def generate_home(budget: int, room: str):
        prompt = f"Suggest home interior items for {room} under {budget} INR"
        return {"recommendations": call_gemini(prompt)}

    @app.post("/generate-party")
    def generate_party(budget: int, guests: int, event_type: str):
        prompt = f"Plan a {event_type} party for {guests} guests under {budget} INR"
        return {"recommendations": call_gemini(prompt)}

    @app.post("/generate-jewelry")
    def generate_jewelry(budget: int, occasion: str, image: UploadFile = None):
        img_data = image.file.read() if image else None
        prompt = f"Suggest jewelry for {occasion} under {budget} INR"
        return {"recommendations": call_gemini(prompt, image=img_data)}

    @app.post("/login")
    def login(username: str, password: str):
        return {"message": f"User {username} logged in"}

    @app.post("/register")
    def register(username: str, password: str):
        return {"message": f"User {username} registered"}
