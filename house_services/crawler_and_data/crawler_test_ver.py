import requests
from bs4 import BeautifulSoup
import json


# Get the webpage source code
url = "https://www.homeadvisor.com/category/startRequest.html"
headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


# There are 3 super-category-containers on the webpage
super_categories = soup.find_all("div", class_="super-category-container")
data = []

# Loop through each super-category-container
for super_category in super_categories:
    # Get super-category title, and all sub-categories
    super_category_title = super_category.find("a", class_="super-category").text
    categories = super_category.find_all("a", class_="category")
    # Use a list to store all sub-categories
    category_titles = [category.text for category in categories]
    # Append the super-category and its titles to the data list
    data.append({super_category_title: category_titles})

# Store the data in a JSON file
with open("categories_test.json", "w") as f:
    # json.dump(data, f)
    json.dump(data, f, indent=4)
    

