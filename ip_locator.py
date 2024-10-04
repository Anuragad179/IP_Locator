# ---------------------------------------------------------
# Program: Change My IP
# Author: Anuragad179
# Date: 04 July 2024
# License: MIT License
#
# Copyright (c) 2024 [Your Name]
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# ---------------------------------------------------------


import geoip2.database
import sys
__author__ = "Anuragad179"
__version__ = "1.0.0"

def print_ownership_info():
    print("------------------------------------------------")
    print("Program: IP_Locator")
    print("Author: Anuragad179")
    print("Copyright © 2024")
    print("------------------------------------------------")


if __name__ == "__main__":
    print_ownership_info()



def get_location(ip_address):
    try:
        # Load the GeoLite2 City database
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        
        # Query the database with the IP address
        response = reader.city(ip_address)
        
        # Extract latitude and longitude
        latitude = response.location.latitude
        longitude = response.location.longitude
        
        return latitude, longitude
    except geoip2.errors.AddressNotFoundError:
        print("IP address not found in database.")
        return None, None
    except Exception as e:
        print("An error occurred:", e)
        return None, None
    finally:
        # Close the GeoLite2 City database reader
        reader.close()

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) != 2:
        print("Usage: python ip_locator.py <IP_ADDRESS>")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    latitude, longitude = get_location(ip_address)
    if latitude is not None and longitude is not None:
        print(f"The latitude and longitude of {ip_address} are: {latitude}, {longitude}")
