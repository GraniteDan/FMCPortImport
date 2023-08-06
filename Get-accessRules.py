from fireREST import FMC
import csv, json
from colors import red, green, blue, yellow, magenta, cyan
from getpass import getpass

h1 = """
################################################################################################

Access Policy Rule/Category Extraction Tool for Cisco FMC API

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
polname = input('Please Enter the Access Policy Name:')
objdata = fmc.policy.accesspolicy.get(name=polname)
objid=objdata['id']
catdata = fmc.policy.accesspolicy.category.get(container_uuid=objid)
poldata = fmc.policy.accesspolicy.accessrule.get(container_uuid=objid)
print(cyan(json.dumps(poldata, indent=2)))
print(yellow('#############################################################################################'))
print(green(json.dumps(catdata, indent=2)))

with open (polname + '_Policy_Rules', 'w', encoding='utf-8') as jfile:
    json.dump(poldata, jfile, ensure_ascii=False, indent=2)

with open (polname + '_Policy_Categories', 'w', encoding='utf-8') as jfile:
    json.dump(catdata, jfile, ensure_ascii=False, indent=2)
 
with open (polname + '_Policy', 'w', encoding='utf-8') as jfile:
    json.dump(objdata, jfile, ensure_ascii=False, indent=2)
