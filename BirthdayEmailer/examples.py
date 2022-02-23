import smtplib
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_email_2 = os.getenv("MY_EMAIL_2")
password = os.getenv("EMAIL_PASSWORD")
receiving_email = os.getenv("RECEIVING_EMAIL")
smtp_address = os.getenv("SMTP_ADDRESS")
smtp_address_2 = os.getenv("SMTP_ADDRESS_2")
app_password = os.getenv("APP_PASSWORD")

# with smtplib.SMTP(smtp_address) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=my_email_2,
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# with smtplib.SMTP(smtp_address_2) as connection:
#     connection.starttls()
#     connection.login(user=my_email_2, password=app_password)
#     connection.sendmail(from_addr=my_email_2, to_addrs=my_email, msg="Subject:Hello from 2\n\nHey from over here.")

# getting info from a datetime
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
day_of_week = now.weekday()  # returns a number. 0=Mon, 1=Tue, etc

# creating a datetime
date_of_birth = dt.datetime(year=1912, month=10, day=31)
print(date_of_birth)
