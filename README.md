NASR to Sector File Converter
=============================

Written by Ian Cowan

Executable for Windows Only

Installation and Usage
----------------------

1. Clone the repository or download the executable from GitHub.

2. Place the following files in the folder with the executable and leave them with the default names.
    - `NAV.txt` - MOST IMPORTANT
    - `FIX.txt`
    - `APT.txt`

3. Run the executable. The command line should open.

4. Follow the instructions. All converters use a VOR reference for searching the file.

5. If the correct files exist in the folder with the converter, the appropriate output file will be created.
    - Please note that if the file doesn't exist, the converter will close without an error but the file will not be created.

Troubleshooting
---------------
Please note that this utility is meant to be FUNCTIONAL and not user friendly. If the converter is not outputting the expected file:
- Make sure the appropriate files are within the same folder as the exe file.
- The executable will only work on Windows (not Mac or Linux). If you would like to run on Mac or Linux, you must use the base python file, have Python 3.7 installed on your computer, and run in the command line:
    - `python main.py`

Please note that the converter may break and not return errors due to the nature of this project.

Open Source
-----------
This program is open source and was written in Python 3.7. Feel free to make any changes but please do not distribute for compensation.
