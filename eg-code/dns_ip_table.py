#!/bin/env python


# simple script to print nodes' published DNS hostname and IP address
# using "nslookup"

# 

# need DNSPython: 
#import dns.resolver


#answers = dns.resolver.query('dnspython.org', 'MX')
#for rdata in answers:
#    print 'Host', rdata.exchange, 'has preference', rdata.preference


# for ping: 
# http://stackoverflow.com/questions/2953462/pinging-servers-in-python
# for capturing status but not output: 
# http://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on

import socket
#import os
import commands
#host = "bluespace-1-1-ctl"
#ip = socket.gethostbyname( host )

host_list = []

# chassis ctl
host_list.append( "bluespace-ctl" )     # 1st chassis has special naming
for y in [2,3,5,6]:
        host = "bluespace" + str(y) + "-ctl"
        host_list.append( host )

# blade ctl
for y in [1,2,3,5,6]:
    for x in range( 1, 17 ):            # last number not included, ie will not process for 17.
        host = "bluespace-" + str(y) + "-" + str(x) + "-ctl"
        host_list.append( host )
# stand alone node.  Note: no 4-2 or 4-3
host_list.append( "bluespace-4-1-ctl" )
y = 4
for x in range( 4, 11 ):
        host = "bluespace-" + str(y) + "-" + str(x) + "-ctl"
        host_list.append( host )
y = 7
for x in range( 1, 6 ):
        host = "bluespace-" + str(y) + "-" + str(x) + "-ctl"
        host_list.append( host )


#print( host_list )
# lookup ip and ping
for host in host_list:
        #print( "looking up " + host + "..." )
        ip = socket.gethostbyname( host )
        response = 0
        #response = os.system("ping -c 1 " + host )
        #response, output = commands.getstatusoutput("ping -c 1 " + host )       # not pingable takes a long time.  multi-thread?
        if response == 0: 
                ping_status = "pingable"
        else:
                ping_status = "NOT_pingable"
        outputline = host + "\t" + ip + "\t" + ping_status
        print( outputline )

