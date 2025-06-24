This repository aims to set up an API endpoint using FastAPI to serve applications powered by Large Language Models like GPT. FastAPI, with its performance and ease of use, provides a straightforward way to build high-performance APIs, making it an ideal choice for developers looking to integrate LLMs into their projects.

# 🧠 LLM Translator API with FastAPI

This project demonstrates how to quickly build REST API endpoints for LLM (Large Language Model) applications using **Python**, **FastAPI**, and **OpenAI GPT-4**.

We build an end-to-end translation application that takes English input and returns a French translation using OpenAI's GPT-4 model.

---

## 🚀 Project Overview

The application:

- Uses `OpenAI GPT-4` to translate English text to French.
- Wraps the logic in a FastAPI app to expose it as a **REST API endpoint**.
- Uses a `POST` method to receive English text and return translated French text.
- Can be easily extended for deployment or UI integration.

---

## 🧾 Example: Translation Function

Here's the core function using the OpenAI client:

```python
from openai import OpenAI

client = OpenAI()

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

🔧 Environment Setup
Clone the repo and navigate to the project directory.

Install dependencies:

```bash
pip install fastapi openai uvicorn python-dotenv
Create a .env file and add your API key:
```bash
OPENAI_API_KEY=your_openai_key_here

▶️ Running the Application
Use the following command to start the local server:

uvicorn app:app --reload

 Testing the API
Once running, go to http://localhost:8000/docs

Click on the /translate/ endpoint

Click "Try it out"

Enter a sentence in English

Click "Execute"

You’ll see the translated French text in the response

📌 Why FastAPI?
User-friendly: Includes Swagger UI docs for testing

High performance: Based on Starlette and Pydantic

Easy integration: Works great with modern Python tooling

✅ Conclusion
This project showed how to:

Use GPT-4 to translate text

Wrap that logic in a REST API using FastAPI

Provide a clean interface for others to consume your model via the web

This architecture makes it easier for others (developers, products, services) to interact with your LLM applications in a scalable and accessible way.