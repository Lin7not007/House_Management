import requests
from bs4 import BeautifulSoup
import json

# The function scrapes the data from HomeAdvisor Categories page
def scraping(url):

    if url is None:
        raise ValueError("url is None")

    # Get the webpage source code
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
        # Ignore the "Show More" category
        if category_titles[-1] == "Show More":
            category_titles.pop()
        # Append the super-category and its titles to the data list
        data.append({super_category_title: category_titles})
    
    return json.dumps(data, indent=4)
    
