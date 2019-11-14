"""
This code will hep you find a place in Google Maps via cmd.
How to use this code: run the script gmaps.py in cmd with location as parameter and it will open Google maps with location.
Or copy the location and just run the script without any paramters.
Libraries required
Webbrowser
sys
pyperclip

"""
import webbrowser as wb
import sys
from typing import List

import pyperclip

git = "https://github.com/Vinci141"
gmap = "https://www.google.com/maps/place/"

# input_data: List[str] = [git, gmap]
NoOfArg = len(sys.argv)
if NoOfArg > 1:
    # get address from argv
    address = ' '.join(sys.argv[1:])
    print('{} arguments provided'.format(NoOfArg))
    print(address)
else:
    # get address from clipboard
    address = pyperclip.paste()

if 'map' in address:
    wb.open(f"{gmap}{address[3:]}")
elif address == 'git':
    wb.open("https://github.com/Vinci141")
