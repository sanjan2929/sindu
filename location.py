import requests

def get_current_location():
    try:
        # Fetching the IP-based location
        response = requests.get('http://ip-api.com/json/')
        data = response.json()

        if data['status'] == 'success':
            lat = data['lat']
            lon = data['lon']
            return lat, lon
        else:
            raise Exception("Unable to get the location data")
    except Exception as e:
        print(f"Error: {e}")
        return None, None

lat, lon = get_current_location()
if lat and lon:
    print(f"Current Location: Latitude = {lat}, Longitude = {lon}")
else:
    print("Could not determine the location.")
