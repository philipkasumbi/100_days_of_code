import requests
from datetime import  datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
ID = "graph1"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":ID,
    "name":"pages graph",
    "unit":"pages",
    "type":"int",
    "color":"shibafu"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
today = datetime.now()
post_graph_endpoint_configs = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many pages did you read today? ")
}

response = requests.post(url=post_graph_endpoint,json=post_graph_endpoint_configs,headers=headers)
print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20260615"
put_configs ={
    "quantity":"12"
}

# response = requests.put(url=put_endpoint,json=put_configs,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20260615"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response)


