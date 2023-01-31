import requests
import json
from bs4 import BeautifulSoup

url = "https://www.homeadvisor.com/category/startRequest.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())


# Find all categories
categories = soup.find_all("a", class_="super-category")
# print(categories)

# Create an empty list to store categories and titles
data = []

# Iterate through each category
for category in categories:
    category_name = category.find("h5").text
    titles = category.find_all("li")
    category_data = {"category_name": category_name, "titles": []}
    # Iterate through each title
    for title in titles:
        category_data["titles"].append(title.text)
    data.append(category_data)

# Write the data to a JSON file
with open("data.json", "w") as file:
    json.dump(data, file)

#/html/body/div[2]/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul/li[1]/a
# /html/body/div[2]/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul/li[2]/a