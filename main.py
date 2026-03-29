import requests
from datetime import datetime
import os
from  dotenv import load_dotenv
load_dotenv()
TOKEN=os.environ.get("TOKEN")
USERNAME=os.environ.get("USERNAME")
GRAPH_ID="graph1"
PIXELA_ENDPOINT=os.environ.get("PIXELA_ENDPOINT")
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

graph_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params={
    "id":GRAPH_ID,
    "name":"Steps Graph",
    "unit":"steps",
    "type":"int",
    "color":"sora",
}
headers={
    "X-USER-TOKEN":TOKEN,
}
pixela_post_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"





print("Menu:")
print("1.Add A Pixel")
print("2.Update a Pixel")
print("3.Delete a Pixel")
print("4.Exit")
print("Enter your choice:")
choice = int(input())
while choice!=4:
    choice = int(input())
    if choice==1:
        pixela_post_params = {
            "date": datetime.now().strftime("%Y%m%d"),
            "quantity": input("How many steps did you walk today?"),
        }
        response=requests.post(url=pixela_post_endpoint,headers=headers,json=pixela_post_params)
        print(response.text)
    elif choice==2:
        date=datetime.now().strftime("%Y%m%d")
        pixela_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
        pixela_update_params = {
            "quantity": input("How many steps did you walk today?"),

        }
        response = requests.put(url=pixela_update_endpoint, json=pixela_update_params, headers=headers)
        print(response.text)
    elif choice==3:
        date=datetime.now().strftime("%Y%m%d")
        pixela_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
        response = requests.delete(url=pixela_delete_endpoint, headers=headers)
        print(response.text)











