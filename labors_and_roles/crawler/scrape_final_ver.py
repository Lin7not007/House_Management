import requests
from bs4 import BeautifulSoup
import json

# get the webpage source code
url = "https://www.homeadvisor.com/category/startRequest.html"
headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

super_categories = soup.find_all("div", class_="super-category-container")
# output = super_categories.text
# print(output)
data = []

for super_category in super_categories:
    # get text content of super-category title
    super_category_title = super_category.find("a", class_="super-category").text
    # get all categories under the super-category
    categories = super_category.find_all("a", class_="category")
    # use a list to store the titles of the categories
    category_titles = [category.text for category in categories]
    # append the super-category and its titles to the data list
    data.append({"super_category": super_category_title, "categories": category_titles})

with open("categories.json", "w") as f:
    json.dump(data, f)

'''
col fourcol tabletls-fourcol
/html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]
    super-category-container
    /html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/div[1]
        super-category
        /html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/div[1]/h5/a
        caterory-list
        /html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul
            category
            /html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul/li[1]/a
            category
            /html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/div[1]/ul/li[2]/a
            .
            .
            .
            category
    super-category-container
    /html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[1]/div[2]
    .
    .
    super-category-container

col fourcol tabletls-fourcol
/html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[2]
    super-category-container
    .
    .
    super-category-container

col fourcol tabletls-fourcol
/html/body/div[2]/div/div[2]/div/div[4]/div/div/div/div[3]
    super-category-container
    .
    .
    super-category-container
'''
