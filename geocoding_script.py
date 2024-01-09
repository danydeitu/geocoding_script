from geopy.geocoders import Nominatim

#I create an OpenStreetMap geolocator object
geolocator = Nominatim(user_agent="my_geocoder")

# Step 1: Geocode the initial address
initial_address = "1300 SE Stark Street, Portland, OR 97214"
initial_location = geolocator.geocode(initial_address)
initial_coordinates = (initial_location.latitude, initial_location.longitude)
print(f"Initial Coordinates: {initial_coordinates}")

# Step 2: Query the neighborhood using the initial coordinates using reverse geocoding
initial_neighborhood = geolocator.reverse(initial_coordinates).raw.get('address', {}).get('neighbourhood')
if not initial_neighborhood:
    initial_neighborhood = "No neighborhood found"
print(f"Initial Neighborhood: {initial_neighborhood}")

# Step 3: Write a recursive function for address increment
def geocode_and_query(address, increment):
    # Geocode the address
    location = geolocator.geocode(address)
    
    if location is None:
        print(f"No location found for {address}")
        return
    
    coordinates = (location.latitude, location.longitude)

    # Query the neighborhood using the place information directly
    neighborhood = location.raw.get('address', {}).get('neighbourhood')
    if not neighborhood:
        neighborhood = "No neighborhood found"

    print(f"Address: {address}, Coordinates: {coordinates}, Neighborhood: {neighborhood}")

    # I build the next direction with the increment
    address_parts = address.rsplit(' ', 2)
    address_number = ''.join(filter(str.isdigit, address_parts[0]))

    if not address_number:
        print(f"No valid address number found for {address}")
        return

    next_address = f"{int(address_number) + increment} {address_parts[1]} {address_parts[2]}"
    print(f"Next Address: {next_address}")
    
    # I check if the neighborhood has changed
    next_neighborhood = geolocator.reverse(coordinates).raw.get('address', {}).get('neighbourhood')
    if not next_neighborhood:
        next_neighborhood = "No neighborhood found"
    
    if next_neighborhood == initial_neighborhood:
        geocode_and_query(next_address, increment)
    else:
        print(f"Neighborhood changed to {next_neighborhood}. Exiting.")
        return

# Step 4: Run the recursive function until the neighborhood changes
geocode_and_query(initial_address, 100)
