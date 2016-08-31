import requests
import json

FLIGHT_URL="https://desktopapps.ryanair.com/en-gb/availability?"
#FLIGHT_URL="https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateIn=" + DATEIN + "&DateOut=" + DATEOUT + "&Destination=" + DESTINATION + "&FlexDaysIn=6&FlexDaysOut=4&INF=0&Origin=" + ORIGIN + "&RoundTrip=true&TEEN=0"

API_URL="https://api.ryanair.com/aggregate/3/common?embedded=airports&market=en-gb"
#API_URL="http://localhost:8080/airports.json"

requests.packages.urllib3.disable_warnings()

## Print flights
def printFlights(origin, destination, datein, dateout, type_of_flight="regularFare"):
    url = FLIGHT_URL + "ADT=1&CHD=0&DateIn=" + datein + "&DateOut=" + dateout + "&Destination=" + destination + "&FlexDaysIn=6&FlexDaysOut=4&INF=0&Origin=" + origin + "&RoundTrip=true&TEEN=0"
    r = requests.get(url)
    j = json.loads(r.content)

    for trip in j['trips']:
        print trip['origin'] + "->" + trip['destination']
        for day in trip['dates']:
             for flight in day['flights']:
                 print "-- " + flight['flightKey'].split("~")[5] + " - " + flight['flightKey'].split("~")[7] + " - " + str(flight[type_of_flight]['fares'][0]['amount']) + " " + j['currency']

## Return json airport object with name,seoName and iataCode from string
def searchAirport(searchname):
    r = requests.get(API_URL)
    j = json.loads(r.content)
    for airport in j['airports']:
        if (searchname.lower() in airport['name'].lower()) or (searchname.lower() in airport['seoName'].lower()):
            result = {}
            result['name'] = airport['name']
            result['seoName'] = airport['seoName']
            result['iataCode'] = airport['iataCode']
            return result
