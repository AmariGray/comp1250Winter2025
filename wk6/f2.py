"""
create a function that converts KMs to Miles
"""
def convert_kilometers_to_miles(distance: float = 1.0)->float:
    if not isinstance(distance, float):
        return 0.0 
    return distance * 0.62


distance_in_km = 5.0

distance_in_miles = convert_kilometers_to_miles(distance_in_km)
print(f"{distance_in_km}KM is equal to {distance_in_miles} miles")

print(convert_kilometers_to_miles())

