import csv
from collections import defaultdict


def processCSV(filename):
    """
    Opens and returns our csv file by lines.
    """
    # Open csv file
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # with open(filename, 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     line_count = 0
    #     # Iterate through rows
    #     for row in csv_reader:
    #         # First row contains column names
    #         if line_count == 0:
    #             print(f'Column names are {", ".join(row)}')
    #             line_count += 1

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

    # Computing top 5 starts
    unique_starts = len(start_stations.values())
    top5_start_scores = sorted(start_stations.values())[unique_starts - 5: unique_starts]
    top_starts = []
    for start in start_stations:
        if start_stations[start] in top5_start_scores and start not in top_starts:
            top_starts.append(start)
    print(top_starts)


    # Computing top 5 ends
    unique_ends = len(end_stations.values())
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
    for row in rows:
        # Start data
        start_lat = row[5]
        start_long = row[6]
        # End data
        end_lat = row[5]
        start_long = row[5]

def run(filename):
    rows = processCSV(filename)
    top_stations(rows)

run("data/bike-data.csv")

# Trip ID, Duration, Start Time, End Time, Starting Station ID, Starting Station Latitude, Starting Station Longitude, Ending Station ID, Ending Station Latitude, Ending Station Longitude, Bike ID, Plan Duration, Trip Route Category, Passholder Type, Starting Lat-Long, Ending Lat-Long


# print("Trip ID: " + row[0]
#       + "Duration: " + row[1]
#       + "Start Time: " + row[2]
#       + "Starting Station ID: " + row[3]
#       + "Starting Station Latitude: " + row[4]
#       + "Starting Station Longitude: " + row[5]
#       + "Ending Station ID: " + row[6]
#       + "Ending Station Latitude: " + row[7]
#       + "Ending Station Longitude: " + row[8]
#       + "Bike ID: " + row[9]
#       + "Plan Duration: " + row[9]
#       + "Trip Route Category: " + row[9]
#       + "Ending Station ID: " + row[9]
#       )
