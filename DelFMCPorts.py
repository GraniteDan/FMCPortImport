from fireREST import FMC
import csv
from colors import red, green, blue, yellow
h1 = """################################################################################################

Common Application Port Object Import Tool for Cisco FMC API

!!! ENSURE API ACCESS IS ENABLED IN THE FMC @: SYSTEM > CONFIGURATION > REST API PREFERENCES !!!

Author: Dan Parr / dparr@granite-it.net
Created: July 29 2023

This Script Relies on a number of Python Libraries (fireREST, csv, ansicolors)
################################################################################################
"""
print(green(h1))

filename = 'protoports.csv'

#fields = []
#rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)
     
    # extracting field names through first row
    #fields = next(csvreader)
 
    # extracting each data row one by one
    #for row in csvreader:
    #    rows.append(row)

    # get total number of rows
    #print(yellow("Importing %d Named Protocol Port Definitions into FirePower Management Console"%(csvreader.line_num)))
   # print(csvreader.count)
    #print (csvreader.len)
# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))

    fmc = FMC(hostname='10.11.35.9', username='apiuser', password='T1ckBit3!', domain='Global')
    for row in csvreader:
        print(row['name'])
        pport_obj = {
        'name':row['name'],
        'port':row['port'],
        'protocol':row['protocol']
    }
        try:
            fmc.object.protocolportobject.delete(name=row['name'])
            #X = fmc.object.protocolportobject.get(name=row['name'])
            #fmc.object.protocolportobject.delete()
            
           # print(X)
        except Exception as e: print(red(e))

