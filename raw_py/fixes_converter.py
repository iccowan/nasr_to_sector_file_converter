# NASR Subscription Information to Sector File Converter for VATSIM - Fixes
# By Ian Cowan
# Python 3.7

# Import Packages
from functions import *

# Main function to be called from main.py
def run():
    # Open all the NAV.txt file and create the output file
    navaid = open('NAV.txt', 'r')
    fixes = open('FIX.txt', 'r')
    fixes_output = open('fix_output.txt', 'w')

    # Asks the user for the VOR and distance for fix results
    fix_ctr = 'NAV1' + input('What would you like the center VOR to be? ')
    range_from_ctr = int(input('How many miles would you like to return Fixes around the said VOR? '))

    # Finds the center VOR
    return_line = ''
    for line in navaid:
        if line[0:7] == fix_ctr and line[8:11] == 'VOR':
            return_line = line
            lat1 = float(return_line[385:395]) / 3600
            lon1 = float(return_line[410:420]) / 3600

    # Validation Loops
    while return_line == '':
        print('That VOR could not be found.')
        fix_ctr = 'NAV1' + input('What would you like the center VOR to be? ')

        navaid = open('NAV.txt', 'r')

        return_line = ''
        for line in navaid:
            if line[0:7] == fix_ctr and line[8:11] == 'VOR':
                return_line = line
                lat1 = float(return_line[385:395]) / 3600
                lon1 = float(return_line[410:420]) / 3600

    while range_from_ctr < 0:
        print('That is not a valid range distance.')
        range_from_ctr = int(input('How many miles would you like to return Fixes around the said VOR? '))

    # Initialize fixes list
    fixes_return = list()

    # Loops through each fix and looks for fixes within the specific radius
    for line in fixes:
        if line[0:4] == 'FIX1':
            lat_hrs = float(line[66:68]) * 3600
            lat_min = float(line[69:71]) * 60
            lat_sec = float(line[72:78])
            lon_hrs = float(line[80:83]) * 3600
            lon_min = float(line[84:86]) * 60
            lon_sec = float(line[87:93])
            lat = lat_hrs + lat_min + lat_sec
            lon = lon_hrs + lon_min + lon_sec
            lat2 = lat / 3600
            lon2 = lon / 3600
            distance = distance_calc(lat1, lon1, lat2, lon2)
            if distance <= range_from_ctr:
                fixes_return.append(line)

    # Inserts everything into a file
    fixes_output.write(';Navaid Database Population Program Created by Ian Cowan\n;All Fixes within ' + str(range_from_ctr) + 'nm of ' + fix_ctr[4:7] + ' VOR\n')

    # Loops through each Fix in the search parameters and adds it to the file
    for v in fixes_return:
        fix_name = v[4:10]
        n_coord = 'N0' + v[66:68] + '.' + v[69:71] + '.' + v[72:78]
        w_coord = 'W' + v[80:83] + '.' + v[84:86] + '.' + v[87:93]
        fixes_output.write(fix_name + ' ' +  n_coord + ' ' + w_coord + '\n')

    # Close the files
    navaid.close()
    fixes.close()
    fixes_output.close()
