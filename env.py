# Loads all environmental variables from .env file
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_PWD = os.getenv("SENDER_EMAIL_PWD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")