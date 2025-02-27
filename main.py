from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests
import json

app = FastAPI()

# ✅ Use Google Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ Google Gemini API key is missing! Set it as an environment variable.")

# ✅ Use Correct Model Name
GEMINI_MODEL = "models/gemini-1.5-pro"  # Update this based on your API key access
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/{GEMINI_MODEL}:generateContent"

class PromptRequest(BaseModel):
    raw_prompt: str
    tone: str = "neutral"
    output_format: str = "plain_text"

# ✅ New Root Endpoint to Prevent 404
@app.get("/")
def home():
    return {"message": "FastAPI is live! Visit /docs for API documentation."}

@app.post("/refine-prompt/")
async def refine_prompt(request: PromptRequest):
    try:
        print("🚀 [DEBUG] API Received Request:", request.dict())

        refined_prompt = f"""
        Refine the following user-provided prompt to make it more structured, clear, and effective:
        - Keep the tone {request.tone}.
        - Format the response as {request.output_format}.

        User's raw input:
        "{request.raw_prompt}"
        """

        print("🟢 [DEBUG] Refined Prompt Generated:", refined_prompt)

        # ✅ Google Gemini API Call
        gemini_headers = {"Content-Type": "application/json"}
        gemini_payload = {
            "contents": [{"parts": [{"text": refined_prompt}]}]
        }

        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=gemini_headers,
            json=gemini_payload,
            timeout=10
        )

        response_json = response.json()
        print("🟢 [DEBUG] Gemini API Response JSON:", json.dumps(response_json, indent=4))

        if "error" in response_json:
            print("❌ [ERROR] Gemini API Error:", response_json["error"]["message"])
            raise HTTPException(status_code=500, detail=f"Gemini API Error: {response_json['error']['message']}")

        return {"refined_prompt": response_json["candidates"][0]["content"]["parts"][0]["text"]}

    except requests.exceptions.Timeout:
        print("❌ [ERROR] Gemini API Timeout")
        raise HTTPException(status_code=500, detail="❌ Gemini API Timeout: Google API took too long to respond.")

    except requests.exceptions.RequestException as e:
        print(f"❌ [ERROR] Gemini API Connection Issue: {str(e)}")
        raise HTTPException(status_code=500, detail=f"❌ Gemini API Connection Error: {str(e)}")

    except Exception as e:
        print(f"❌ [ERROR] Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"❌ Server Error: {str(e)}")
