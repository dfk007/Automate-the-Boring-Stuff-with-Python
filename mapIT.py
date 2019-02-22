#! python3
# mapIT.py - Launches a map in the browser using an address from the
# command line or clipboard.
"""[*]Check recent format for gmap url format.[*]"""
import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])    # sys.argv = list of strings, .join() returns a single string value.
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/map/place/' + address)

    

