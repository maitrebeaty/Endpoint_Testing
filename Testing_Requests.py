import requests
import json
from pprint import pprint
import time
import datetime

url = "https://prod-tyk.rewardstyle.com/api/ltk/v2/likes/"

headers = {
    'Authorization': "Bearer KisYtXp7RV7fZKHHOKVDe9zG3vMbcS",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    #'Postman-Token': "b0a3c7fc-4702-4df7-8a87-cc485c77b629"
    }

response = requests.request("GET", url, headers=headers)
jsonResponse = json.loads(response.text)
print(type(response.status_code))
counter = 1;
while(counter<100):
    response = requests.request("GET", url, headers=headers)
    pprint(response.status_code)
    if(response.status_code != 200):
        print("THERE MIGHT BE A PROBLEM HERE")
    print(datetime.datetime.now())
    counter+=1
    time.sleep(30)

# This is literally a dictionary where each element is a list and each element of THAT list is another dictionary
#print(type(jsonResponse))
#print(type(jsonResponse["likes"]))
#print(type(jsonResponse["likes"][1]))
#print(jsonResponse["likes"][1]["like_type"])

# This will print the entire response in json format
#pprint(json.loads(response.text))

