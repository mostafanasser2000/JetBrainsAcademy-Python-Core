import itertools
import json

json_string = input()
buse_information = json.loads(json_string)
buses = {}

# Stage6
starting_stops = set()
all_stops = []
finishing_stops = set()
transfer_stops = set()
on_demand_stops = set()
for item in buse_information:
    if item["bus_id"] not in buses:
        buses[item["bus_id"]] = []
    buses[item["bus_id"]].append((item["stop_type"], item["stop_name"]))

for line, bus_line_stops in buses.items():
    points = set()
    for stop_type, name in bus_line_stops:
        if stop_type == 'S':
            starting_stops.add(name)
        elif stop_type == 'F':
            finishing_stops.add(name)
        elif stop_type == 'O':
            on_demand_stops.add(name)
        points.add(name)
    all_stops.append(points)


for point1, point2 in itertools.combinations(all_stops, 2):
    intersection_stops = list(set.intersection(point1, point2))
    for stop in intersection_stops:
        transfer_stops.add(stop)

wrong_stops = set()
for on_demand_stop in on_demand_stops:
    if (on_demand_stop in starting_stops) or (on_demand_stops in finishing_stops) or (on_demand_stop in transfer_stops):
        wrong_stops.add(on_demand_stop)

print("On demand stops test:")
if wrong_stops:
    print("Wrong stop type:", sorted(wrong_stops))
else:
    print("OK")