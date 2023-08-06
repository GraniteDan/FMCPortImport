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

print(yellow(h1))
filename = 'protoports.csv'
Groups=[]
CSVData=[]

ip = input("Enter your FMC Management IP/Hostname:")
user = input("Enter FMC Username:")
pwd = getpass()
fmc = FMC(hostname=ip, username=user, password=pwd, domain='Global')
pwd = None


#fn = input("Please enter a file name to save json to:")
objdata = ['fqdn','icmpv4object','interface','interfacegroup','network','networkaddress','networkgroup','policylist','portobjectgroup','protocolportobject','range','securitygrouptag','securityzone']
poldata = ['accesspolicy','filepolicy','intrusionpolicy','prefilterpolicy']

for o in objdata:
    fn = o + '.json'
    data = (getattr(fmc.object, o).get())
    with open (fn, 'w', encoding='utf-8') as jfile:
        jdata = json.dump(data, jfile, ensure_ascii=False, indent=2)

for o in poldata:
    fn = o + '.json'
    data = (getattr(fmc.policy, o).get())
    with open (fn, 'w', encoding='utf-8') as jfile:
        jdata = json.dump(data, jfile, ensure_ascii=False, indent=2)
