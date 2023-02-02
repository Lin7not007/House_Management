
import json

# load the JSON file of house services and their required workers
with open('/Users/dongbinlin/Desktop/House_Management/house_services/crawler_and_data/workers_and_roles/relation_just_testing.json', 'r') as f:
    roleToWorker = json.load(f)

# load the JSON file of worker and their roles
with open('/Users/dongbinlin/Desktop/House_Management/house_services/crawler_and_data/workers_and_roles/worker_dict.json', 'r') as f:
    workerToRole = json.load(f)

# a list for display workers
display = []
# get a list of workers titles
for item in workerToRole:
    tempo = list(item)
    display.append(tempo[0])
display.sort()

# use the dict to store the result
output_dict = {}
# loop throught display list, 
# for each woker, set it as a key in output_dict with a list as the value.
# Then, loop throught roleToWorker, 
# in its inner dict value, if the value list contains the worker, then add the key into worker's list.
for worker in display:
    output_dict[worker] = []
    for key, value in roleToWorker.items():
        for inner_key, inner_value in value.items():
            if worker in inner_value:
                output_dict[worker].append(inner_key)



# save the result to a JSON file
with open('worker_and_their_roles.json', 'w') as f:
    json.dump(output_dict, f, indent=4)

