import os
from dotenv import load_dotenv

load_dotenv()

# Config class for the project
class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = "gpt-4o"
    MAX_TOKENS = 300
    TRANSCRIPT_LIMIT = 3500