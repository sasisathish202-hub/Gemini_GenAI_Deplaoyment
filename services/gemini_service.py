from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("Full Gemini Response:", response)

    answer = response.text

    if not answer:
        return "Gemini response empty-ah irukku. PowerShell output check pannunga."

    return answer