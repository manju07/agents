from dotenv import load_dotenv
import os
from google import genai

load_dotenv(override=True)
gemini_api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=gemini_api_key)

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=["What is 2+2?"]
)

print(response.text)

messages = [
    {"role": "user", "content": "pick a business area that might be worth exploring for an Agentic AI opportunity."}
]

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=messages[0]["content"]
)

industry = response.text

messages = [
    {
        'role': 'user',
        'content': industry + ' a pain-point in that industry and something challenging that might be ripe for an Agentic solution '
    }
]
print('industry', industry)

            # <span style="color:#ff7800;">Now try this commercial application:<br/>
            # First ask the LLM to pick a business area that might be worth exploring for an Agentic AI opportunity.<br/>
            # Then ask the LLM to present a pain-point in that industry - something challenging that might be ripe for an Agentic solution.<br/>
            # Finally have 3 third LLM call propose the Agentic AI solution.
            # </span>

answer = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=messages[0]['content']
)

print('answer', answer.text)

agentic_solution = client.models.generate_content(
    model="gemini-1.5-flash",
    contents= answer.text + ' propose the Agentic AI solution.'
)

print('agentic_solution', agentic_solution.text, end="\n\n")