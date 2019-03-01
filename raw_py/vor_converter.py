# NASR Subscription Information to Sector File Converter for VATSIM - VORs
# By Ian Cowan
# Python 3.7

# Import Packages
from functions import *

# Main function to be called from main.py
def run():
    # Open all the NAV.txt file and create the output file
    navaid = open('NAV.txt', 'r')
    navaid_output = open('vor_output.txt', 'w')

    # Asks the user for the VOR and distance for VOR results
    vor_ctr = 'NAV1' + input('What would you like the center VOR to be? ')
    range_from_ctr = int(input('How many miles would you like to return VORs around the said VOR? '))

    # Finds the center VOR
    return_line = ''
    for line in navaid:
        if line[0:7] == vor_ctr and line[8:11] == 'VOR':
            return_line = line
            lat1 = float(return_line[385:395]) / 3600
            lon1 = float(return_line[410:420]) / 3600

    # Validation Loops
    while return_line == '':
        print('That VOR could not be found.')
        vor_ctr = 'NAV1' + input('What would you like the center VOR to be? ')

        navaid = open('NAV.txt', 'r')

        return_line = ''
        for line in navaid:
            if line[0:7] == vor_ctr:
                return_line = line
                lat1 = float(return_line[385:395]) / 3600
                lon1 = float(return_line[410:420]) / 3600

    while range_from_ctr < 0:
        print('That is not a valid range distance.')
        range_from_ctr = int(input('How many miles would you like to return VORs around the said VOR? '))

    # Initialize vors list
    vors = list()

    # Loops through each navaid and looks for VORs within the specific radius
    navaid = open('NAV.txt', 'r')
    for line in navaid:
        if line[8:11] == 'VOR':
            if line[0:4] == 'NAV1':
                lat2 = float(line[385:395]) / 3600
                lon2 = float(line[410:420]) / 3600
                distance = distance_calc(lat1, lon1, lat2, lon2)
                if distance <= range_from_ctr:
                    vors.append(line)

    # Inserts everything into a file
    navaid_output.write(';Navaid Database Population Program Created by Ian Cowan\n;All VORs within ' + str(range_from_ctr) + 'nm of ' + vor_ctr[4:7] + ' VOR\n')

    # Loops through each VOR in the search parameters and adds it to the file
    for v in vors:
        vor_three = v[4:7]
        freq = v[533:539]
        n_coord = 'N0' + v[371:373] + '.' + v[374:376] + '.' + v[377:379] + '.' + v[380:383]
        w_coord = 'W' + v[396:399] + '.' + v[400:402] + '.' + v[403:405] + '.' + v[406:409]
        substring = v[42:]
        substring = substring.split('  ', 1)
        name = substring[0]
        substring = v[8:]
        substring = substring.split('  ', 1)
        nav_type = substring[0]
        navaid_output.write(vor_three + ' ' + freq + '  ' + n_coord + ' ' + w_coord + ' ;' + name + ' ' + nav_type + '\n')

    # Close the files
    navaid.close()
    navaid_output.close()
