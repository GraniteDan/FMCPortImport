from fireREST import FMC
import csv, json
from colors import red, green, blue, yellow
from getpass import getpass

## Global Variables ##
global fmc


#Function Definition
def GetPortObject (portname):
    try:
        obj = fmc.object.protocolportobject.get(name=portname)
    except:
        obj = None
    return obj

def GetPortGroup (groupname):
    try:
        obj = fmc.object.portobjectgroup.get(name=groupname)
    except:
        obj = None
    return obj

def search_dictionaries(key, value, list_of_dictionaries):
  return [element for element in list_of_dictionaries if element[key] == value]


## Variable Definitions ##
h1 = """
################################################################################################

Common Application Port Object Import Tool for Cisco FMC API

!!! ENSURE API ACCESS IS ENABLED IN THE FMC @: SYSTEM > CONFIGURATION > REST API PREFERENCES !!!

Author: Dan Parr
Created: July 29 2023
Version: 1.0

This Script Relies on a number of Python Libraries (fireREST, csv, ansicolors)
################################################################################################

"""
print(green(h1))
filename = 'protoports.csv'
Groups=[]
CSVData=[]
ip = input("Enter your FMC Management IP/Hostname:")
user = input("Enter FMC Username:")
pwd = getpass()
fmc = FMC(hostname=ip, username=user, password=pwd, domain='Global')
pwd = None



with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)
    
    #Loop Through CSV Rows.
    for row in csvreader:
        CSVData.append(row)
        #print(row['name'])
        #Create ProtocolPortObject if one of the same name doesn't already exist
        if not GetPortObject(row['name']):
            print(green("Port Object: " + row['name'] + " Not defined, Creating new Protocol Port Object"))
            pport_obj = {
                'name':row['name'],
                'port':row['port'],
                'protocol':row['protocol']
            }
            fmc.object.protocolportobject.create(data=pport_obj)
        else:
            print(red("Port object: " + row['name'] + " Already Exists. Manually verify that objects match"))
                
        #Generate a list of unique Group Names from the CSV files Groups column
        grps=row['groups'].split('/')
        for g in grps:
            if (g) and (g not in Groups):
                Groups.append(g)

#Create Groups and add members
for g in Groups:
    grpobj = GetPortGroup(g)
    if grpobj: #Update Existing Group
        print(yellow("Group " + g +" Already Exists, Adding Port Objects to Existing Group"))
        #Loop Through CSV to find Group Members
        for p in CSVData:
            if g in p['groups'].split('/'):
                portobj = GetPortObject(p['name'])
                if not portobj:
                    print("object not found")
                else:
                    stripport = portobj
                    del stripport['metadata']
                    del stripport['links']
                    if not search_dictionaries('id', stripport['id'], grpobj['objects']):
                        grpobj['objects'].append(stripport)
        fmc.object.portobjectgroup.update(data=grpobj)                
    else: # Create New Group if one doesn't exist
        print(green("Group " + g + " Not Previously Defined. Creating New PortObjectGroup"))
        elist = []
        grpobj = {
            'name':g,
            'type':"PortObjectGroup",
            'objects':[]
        }
        
        #Loop Through CSV to Find Members
        for p in CSVData:
            if g in p['groups'].split('/'):
                portobj = GetPortObject(p['name'])
                if not portobj:
                    print("object not found")
                else:
                    stripport = portobj
                    del stripport['metadata']
                    del stripport['links']
                    if not search_dictionaries('id', stripport['id'], grpobj['objects']):
                        print(green("Adding PortObject: " + portobj['name'] + " to PortObjectGroup: " + g))
                        grpobj['objects'].append(stripport)
        fmc.object.portobjectgroup.create(data=grpobj)


