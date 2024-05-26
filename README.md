# ADB
A Python script that backs up your files from your Phone to your PC via ADB.

## Prerequisites:
* Python installed, obviously.
* USB-Debugging enabled on your Android phone.
* "backup.txt" contains the path of the folders to be copied. Make sure to type out the path of the files or folders to be saved there. A sample file has been provided for your reference.
* The "requests" module to be installed using pip by the following command `pip install requests` or `pip3 install requests`

## Features:
* Fast file transfer
* Auto-download ADB at the correct place
* Allows automation (Guide coming soon)
* Experimental macOS support (You have to download and extract the "platform-tools" folder from [here](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip) into the app folder correctly) (This behaviour will be fixed soon...)

## Upcoming Features:
* Ask which files/folders to back up upon execution
* Speed optimisation
* GUI app
