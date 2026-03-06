import os
import openai

# Properly loaded from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY")

def get_completion(prompt):
    return openai.ChatCompletion.create(model="gpt-4", messages=[{"role":"user","content":prompt}])
