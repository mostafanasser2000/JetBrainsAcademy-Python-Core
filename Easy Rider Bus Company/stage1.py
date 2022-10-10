import json

json_string = input()  # take a json string from user
buses_information = json.loads(json_string)  # create dictionay using json string


bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0

#  check for requirements validation 
for item in buses_information: 
    if not item["bus_id"] or not isinstance(item["bus_id"], int):
        bus_id += 1
    if not item["stop_id"] or not isinstance(item["stop_id"], int):
        stop_id += 1
    if not item["stop_name"] or not isinstance(item["stop_name"], str):
        stop_name += 1
    if not isinstance(item["next_stop"], int):
        next_stop += 1
    if item["stop_type"] not in ["S", "O", "F", ""]:
        stop_type += 1
    if not item["a_time"] or not isinstance(item["a_time"], str):
        a_time += 1

total_errors = bus_id + stop_id + stop_name + stop_type + next_stop + a_time
print(f"Type and required field validation: {total_errors} errors")
print(
f"""bus_id: {bus_id}
stop_id: {stop_id}
stop_name: {stop_name}
next_stop: {next_stop}
stop_type: {stop_type}
a_time: {a_time}
""")
