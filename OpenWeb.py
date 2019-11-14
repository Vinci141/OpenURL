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
import pyperclip

NoOfArg = len(sys.argv)
if NoOfArg > 1:
    # get address from argv
    address = ' '.join(sys.argv[1:])
    print('{} arguments provided'.format(NoOfArg))
else:
    # get address from clipboard
    address = pyperclip.paste()

# un comment below line to find a place in Google maps
# wb.open('https://www.google.com/maps/place/' + address)
wb.open("https://github.com/Vinci141")
