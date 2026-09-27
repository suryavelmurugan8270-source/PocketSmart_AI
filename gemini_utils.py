import os, requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://api.gemini.google/v1/generate"

def call_gemini(prompt, image=None):
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    data = {"prompt": prompt}
    if image:
        data["image"] = image
    response = requests.post(GEMINI_URL, json=data, headers=headers)
    return response.json()
