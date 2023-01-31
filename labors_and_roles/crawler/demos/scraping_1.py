
import requests
from lxml import etree
import time  

# Get the webpage source code
url = "https://www.homeadvisor.com/category/startRequest.html"
headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}
response = requests.get(url, headers=headers).text
# print(response)

# Parse the HTML source code using etree
html = etree.HTML(response)
divs = html.xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul/li")  
print(divs)
'''
for div in divs:
    category = div.xpath("")[0]
    print(category)
    time.sleep(1)
'''
# /html/body/div[2]/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul/li[2]/a