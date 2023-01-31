import json

# Load the JSON file
with open('/Users/dongbinlin/Desktop/House_Management/labors_and_roles/categories.json', 'r') as f:
    data = json.load(f)

# Format the JSON file
formatted_json = json.dumps(data, indent=4)

# Save the formatted JSON file
with open('formatted_file.json', 'w') as f:
    f.write(formatted_json)
