# NASR Subscription Information to Sector File Converter for VATSIM FUNCTIONS
# By Ian Cowan
# Python 3.7

# Import Packages
import math

# Latitude/Longitude Distance Calculation
def distance_calc(lat1, lon1, lat2, lon2):
    lat1 = lat1 / 180 * math.pi
    lon1 = lon1 / 180 * math.pi
    lat2 = lat2 / 180 * math.pi
    lon2 = lon2 / 180 * math.pi
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) * math.sin(dlon / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6366.707

    dist = R * c * .54
    
    return dist
