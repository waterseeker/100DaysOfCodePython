import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_email_2 = os.getenv("MY_EMAIL_2")
password = os.getenv("EMAIL_PASSWORD")
receiving_email = os.getenv("RECEIVING_EMAIL")
smtp_address = os.getenv("SMTP_ADDRESS")
smtp_address_2 = os.getenv("SMTP_ADDRESS_2")
app_password = os.getenv("APP_PASSWORD")

weekday = dt.datetime.now().weekday()

# Check if it's Monday
if weekday == 0:
    # if it is, grab a random quote from quotes.txt
    with open("quotes.txt", "r") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        print(random_line)
# and e-mail it to yourself
    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email_2,
                            msg=f"Subject:Happy Monday!\n\n{random_line}")
