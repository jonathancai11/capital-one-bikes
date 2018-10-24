import csv
from collections import defaultdict
import numpy as np
import geopy.distance



def processCSV(filename):
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
    unique_starts = len(start_stations.values())
    print("Number of unique starting stations:", unique_starts)
    top5_start_scores = sorted(start_stations.values())[unique_starts - 5: unique_starts]
    top_starts = []
    for start in start_stations:
        if start_stations[start] in top5_start_scores and start not in top_starts:
            top_starts.append(start)
    print(top_starts)


    # Computing top 5 ends
    unique_ends = len(end_stations.values())
    print("Number of unique ending stations:", unique_ends)
    top5_end_scores = sorted(end_stations.values())[unique_ends - 5: unique_ends]
    top_ends = []
    for end in end_stations:
        if end_stations[end] in top5_end_scores and end not in top_ends:
            top_ends.append(end)
    print(top_ends)


def computeAverageDistanceTravelled(rows):
    """
    Given rows of our data, computes average distance.
    """
    count = 0
    distances = []
    for row in rows:
        count += 1
        # Start data
        start_lat = float(row[5])
        start_long = float(row[6])
        # End data
        end_lat = float(row[8])
        end_long = float(row[9])

        trip_route_category = row[12]


        start = np.array([start_lat, start_long])
        end = np.array([end_lat, end_long])

        # print(start_lat, start_long, " ->  TO  -> ", end_lat, end_long)
        if trip_route_category != "Round Trip":
            distance = geopy.distance.distance(start, end)
            # print("Distance :", distance)
            distances.append(distance)
        if count == 20:
            break

    for dist in distances:
        print(dist.miles)
    # print(x.miles for x in distances)

def run(filename):
    rows = processCSV(filename)
    # top_stations(rows)
    computeAverageDistanceTravelled(rows)

run("data/bike-data.csv")

# Trip ID, Duration, Start Time, End Time, Starting Station ID, Starting Station Latitude, Starting Station Longitude, Ending Station ID, Ending Station Latitude, Ending Station Longitude, Bike ID, Plan Duration, Trip Route Category, Passholder Type, Starting Lat-Long, Ending Lat-Long

