import json

# Open the file
with open("/Users/dongbinlin/Desktop/House_Management/house_services/crawler_and_data/workers_and_roles/categories_and_workers.json", "r") as json_file:
    # Load the JSON data from the file
    data = json.load(json_file)

# create a set to store all job titles in json file
job_titles = set()

# loop through data, and get all job titles
for category in data:
    for worker in data["workers"]:
        job_titles.add(worker["job_title"])

# print all job titles
print(job_titles)

