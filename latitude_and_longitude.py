from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

places = ['India', 'United States', 'Japan', 'Germany']

coordinates = {}

for place in places:
    location = geolocator.geocode(place)
    if location:
        coordinates[place] = (location.latitude, location.longitude)
    else:
        coordinates[place] = 'Not found'

for place, coord in coordinates.items():
    print(f"{place}: {coord}")
