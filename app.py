import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client with your API key
client = OpenAI()

# Initialize FastAPI client
app = FastAPI()

class TranslationRequest(BaseModel):
    input_str: str

def translate_text(input_str):
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
                "role": "system",
                "content": "You are an expert translator who translates text from english to french and only return translated text",
            },
            {"role": "user", "content": input_str},
        ],
    )

    return completion.choices[0].message.content

@app.post("/translate/")  # This line decorates 'translate' as a POST endpoint
async def translate(request: TranslationRequest):
    try:
        # Call your translation function
        translated_text = translate_text(request.input_str)
        return {"translated_text": translated_text}
    except Exception as e:
        # Handle exceptions or errors during translation
        raise HTTPException(status_code=500, detail=str(e))

# test the function
# print(translate_text("this is a test string to translate"))



#How to run this file:
# uvicorn app:app --reload

