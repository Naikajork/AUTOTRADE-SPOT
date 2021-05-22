import os
API_BINANCE_KEY = os.getenv("API_BINANCE_KEY")
API_BINANCE_SECRET = os.getenv("API_BINANCE_SECRET")

API_LINE_KEY = os.getenv("API_LINE_KEY")
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")

LINE_BOT_ACCESS_TOKEN = os.getenv("LINE_BOT_ACCESS_TOKEN")
LINE_BOT_CHANNEL_SECRET = os.getenv("LINE_BOT_CHANNEL_SECRET")

from firebase import Firebase

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "bottrading-databse.firebaseapp.com",
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": "bottrading-databse",
    "storageBucket": "bottrading-databse.appspot.com",
    "messagingSenderId": "1091910107557",
    "appId": "1:1091910107557:web:1606a1ddaa97fbc530284c"
  }

firebaseClient = Firebase(firebaseConfig)
auth = firebaseClient.auth()
user = auth.sign_in_with_email_and_password(os.getenv("FIREBASE_EMAIL_AUTH"),os.getenv("FIREBASE_PASSWORD"))

i
