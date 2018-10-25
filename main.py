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
    #Test:
    start_tmp = {"start": []}

    # Processing
    start_stations = defaultdict(int)
    end_stations = defaultdict(int)
    for row in rows:
        start_station = row[4]
        end_station = row[7]
        start_stations[start_station] += 1
        end_stations[end_station] += 1

        # Test:
        try:
            start = float(start_station)
            if start > 20000 or start < 3400:
                start_tmp["start"].append(start_station)
        except ValueError:
            continue

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

    return start_stations, end_stations, start_tmp


def average_distance_travelled(rows):
    """
    Given rows of our data, computes average distance.
    """
    count = 0
    total_distance = 0
    distances = defaultdict(int)

    for row in rows:

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
            distances[distance.miles] += 1
            total_distance += distance.miles
            count += 1

        # if count == 20:
        #     break

    print("Average distance in miles:", total_distance / count)

    return distances



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

    # START/STOP STATIONS
    start_stations, end_stations, start_tmp = top_stations(rows)
    with open('data/start-freq.json', 'w') as outfile:
        json.dump(start_tmp, outfile)
    # with open('data/end-stations-frequency.json', 'w') as outfile:
    #     json.dump(end_stations, outfile)

    # DISTANCES
    # distances = average_distance_travelled(rows)
    # with open('data/travel-distances.json', 'w') as outfile:
    #     json.dump(distances, outfile)

    # REGULAR COMMUTERS
    # regular_commute(rows)

run("data/original-bike-data.csv")
