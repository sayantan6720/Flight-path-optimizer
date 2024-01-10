import requests
import json

# public api key we found on skyscanner documentation
api_key = 'sh428739766321522266746152871799'

# this is the actual payload, using for testing
data = {
    "query": {
    "market": "US",
    "locale": "en-US",
    "currency": "USD",
    "queryLegs": [
      {
        "originPlaceId": {
          "iata": "DCA"
        },
        "destinationPlaceId": {
          "iata": "JFK"
        },
        "date": {
          "year": 2023,
          "month": 12,
          "day": 12
        }
      }
    ],
    "cabinClass": "CABIN_CLASS_ECONOMY",
    "adults": 1,
    "childrenAges": [],
    "includedCarriersIds": [],
    "excludedCarriersIds": [],
    "includedAgentsIds": [],
    "excludedAgentsIds": [],
    "includeSustainabilityData": True,
    "nearbyAirports": True
  }
}

# the headers
headers = {
    'x-api-key': api_key
}

# url to get the create search
url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'

# the actual post
response = requests.post(url, headers=headers, json=data)


# simple if else to help with debugging
if response.ok:
    print(response.json())
else:
    print(f"Error when retrieving data: {response.status_code}, {response.json}")



