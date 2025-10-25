import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = genai.GenerativeModel("models/gemini-2.5-flash")

# Default parameters
DEFAULT_BOOK_PATH = "books/christmas_carol.txt"
CHUNK_SIZE = 500
