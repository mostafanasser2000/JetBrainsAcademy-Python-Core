import json
import re


json_string = input()
buse_information = json.loads(json_string)


bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0
buses = {}
for item in buse_information:
    if not item["bus_id"] or not isinstance(item["bus_id"], int):
        bus_id += 1
    if not item["stop_id"] or not isinstance(item["stop_id"], int):
        stop_id += 1
    if re.match("^[A-Z].+(Street|Avenue|Boulevard|Road)$", item["stop_name"]) is None:
        stop_name += 1
    if not isinstance(item["next_stop"], int):
        next_stop += 1
    if item["stop_type"] not in ["S", "O", "F", ""]:
        stop_type += 1
    if re.match("^[012]\d:[0-6]\d$", item["a_time"]) is None:
        a_time += 1

    if item["bus_id"] not in buses:
        buses[item["bus_id"]] = set()
    buses[item["bus_id"]].add(item["stop_id"])
total_errors = stop_name + stop_type + a_time
print("Line names and number of stops:")
for line, stops in buses.items():
    print(f"bus_id: {line}, stops: {len(stops)}")
