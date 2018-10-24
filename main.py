import csv
from collections import defaultdict
import numpy as np
import geopy.distance
import json


def process_csv(filename):
    """
    Opens and returns our csv file by lines.
    """
    # Open csv file
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    # Return all rows except first
    return rows[1:]

def top_stations(rows):
    """
    Generates top 5 stations (start and end) given a list of rows as input.
    """
    # Processing
    start_stations = defaultdict(int)
    end_stations = defaultdict(int)
    for row in rows:
        start_station = row[4]
        end_station = row[7]
        start_stations[start_station] += 1
        end_stations[end_station] += 1

    # print(start_stations)
    # print(end_stations)

    # Computing top 5 starts
    unique_starts = len(start_stations)
    print("Number of unique starting stations:", unique_starts)

    top5_start_scores = sorted(start_stations.values())[unique_starts - 5: unique_starts]
    top_starts = []
    for start in start_stations:
        if start_stations[start] in top5_start_scores and start not in top_starts:
            top_starts.append(start)
    print(top_starts)

    # Computing top 5 ends
    unique_ends = len(end_stations)
    print("Number of unique ending stations:", unique_ends)

    top5_end_scores = sorted(end_stations.values())[unique_ends - 5: unique_ends]
    top_ends = []
    for end in end_stations:
        if end_stations[end] in top5_end_scores and end not in top_ends:
            top_ends.append(end)
    print(top_ends)


    return start_stations, end_stations


def average_distance_travelled(rows):
    """
    Given rows of our data, computes average distance.
    """
    count = 0
    distances = []
    for row in rows:
        count += 1
        # Malformed data, sometimes can't parse to float
        try:
            # Start data
            start_lat = float(row[5])
            start_long = float(row[6])
            # End data
            end_lat = float(row[8])
            end_long = float(row[9])
        except ValueError:
            continue

        trip_route_category = row[12]

        start = np.array([start_lat, start_long])
        end = np.array([end_lat, end_long])

        # print(start_lat, start_long, " ->  TO  -> ", end_lat, end_long)

        # Only considering One-Way trips for now....
        if trip_route_category != "Round Trip":
            distance = geopy.distance.distance(start, end)
            # print("Distance :", distance)
            distances.append(distance)

        if count == 20:
            break

    distances_miles = list(x.miles for x in distances)
    print("Average distance:", sum(distances_miles) / len(distances_miles))


def regular_commute(rows):
    """
    Given the rows of data, computes the number of "riders that include bike-sharing
    as a regular part of their commute.
    """
    count = 0
    regulars = 0
    for row in rows:
        count += 1
        pass_type = row[13]
        if pass_type != "Walk-up":
            regulars += 1

        # if count == 20:
        #     break

    print(regulars)

def run(filename):
    """
    Run computations.
    """
    rows = process_csv(filename)
    start_stations, end_stations = top_stations(rows)
    with open('data/start_stations_frequency.json', 'w') as outfile:
        json.dump(start_stations, outfile)
    with open('data/end_stations_frequency.json', 'w') as outfile:
        json.dump(end_stations, outfile)

    # average_distance_travelled(rows)
    # regular_commute(rows)

run("data/bike-data.csv")


# test = { "name":"John", "age":40, "car":None }
##convert object to json
# serialized= json.dumps(test)
# print(serialized)
# with open('data.json', 'w') as outfile:
#     json.dump(test, outfile)

