import json
import csv
from collections import defaultdict, OrderedDict

import numpy as np
import geopy.distance
import dateutil.parser
import datetime


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

    # Sort both start and end frequencies
    sorted_starts = sorted(start_stations.items(), key=lambda kv: -kv[1])
    sorted_ends = sorted(end_stations.items(), key=lambda kv: -kv[1])
    return sorted_starts, sorted_ends


def average_distance_travelled(rows):
    """
    Given rows of our data, computes average distance.
    """
    count = 0
    total_distance = 0
    distance_frequencies = defaultdict(int)

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

        # Get trip category and form arrays of start/end
        trip_route_category = row[12]
        start = np.array([start_lat, start_long])
        end = np.array([end_lat, end_long])

        # Only considering One-Way trips for now....
        if trip_route_category != "Round Trip":
            distance = geopy.distance.distance(start, end)
            # Crazy outliers
            if distance > 1000:
                continue
            distance_frequencies[round(distance.miles, 2)] += 1
            total_distance += distance.miles
            count += 1

    # Store distance frequencies sorted
    distance_probabilities = OrderedDict(sorted(distance_frequencies.items()))

    # We want probability density, not frequencies
    for key in distance_probabilities:
        distance_probabilities[key] = distance_probabilities[key] / count

    # Find our median
    total = 0.0
    median = 0
    for elem in sorted(distance_probabilities.items()):
        total += elem[1]
        if total >= .5:
            median = elem[0]
            break

    print("Median distance in miles:", median)
    print("Average distance in miles:", total_distance / count)
    return distance_probabilities


def regular_commute(rows):
    """
    Given the rows of data, computes the number of "riders that include bike-sharing
    as a regular part of their commute".
    """
    counts = defaultdict(int)
    for row in rows:
        pass_type = row[13]
        counts[pass_type] += 1
    return counts


def bike_distribution(rows):
    """
    Computes the frequencies of use across all bikes
    """
    # Initialize dates/time, dict
    count = 0
    bike_dist = defaultdict(int)

    # Iterate through all data
    for row in rows:
        # Get each bike id
        count += 1
        bike_id = row[10]
        if bike_id != "":
            bike_dist[bike_id] += 1

    # Get average
    print("Number of unique bikes:", len(bike_dist.keys()))
    avg_freq = count / len(bike_dist.keys())
    print("Average frequency for a bike:", avg_freq)

    # Sorted by value (frequency)
    sorted_bike_dist = sorted(bike_dist.items(), key=lambda kv: -kv[1])
    # Sorted by key (bike id)
    sorted_bike_id = OrderedDict(sorted(bike_dist.items()))
    # return sorted_bike_id
    return sorted_bike_dist


def time_distribution(rows):
    """
    Computes the distibution of time intervals for each bike usage.
    """
    time_dist = defaultdict(int)
    count = 0
    for row in rows:
        # Let's try to get the date/time
        try:
            start_time = dateutil.parser.parse(row[2])
            end_time = dateutil.parser.parse(row[3])
            minutes = (end_time - start_time).seconds / 60.0
            if minutes < 101:
                time_dist[minutes] += 1
                count += 1
        except ValueError:
            continue

    # Get mean
    total_time = 0
    for k, v in time_dist.items():
        total_time += k * v
    print("Average time:", total_time / count)
    # Get median
    total = 0.0
    median = 0
    for key, value in sorted(time_dist.items()):
        total += value
        if total > count / 2:
            median = key
            break
    print("Median time:", median)
        

    sorted_time_dist = OrderedDict(sorted(time_dist.items()))
    return sorted_time_dist


def run(filename):
    """
    Run computations.
    """
    rows = process_csv(filename)

    # START/STOP STATIONS
    # start_stations, end_stations = top_stations(rows)
    # with open('data/start-stations-frequency.json', 'w') as outfile:
    #     json.dump(start_stations, outfile)
    # with open('data/end-stations-frequency.json', 'w') as outfile:
    #     json.dump(end_stations, outfile)

    # DISTANCES
    # distances = average_distance_travelled(rows)
    # with open('data/travel-distances.json', 'w') as outfile:
    #     json.dump(distances, outfile)

    # REGULAR COMMUTERS
    # comms = regular_commute(rows)
    # print(comms['Walk-up'] / sum(comms.values()))
    # with open("data/pass-types.json", "w") as outfile:
    #     json.dump(comms, outfile)

    # BIKE FREQUENCIES
    # bike_dist = bike_distribution(rows)
    # with open("data/bike-freq.json", "w") as outfile:
    #     json.dump(bike_dist, outfile)

    # TIME SERIES
    time_dist = time_distribution(rows)
    with open("data/time-dist.json", "w") as outfile:
        json.dump(time_dist, outfile)


run("data/og/original-bike-data.csv")
