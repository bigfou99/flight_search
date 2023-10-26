import search_flights
import utils

ids = ["Station:airport:ORY", "Station:airport:CDG", "City:beirut_lb"]

# 1 way tip
form_data_1_way = {
    'sheetName':'Itineraries_1_way.xlsx',
    'startDate': '2024-02-01',
    'endDate': '2024-02-03',
    "source": {
        "ids": [
            "City:beirut_lb"
        ]
    },
    "destination": {
        "ids": [
            "Station:airport:CDG",
            "Station:airport:ORY"
        ]
    },
    'Kw-Umbrella-Token':'8648c6f1ec561ba3cfe9ecd4530d28f483422b3d0493501dbed378f3e86d2ecb',
    'minWaitTime':1,
    'maxWaitTime':3
}

# round trip
form_data_round = {
    'sheetName':'Itineraries_round.xlsx',
    'minNights': 5,
    'maxNights': 8,
    'startDate': '2024-02-01',
    'endDate': '2024-02-29',
    "source": {
        "ids": [
            "City:beirut_lb"
        ]
    },
    "destination": {
        "ids": [
            "Station:airport:CDG",
            "Station:airport:ORY"
        ]
    },
    'Kw-Umbrella-Token':'d6d4f47ccdad80c2faa8c8edca2b8196d6845c5303151ea493e5405cdb97b284',
    'minWaitTime':1,
    'maxWaitTime':3
}

# 1 way trip
# itineraries = search_flights.search_1_way(form_data_1_way)
# utils.save_excel(itineraries, form_data_1_way['sheetName'])  

# round tri
itineraries = search_flights.search_round(form_data_round)
utils.save_excel(itineraries, form_data_round['sheetName'])  


print("Done.")