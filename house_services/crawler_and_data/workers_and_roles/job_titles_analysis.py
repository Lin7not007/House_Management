import json

# Open the file
with open("/Users/dongbinlin/Desktop/House_Management/house_services/crawler_and_data/workers_and_roles/categories_and_workers.json", "r") as json_file:
    # Load the JSON data from the file
    data = json.load(json_file)

# Access each element of the JSON data
for category in data:
    
