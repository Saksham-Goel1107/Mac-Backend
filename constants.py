from dotenv import load_dotenv
import os
load_dotenv()

ENV = os.getenv("ENV", "development")
SERVER_URL = os.getenv("SERVER_URL", "localhost")
PORT = int(os.getenv("PORT", 8000))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")