"""
Create a program that will help us determine the price of a Go Train trip
Allow user to enter departing station, destination station
output to user the trip price & summarize their trip  => output to file
validate departing and destination stations: raise errors if valid input found
"""
import sys

departing_station = "Union"
destination_station = "Oshawa"

valid_stations = "Union,Danforth,Scarborough,Eglinton,Guildwood,Rouge Hill,Pickering,Ajax,Whitby,Oshawa".split(",")

base_price = 3.00
price_per_station = 2.50


def set_departing(station_name: str):

    if station_name.title() not in valid_stations:
        raise ValueError(f"{station_name} is not a stop in our trip. Valid station names are:  {','.join(valid_stations)}")

    global departing_station
    departing_station = station_name.title()


def set_destination(station_name):
    if station_name.title() not in valid_stations:
        raise ValueError(f"{station_name} is not a stop in our trip. Valid station names are:  {','.join(valid_stations)}")

    global destination_station
    destination_station = station_name.title()


def calculate_trip():
    """
    get the absolute difference between the departing and destination
    """
    try:
        index_departing = valid_stations.index(departing_station)
        index_destination = valid_stations.index(destination_station + "abc")
        station_difference = abs(index_departing - index_destination)
        station_difference -= 1
        total_price = base_price + price_per_station * station_difference
        with open("trip_details.txt", 'w') as fo:
            fo.write(f"Trip from {departing_station} to {destination_station} cost ${total_price}")
    except ValueError as e:
        print("Custom Error" + str(e), file=sys.stderr)
    except IOError:
        print("Could not open file to write")


def main():
    print("Welcome to our Go Train Trip Program")
    print("Usage: set_departing(station_name), set_destination(station), calculate_trip()")


if __name__ == "__main__":
    main()