import requests

response = requests.get("http://api.open-notify.org/iss-now")
# this only returns the response code

# response codes generally follow the pattern:
# 1XX: Hold On, processing, waiting for something
# 2XX: Success, here you go
# 3XX: Go Away
# 4XX: You Screwed Up, resource doesn't exist
# 5XX: I (the server) Screwed Up, internal error

# you can raise exceptions for statuses by using
response.raise_for_status()
# you access the actual data from the response by using
data = response.json()
# you can manipulate this like any python dictionary
# access a specific key
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = {longitude, latitude}
