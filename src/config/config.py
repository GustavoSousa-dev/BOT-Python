from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    WHAPI_BASE_URL = "https://gate.whapi.cloud"
    WHAPI_TOKEN = os.getenv("WHAPI_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")

config = Config()