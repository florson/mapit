#! /usr/bin/env python3

import webbrowser, sys, pyperclip

#sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Vakencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://google.com/maps/place/<ADDRESS>
webbrowser.open('https://google.com/maps/place/' + address)
