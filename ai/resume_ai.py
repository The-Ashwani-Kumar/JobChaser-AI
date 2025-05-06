import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# Working OpenRouter model — you can change to other supported models
MODEL = "mistralai/mistral-7b-instruct"

def generate_resume(jd, resume):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",     # Use your actual project domain
        "X-Title": "JobChaser AI Resume Generator"    # Any string identifier
    }

    prompt = f"Tailor the following resume to the job description below.\n\nJob Description:\n{jd}\n\nResume:\n{resume}"

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}\n\nDetails: {response.text if 'response' in locals() else 'No response'}"
    except KeyError:
        return f"Unexpected response structure: {response.text}"

# Test
if __name__ == "__main__":
    jd = "We are hiring a backend engineer with Python, Django, and PostgreSQL experience."
    resume = "Experienced developer with 3+ years in full-stack development and React."
    result = generate_resume(jd, resume)
    print(f"\nGenerated Resume:\n\n{result}")
