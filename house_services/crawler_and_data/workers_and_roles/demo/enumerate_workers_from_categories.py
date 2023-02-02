import json

# Load the JSON data from a file
with open('/Users/dongbinlin/Desktop/House_Management/house_services/crawler_and_data/workers_and_roles/categories_and_workers_demo.json', 'r') as file:
    data = json.load(file)

# Create a set to store the unique worker titles
worker_titles = set()

# Loop through the dictionaries in the list
for d in data:
    # Loop through the workers in each dictionary
    for worker in d['workers']:
        # Add the worker title to the set
        worker_titles.add(worker)

# The set of unique worker titles is stored in the variable "worker_titles"
# print(sort(worker_titles))

# Print worker titles in alphabetical order
'''
output_display = list(worker_titles)
output_display.sort()
print(output_display)
print(len(output_display))
'''

worker_list = [{worker: None} for worker in worker_titles]
# save worker_list as a JSON file in a readable format
with open('/Users/dongbinlin/Desktop/House_Management/house_services/crawler_and_data/workers_and_roles/worker_list.json', 'w') as file:
    json.dump(worker_list, file, indent=4)




'''
for item in worker_list:
    # get key of each item to store servies later
    for key in item:
        # open another json file and read the data
        # [{}, {}, {}, {}......]
'''