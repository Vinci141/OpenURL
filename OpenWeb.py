"""
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
NoOfArg = len(sys.argv)


def openWebPage(data):
    if 'map' in data:
        wb.open(f"{gmap}{data[3:]}")
    elif address == 'git':
        wb.open(f"{git}")
    else:
        wb.open(data) # Data copied in clipboard will be opened


if NoOfArg > 1:
    # get address from argv
    address = ' '.join(sys.argv[1:])
    openWebPage(address)
    print('{} arguments provided'.format(NoOfArg))
    print(address)
else:
    # get address from clipboard
    address = pyperclip.paste()
