# OwlHacks 2020
# Athan Kim

# Program takes in two user inputs as the Latitude and Longitude of the location to be used
# Also takes in the API key
# Program establishes 5 usable functions that fetch the key, latitude, longitude and the radius. Given these parameters, a URL can be created.

import os

def getKey(): # Fetches the key and returns the value
    
    file = open("key.txt", "r")
    key1 = file.read()
    file.close()
    
    return key1

def getLati(): # Takes in a user input of the latitude and returns the value
    lati = input("Enter the desired latitude value (N): ")
    return lati

def getLongi(): # Takes in a user input of the longitude and returns the value
    longi = input("Enter the desired longitude value (W): ");
    return longi

def getRadius(): # Takes in a user input of miles and converts it to meters and returns the value
    miles = input("Enter the desired mile radius: ")
    meters = float(miles) * 1609.34
    return meters

def generatePlaceSearchCall(key, lati, long, rad): # Takes all established parameters and creates a URL
    return "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lati) + "," + str(long) + "&radius=" + str(rad) + "&type=electronics_store&key=" + str(key)
