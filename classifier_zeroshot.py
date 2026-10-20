import os
import json
from google import genai


api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY is not set. Run: export GEMINI_API_KEY='your-key-here'")

client = genai.Client(api_key=api_key)

text = input("Enter text to classify: ")


prompt = f"""Classify the following text into one of these categories: complaint, inquiry, praise.
Return ONLY JSON in this exact format: {{"category": "...", "confidence": 0.0}}

Text: {text}"""


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
)


try:
    result = json.loads(response.text)
    print("Category:", result["category"])
    print("Confidence:", result["confidence"])
except json.JSONDecodeError:
    print("Error: the model did not return valid JSON")
    print("Raw response:", response.text)
