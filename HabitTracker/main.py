import os
from dotenv import load_dotenv
import requests

load_dotenv()
PIXELA_AUTH_TOKEN = os.getenv("PIXELA_AUTH_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"

create_user_parameters = {
    "token": PIXELA_AUTH_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # create an account
# response = requests.post(url=PIXELA_CREATE_USER_ENDPOINT, json=create_user_parameters)
# print(response.text)

# create a graph
graph_endpoint = f"{PIXELA_CREATE_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs"
graph_configuration = {
    "id": "graph1",
    "name": "Finnish Practice Graph",
    "unit": "Days",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": PIXELA_AUTH_TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
print(response.text)