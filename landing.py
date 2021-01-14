#!/bin/python3

import os

#https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

welcome=f"""
{bcolors.BOLD}
	__________________________________________________
	EE250 - Distributed Systems and Internet Of Things
	``````````````````````````````````````````````````

{bcolors.WARNING+bcolors.UNDERLINE}
	WARNING! RPi Playground must be used with caution.

{bcolors.HEADER}
	General Information:
{bcolors.ENDC+bcolors.BOLD+bcolors.HEADER}
	1. Try not to shutdown or reboot this RPi
	2. Try not to add packages to the RPi without permission
	3. Report any unusual incidents to the EE250 Staffs
	4. Your logins to this RPi are timestamped and recorded.

"""
print(welcome)




os.system('bash')
