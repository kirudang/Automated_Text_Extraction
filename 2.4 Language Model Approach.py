# 1. Import the necessary libraries
import openai
import os
import pandas as pd
import time

# 2. Set your API from ChatGPT account
openai.api_key = '<YOUR API KEY>'

# 3. Set up a function to get the result
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        )
    return response.choices[0].message["content"]

# 4. Create a promt from text file and our words:
question = "Read and understand the document, then help me extract 5 pieces of information including (1) First name, (2) last name, (3) date of birth, (4) address, (5) phone number  of tenants only. Here is the content of the document: ".join(text)

# 5. Query the API
response = get_completion(question)
print(response)