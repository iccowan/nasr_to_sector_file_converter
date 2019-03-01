# NASR Subscription Information to Sector File Converter for VATSIM
# By Ian Cowan
# Python 3.7

# Import Packages
import vor_converter
import ndb_converter
import fixes_converter
import airport_converter

# Run this on program run
def main():
    # Prompt the user for which converter they want to run
    print('Choose which converter to run:')
    print('1 => VORs')
    print('2 => NDBs')
    print('3 => Fixes')
    print('4 => Airports')
    run_what = input('')

    # Validation
    while run_what == '':
        print('Please choose a converter.')
        print('1 => VORs')
        print('2 => NDBs')
        print('3 => Fixes')
        print('4 => Airports')
        run_what = input('')

    while int(run_what) < 1 or int(run_what) > 7:
        print('That is not a valid converter.')
        print('1 => VORs')
        print('2 => NDBs')
        print('3 => Fixes')
        print('4 => Airports')
        run_what = input('')

    # Convert run_what to int
    run_what = int(run_what)

    # Pick the converter they chose and run it
    if run_what == 1:
        vor_converter.run()
    elif run_what == 2:
        ndb_converter.run()
    elif run_what == 3:
        fixes_converter.run()
    elif run_what == 4:
        airport_converter.run()

main()
