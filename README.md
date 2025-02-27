# 🚀 Prompt Refinement API

## 📌 About
This is a FastAPI-based API that **refines user-provided prompts** to make them **more structured, clear, and effective** using Google Gemini AI.

## 🛠️ Installation

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/dubliramprasath/prompt-refiner-api.git
cd prompt-refiner-api
2️⃣ Create a virtual environment & activate it:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # MacOS/Linux
env\Scripts\activate  # Windows
3️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Running the API Locally
bash
Copy
Edit
uvicorn main:app --reload
Open Swagger UI: http://127.0.0.1:8000/docs
🌐 API Endpoints
Method	Endpoint	Description
POST	/refine-prompt/	Refines the given prompt using Gemini AI
📌 Example Request:
json
Copy
Edit
{
    "raw_prompt": "Write a Python script to scrape weather data.",
    "tone": "formal",
    "output_format": "markdown"
}
📡 Deployment (Render)
Sign up at Render
Deploy via GitHub: Follow the guide to host your FastAPI app.
👤 Author
Ramprasath Srinivasan
GitHub: @dubliramprasath
