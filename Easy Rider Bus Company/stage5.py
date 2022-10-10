import json


json_string = input()
buse_information = json.loads(json_string)

# Stage 5
buses = {}
invalid_lines = []
invalid_buses_stops = []

for item in buse_information:
    if item["bus_id"] not in buses:
        buses[item["bus_id"]] = []
    if item["bus_id"]:
        buses[item["bus_id"]].append((item["stop_name"], item["a_time"]))

for bus, arrival_times_info in buses.items():
    for i in range(len(arrival_times_info) - 1):
        curren_arrival_time = arrival_times_info[i][1]
        next_arrival_time = arrival_times_info[i + 1][1]
        next_bus_stop = arrival_times_info[i + 1][0]
        if curren_arrival_time >= next_arrival_time:
            invalid_lines.append(bus)
            invalid_buses_stops.append(next_bus_stop)
            break

print("Arrival time test:")
if invalid_lines:
    for line, bus_stop in zip(invalid_lines, invalid_buses_stops):
        print(f"bus_id line {line}: wrong time on station {bus_stop}")
else:
    print("OK")
