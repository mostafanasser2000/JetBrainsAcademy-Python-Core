import itertools
import json
import re


# Stage 4
json_string = input()
buse_information = json.loads(json_string)

buses = {}
starting_stops = set()
all_stops = []
finishing_stops = set()
transfer_stops = set()
for item in buse_information:
    if item["bus_id"] not in buses:
        buses[item["bus_id"]] = []
    buses[item["bus_id"]].append((item["stop_type"], item["stop_name"]))

first = True
for line, bus_line in buses.items():
    number_of_stops = 0
    number_of_finishes = 0
    points = set()
    for stop, name in bus_line:
        if stop == 'S':
            starting_stops.add(name)
            number_of_stops += 1
        elif stop == 'F':
            finishing_stops.add(name)
            number_of_finishes += 1
        points.add(name)
    all_stops.append(points)
    if number_of_stops != 1 or number_of_finishes != 1:
        print(f"There is no start or end stop for the line: {line}.")
        exit(0)
for point1, point2 in itertools.combinations(all_stops, 2):  # check if a bus stop exist in two buses lines and add it to transfer stops
    intersection_stops = list(set.intersection(point1, point2))
    for stop in intersection_stops:
        transfer_stops.add(stop)

print(
f"""Start stops: {len(starting_stops)} {sorted(starting_stops)}
Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}
Finish stops: {len(finishing_stops)} {sorted(finishing_stops)}
""")
