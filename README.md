# FMCPortImport
API Import and Grouping of Common Protocol Port Objects into Cisco Firepower Managment Console

## Pre-Requisits
This python script requires the addition of two non-standard libraries (fireREST, and ansicolors).  These pre-requisits can be installed using the pip:

**pip install ansicolors fireREST**


## Purpose
This Script is being developed to read a CSV file of common protocol ports that are used within organzations and populate them into a Cisco Firepower Managment Console via the web api.
Often when configuring firewalls to perform internal segmentation of networks many firewall policies are needed and many common services are required for services such as client connections to Active Directory Domain Controllers, File and Print Servers, LDAP, NTP, and web servers.  Not making any comparison around overall functionality of devices but I have found that Fortigate firewalls tend to have many useful services and service groups defined out of the box, which make OOB configurations or reconfigurations much easier. So I wanted to design away to predefine a bunch of services out of the gate.

The input file is configured in the following format where the "groups" column is a "/" delimited list of groups that the Port or service should be added to (Stand-alone Services that will not be added to groups can have groups column left empty):

|name	| port	| protocol	| groups |
|-----|-------|----------|--------|
| MS_SMB	| 445	| tcp	| AD/FileAndPrint |
|MS_NETBIOS_DATAGRAM |138	| udp	| AD/FileAndPrint |
| ADDS_KERBEROS	| 88	| tcp	| AD |
| ADDS_KERBEROS_PASSWD	| 464	| tcp	| AD |
| DHCP | 87-88 | udp | |
| MS-SQL | 1433 | tcp | |
