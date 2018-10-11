import requests
import json
from pprint import pprint

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
options = Options()
options.set_headless(headless=True)

#Perform a GET request to retrieve the featured LTKs
url = "https://prod-api-gateway.rewardstyle.com/api/ltk/v2/ltks/"
querystring = {"featured":"True"}
headers = {
    'Authorization': "Bearer bJ1YyRosK1AS1xF6rgBbIrP10ReOAQ",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, headers=headers, params=querystring)
jsonResponse = json.loads(response.text)

print("Status Code: " + str(response.status_code))
print(str(len(jsonResponse["ltks"])) +" ltks were successfully fetched.")

# This list will contain all the product ids from the featured page
product_list = []
for item in jsonResponse["ltks"]:
    product_list.append(item["product_ids"])

url = "https://prod-tyk.rewardstyle.com/api/ltk/v2/products/"

# This list will contain all the hyperlinks for the products from featured
hyperlink_list = []

# For each product id, perform a GET request on the products endpoint to grab the rstyle link
for x in product_list:
    #print(x)
    querystring = {"ids[]": x, "": ""}

    headers = {
        'Authorization': "Bearer KisYtXp7RV7fZKHHOKVDe9zG3vMbcS",
        'X-RS-AUTH': "application/json",
        'cache-control': "no-cache",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    jsonResponse = json.loads(response.text)
    for item in jsonResponse["products"]:
        hyperlink_list.append(item["hyperlink"])
    #pprint(json.loads(response.text))

url="C:\\Users\\DDF Employee\\Browser_Drivers\\geckodriver.exe"
driver=webdriver.Firefox(firefox_options=options, executable_path=r'C:\\Users\\DDF Employee\\Browser_Drivers\\geckodriver.exe')
driver.set_page_load_timeout(30)

import io
with io.open("featured_data.txt", "w", encoding="utf-8") as f:
    for x in hyperlink_list:
     driver.get(x)
     f.write(driver.title +"\n")
     driver.refresh()
     f.write(driver.current_url +"\n"+"\n")


driver.close()