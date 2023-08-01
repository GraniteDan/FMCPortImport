# FMCPortImport
API Import and Grouping of Common Protocol Port Objects into Cisco Firepower Managment Console

## PreReqs
This python script requires the addition of two non-standard libraries

## Purpose
This Script is being developed to read a CSV file of common protocol ports that are used within organzations and populate them into a Cisco Firepower Managment Console via the web api.
Often when configuring firewalls to perform internal segmentation of networks many firewall policies are needed and many common services are required for services such as client connections to Active Directory Domain Controllers, File and Print Servers, LDAP, NTP, and web servers.

The input file is configured in the following format where the "groups" column is a "/" delimited list of groups that the Port or service should be added to:


