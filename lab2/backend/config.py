import os
from dotenv import load_dotenv

# Încarcă variabilele din .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    MQTT_BROKER = os.getenv("MQTT_BROKER")
    MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))  # Conversie în int
    MQTT_TOPIC = os.getenv("MQTT_TOPIC")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
