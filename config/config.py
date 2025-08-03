import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv('groq_api_key')
HUGGIGFACEHUB_API_KEY=os.getenv('Huggingface_api_key')
model_name='llama-3.1-8b-instant'