import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()
PIXELA_AUTH_TOKEN = os.getenv("PIXELA_AUTH_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = os.getenv("GRAPH_ID")

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
# graph_configuration = {
#     "id": GRAPH_ID,
#     "name": "Finnish Practice Graph",
#     "unit": "Days",
#     "type": "int",
#     "color": "shibafu",
# }
headers = {
    "X-USER-TOKEN": PIXELA_AUTH_TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

# post data to the graph
today = datetime.datetime.today()
add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

post_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "9",
}
# response = requests.post(url=add_pixel_endpoint, json=post_data, headers=headers)
# print(response.text)

# update a pixel
update_pixel_endpoint = f"{add_pixel_endpoint}/{today.strftime('%Y%m%d')}"
put_data = {
    "quantity": "90",
}
# response = requests.put(url=update_pixel_endpoint, json=put_data, headers=headers)
# print(response.text)

# delete a pixel
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
