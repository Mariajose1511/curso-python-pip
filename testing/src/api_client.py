import requests

def get_location(ip):
    url =  f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()       
    return {
        'country': data['countryName'],
        'region': data['regionName'],
        'city': data['cityName'],
        'code': data['countryCode'],
        'continent': data['continent'],
    }


# if __name__ == '__main__':
#     print(get_location('8.8.8.8'))
    
    
#     {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']}