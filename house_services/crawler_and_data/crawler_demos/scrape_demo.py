import requests
from bs4 import BeautifulSoup
import json

# Make a GET request to the URL of the webpage
url = "https://www.homeadvisor.com/category/startRequest.html"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with class "super-category-container"
super_categories = soup.find_all("div", class_="super-category-container")

# Create an empty list to store the categories and their titles
data = []

# Loop through each super-category
for super_category in super_categories:
    # Extract the text content of the super-category title
    super_category_title = super_category.find("a", class_="super-category").text
    # Find all elements with class "category" under the super-category
    categories = super_category.find_all("a", class_="category")
    # Create a list to store the titles of the categories
    category_titles = [category.text for category in categories]
    # Append the super-category and its titles to the data list
    data.append({"super_category": super_category_title, "categories": category_titles})

# Write the data to a JSON file
with open("categories.json", "w") as f:
    json.dump(data, f)
