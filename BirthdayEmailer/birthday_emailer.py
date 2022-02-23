import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random
import pandas as pd

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_email_2 = os.getenv("MY_EMAIL_2")
password = os.getenv("EMAIL_PASSWORD")
receiving_email = os.getenv("RECEIVING_EMAIL")
smtp_address = os.getenv("SMTP_ADDRESS")
smtp_address_2 = os.getenv("SMTP_ADDRESS_2")
app_password = os.getenv("APP_PASSWORD")

now = dt.datetime.now()
current_day = float(now.day)
current_month = float(now.month)
df = pd.read_csv("birthdays.csv")
df.reset_index()
# Check if today matches a birthday in the birthdays.csv
for index, row in df.iterrows():
    if row['month'] == current_month and row['day'] == current_day:
        birthday_name = row['name'].title()
        birthday_email = row['email']
        random_file = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{random_file}", "r") as letter:
            letter_text = letter.read()
            name_added = letter_text.replace("[NAME]", birthday_name)
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_email,
                                msg=f"Happy Birthday {birthday_name}!\n\n{name_added}")
