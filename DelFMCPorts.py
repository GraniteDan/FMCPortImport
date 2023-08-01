from fireREST import FMC
import csv, json
from colors import red, green, blue, yellow
from getpass import getpass

h1 = """
################################################################################################

Common Application Port Object Removal Tool for Cisco FMC API

!!! ENSURE API ACCESS IS ENABLED IN THE FMC @: SYSTEM > CONFIGURATION > REST API PREFERENCES !!!

Author: Dan Parr
Created: July 29 2023
Version: 1.0

This Script Relies on a number of Python Libraries (fireREST, csv, ansicolors)
################################################################################################
"""


filename = 'protoports.csv'
Groups=[]
CSVData=[]
ip = input("Enter your FMC Management IP/Hostname:")
user = input("Enter FMC Username:")
pwd = getpass()
fmc = FMC(hostname=ip, username=user, password=pwd, domain='Global')
pwd = None
print(yellow(h1))

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)
     
    for row in csvreader:
        CSVData.append(row)
        grps=row['groups'].split('/')
        grps=row['groups'].split('/')
        for g in grps:
            if (g) and (g not in Groups):
                print(yellow("Adding " + g + " To list of groups to remove"))
                Groups.append(g)
               

    for group in Groups:
        print(green("Deleting: " + group))
        try:
            fmc.object.portobjectgroup.delete(name=group)
        except Exception as e: print(red(e))
    
    
    for row in CSVData:

        print("Removing Port Object: " + row['name'])
        
        try:
            fmc.object.protocolportobject.delete(name=row['name'])
           
        except Exception as e: print(red(e))
        
