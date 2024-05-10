# ADB
An app that backs up your files from your Phone to your PC via ADB.

## Prerequisites:
* USB-Debugging enabled on your Android phone (Doesn't work on iOS).
* ADB needs to downloaded from [here](https://developer.android.com/tools/releases/platform-tools) and put into the same folder as the main file and the Windows/Linux files. Ignore if ADB is in $PATH.
NOTE: "platform-tools" folder is to be present with correct version for your OS.
* "backup.txt" contains the path of the folders to be copied. Make sure to type out the path of the files to be saved there. A sample file has been provided for your reference.

## Upcoming Features:
* Download and place ADB files in the correct place upon execution
* macOS support
* Ask which files/folders to back up upon execution
* Speed optimisation