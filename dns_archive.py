#!/usr/bin/python

# Program: dns_archive v1.1
# Description:
#     This python script generates a hostfile which can be used to access websites 
#     in the event DNS is unavailable. The input is a list of websites (see websites.txt)
#     and the output is a hostfile for inclusion in your specific operating system.

# Required modules
import dns.resolver

# Variable descriptions
dnsResolve = dns.resolver.Resolver()
dnsResolve.lifetime = 30  # Set timeout to 30 seconds

### START PROGRAM ###
print '\n Hello friend. The script is running.  Please wait. \n'

# Open the website list and remove any whitespace.
my_websites = list(open('websites.txt', 'r'))
striped_websites = [elem.strip() for elem in my_websites]

# Create hostfile.
my_output = open('hosts.txt', 'w')
my_output.write('# The contents of this file should be placed in:' + '\n')
my_output.write('# WINDOWS = C:\Windows\System32\drivers\etc\hosts' + '\n')
my_output.write('# MACOS = /etc/hosts' + '\n')
my_output.write('# LINUX = /etc/hosts' + '\n\n')
my_output.write('# IP ADDRESSES' + '\t' + 'WEBSITE' + '\n')

# Set default localhost information.
my_output.write('127.0.0.1' + '\t' + 'localhost' + '\n')
my_output.write('255.255.255.255' + '\t' + 'broadcasthost' + '\n')
my_output.write('::1' + '\t\t' + 'localhost ip6-localhost ip6-loopback' + '\n')

# Loop through websites and perform a DNS query on each.
for item in striped_websites:
    try:
        dns_grab = dnsResolve.query(item, "A")

        # Inner loop to print multiple DNS listings for host and print corresponding hostname.
        for rdata in dns_grab:  # for each response
            my_output.write(str(rdata) + '\t')
            my_output.write(('{}'*len(item)).format(*item) + '\n')

    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        print(f"Skipping {item}: No response or DNS error.")
        continue

my_output.close()

### END PROGRAM ###
