# NASR Subscription Information to Sector File Converter for VATSIM - Airports
# By Ian Cowan
# Python 3.7

# Import Packages
from functions import *

# Main function to be called from main.py
def run():
    # Open all the NAV.txt file and create the output file
    navaid = open('NAV.txt', 'r')
    airports = open('APT.txt', 'r')
    apt_output = open('apt_output.txt', 'w')

    # Asks the user for the VOR and distance for airport results
    apt_ctr = 'NAV1' + input('What would you like the center VOR to be? ')
    range_from_ctr = int(input('How many miles would you like to return Airports around the said VOR? '))

    # Finds the center VOR
    return_line = ''
    for line in navaid:
        if line[0:7] == apt_ctr and line[8:11] == 'VOR':
            return_line = line
            lat1 = float(return_line[385:395]) / 3600
            lon1 = float(return_line[410:420]) / 3600

    # Validation Loops
    while return_line == '':
        print('That VOR could not be found.')
        apt_ctr = 'NAV1' + input('What would you like the center VOR to be? ')

        navaid = open('NAV.txt', 'r')

        return_line = ''
        for line in navaid:
            if line[0:7] == apt_ctr and line[8:11] == 'VOR':
                return_line = line
                lat1 = float(return_line[385:395]) / 3600
                lon1 = float(return_line[410:420]) / 3600

    while range_from_ctr < 0:
        print('That is not a valid range distance.')
        range_from_ctr = int(input('How many miles would you like to return Airports around the said VOR? '))

    # Initialize airports list
    apts_return = list()

    # Loops through each airport and looks for airports within the specific radius
    for line in airports:
        if line[0:3] == 'APT':
            lat2 = float(line[538:549]) / 3600
            lon2 = float(line[565:576]) / 3600
            distance = distance_calc(lat1, lon1, lat2, lon2)
            if distance <= range_from_ctr:
                apts_return.append(line)

    # Inserts everything into a file
    apt_output.write(';Navaid Database Population Program Created by Ian Cowan\n;All Airports within ' + str(range_from_ctr) + 'nm of ' + apt_ctr[4:7] + ' VOR\n')

    # Loops through each Airport in the search parameters and adds it to the file
    for v in apts_return:
        apt_identifier = v[1210:1214]
        if apt_identifier == '    ':
            apt_identifier = v[27:30]
        freq = '000.000'
        n_coord = 'N0' + v[523:525] + '.' + v[526:528] + '.' + v[529:536]
        w_coord = 'W' + v[550:553] + '.' + v[554:556] + '.' + v[557:564]
        if len(apt_identifier) == 3:
            apt_output.write(apt_identifier + '  ' +  n_coord + ' ' + w_coord + '\n')
        else:
            apt_output.write(apt_identifier + ' ' +  n_coord + ' ' + w_coord + '\n')

    # Close the files
    navaid.close()
    airports.close()
    apt_output.close()
