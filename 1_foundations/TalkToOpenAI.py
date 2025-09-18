from dotenv import load_dotenv
import os
# Yes, this is from the openai package.
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv("OPEN_API_KEY")

# Yes, OpenAI is a class from the openai package.
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Need to test the someones IQ. please help me with the question"}]
)

question = response.choices[0].message.content
print('question', question)

answer = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": question,  'task': "please answer the question in a way that is easy to understand"}]
)

print('answer', answer.choices[0].message.content)