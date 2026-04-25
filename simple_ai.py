from langchain.chat_models import init_chat_model
from env import GOOGLE_API_KEY

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )
