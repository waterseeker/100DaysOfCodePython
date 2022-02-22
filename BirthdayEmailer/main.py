import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("MY_EMAIL")
connection = smtplib.SMTP("SMTP_ADDRESS")
