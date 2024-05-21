#!/bin/python3

import os, subprocess
from time import sleep

compPath = os.path.dirname(__file__)
ADBPath = f"{compPath}/platform-tools/"

def backup(compPath,ADBPath):
	try:
		file=open("backup.txt","r")
	except:
		file=open("backup.txt","w")
		print("Backup txt file is created, please enter the path of files you want to save from phone")
		file.close()
	str=file.readlines()
	file.close()
	for i in str:
		i=i.rsplit("\n")
		phonePath=i[0]
		try:
			os.makedirs(compPath+"/Saved_Files")
		except FileExistsError:
			pass
		try:
			command=f"cd {ADBPath} && ./adb pull {phonePath} {compPath}/Saved_Files/"
            subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
			print("Backed up", phonePath)
		except subprocess.CalledProcessError as e:
			print(e.output)
			if "Permission denied" in e.output:
				print("Enter sudo password to set ADB to be executable")
				os.system(f"cd {ADBPath} && sudo chmod +x *")

		except:
			command=f"cd {ADBPath} && ./adb pull {phonePath} {compPath}/Saved_Files/ >>/dev/null"
			os.system(command)
			print("Backed up", phonePath)
		sleep(2)
