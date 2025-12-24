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
    'Kw-Umbrella-Token':'a92af63cd4ec3fb2d606dc6e5f23c374d6e75bd9f2dd796b273d53c612f3b183',
    'minWaitTime':1,
    'maxWaitTime':3
}

# round trip
form_data_round = {
    'sheetName':'Itineraries_round.xlsx',
    'minNights': 8,
    'maxNights': 11,
    # NOTE: update dates as needed
    'startDate': '2026-06-11',
    'endDate': '2026-06-28',
    "source": {
        "ids": [
            "City:beirut_lb"
        ]
    },
    "destination": {
        "ids": [
            # Use city id (matches working browser capture). You can add airport ids too if desired.
            "City:paris_fr"
        ]
    },
    # Required tokens/headers (copied from requestsresponse.txt capture)
    'Kw-Umbrella-Token':'f78680f2e89b67b438a528b0ccf8b53eaf1aa4199b46828c127b3e6b4b0d57de',
    'Kw-Skypicker-Visitor-Uniqid': '45a80434-113c-4a86-8979-8aadae353ac6',
    'extra_headers': {
        'Kw-Validation-Token': '684b02eac1cf24d4390748a7997dc723405f7a4442d37b6488c48ca3f17366eb',
        'Kw-X-Rand-Id': 'e214d1f18a0abdcf31031c9d8c25b8f4cc1bfdd8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
    },

    # Options that materially affect results (copied from requestsresponse.txt capture)
    'currency': 'usd',
    'locale': 'en',
    'partner': 'skypicker',
    'market': 'lb',
    'partnerMarket': 'xx',
    'affilID': 'acquisition000brand000sem',
    'searchStrategy': 'REDUCED',
    'mergePriceDiffRule': 'INCREASED',
    'searchSessionId': '185e46161abe42fdb432a2678e17a34d',
    'serverToken': 'eyJ0b2tlbiI6InRSRnoxdWdqZ3VSV0pCeE5NZkpwRDdaczkxVGRMYk5uUXZRMjBCUmhMR3B0WWpmemcwY0RGUWQxM1ZwclVCWDVEVmJiUnFxcVRDbXJCY2hWb2FyYXZ0dnU0dmt4Z3FwRzA4d0F1YzNZbUNWWExIdHFGcXl1SzNiTmVYWUtrY0M3dlhXbG9kWHNtT0RZN3M3QzlVVldHaUNaNFJvWEFFSVY3TndTV203b0ZwdEhZaEZteXZqYkI0NW5wbzE4amhPdlh0N2FJQnMtQThxaHJjeFNoUlUzV19Mb3d4RXJXV2s5S0plMkRFN1RZSEJ6ZjFvc1g5Z3NheGFGVk1DR3lGU3d4Z1FGMVJ6c2kyYm5UWmJnSXByOFZ0eWh2WmROY3F6b2ItWFhpMG5xVW5vdmpGYW83OG9hMXo4cXFFSHkwUnBObTEtdTZsSjdiWGtzeVYyMkFDTGRnc240OU9VdXk2cVNHeVV2Y01hUW9QRGFhYUlpc3Mxc1ptSHZmbE81MHh4TjUwbUdkazJOLVVRaFI1MzJZNDB3ZnJVVXdJN0p6eTRlbVlCYTJCWmZVWHB3b1RMX0x4dE5yMmJRazBwQ1VZcGh5aDNHMG5hc2UyNW5SVWpxRzFpaVhjWDVuMW81QXFyd3l2ai1ZYjdiMDAzVFotODBad0pCYnd2LXJYSldUV3dtQVloWkFPZXpreGFyM0JRTWlfU0NRYjZRUEhhS21rcDZuaXYtSW8wUFVlV0NEeVRNWWx2YTRLaV9BZlliZXBiYyIsInRpbWVzIjp7IjEiOjE3NjY1Nzc5ODMuOTIsIjgiOjE3NjY1Nzc5ODMuMTI3LCJUVCI6MTc2NjU3Nzk4Mi43Mjh9fQ==',

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