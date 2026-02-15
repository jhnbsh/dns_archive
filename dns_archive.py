#!/usr/bin/python
# Program: dns_archive v1.2 (Python 2.7 compatible)
# Description:
# Generates a hosts file from websites.txt. Uses 30s DNS timeout.
# Timeouts / DNS failures are written as commented lines with a note.

import dns.resolver
import dns.exception

# Configure resolver and timeout
dnsResolve = dns.resolver.Resolver()
dnsResolve.lifetime = 30  # overall query timeout in seconds
dnsResolve.timeout = 30   # per-retry timeout

### START PROGRAM ###

print "\n Hello friend. \n The script is running.  Please wait. \n"

# Read websites from file
f = open("websites.txt", "r")
try:
    striped_websites = []
    for line in f:
        line = line.strip()
        if line:
            striped_websites.append(line)
finally:
    f.close()

# Open output host file
my_output = open("hosts.txt", "w")
try:
    my_output.write("# The contents of this file should be placed in:\n")
    my_output.write("# WINDOWS = C:\\Windows\\System32\\drivers\\etc\\hosts\n")
    my_output.write("# MACOS = /etc/hosts\n")
    my_output.write("# LINUX = /etc/hosts\n\n")
    my_output.write("# IP ADDRESSES \t WEBSITE\n")
    my_output.write("127.0.0.1 \t localhost\n")
    my_output.write("255.255.255.255 \t broadcasthost\n")
    my_output.write("::1 \t\t localhost ip6-localhost ip6-loopback\n")

    # Loop through websites and perform DNS queries
    for item in striped_websites:
        try:
            dns_grab = dnsResolve.query(item, "A")

            # Write each resolved IP
            for rdata in dns_grab:
                my_output.write("%s \t %s\n" % (str(rdata), item))

        except dns.exception.Timeout:
            # Timed out — include as commented out entry with note
            print "Timeout for %s, skipping but recording." % item
            my_output.write("# TIMEOUT \t %s (failed to resolve)\n" % item)
            continue

        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            # No DNS answer or domain not found — comment out
            print "No DNS answer for %s, skipping." % item
            my_output.write("# NOANSWER/NXDOMAIN \t %s (failed to resolve)\n" % item)
            continue

        except Exception as e:
            # Catch-all for any other lookup errors, comment out
            print "Error resolving %s: %s" % (item, str(e))
            my_output.write("# ERROR \t %s (failed: %s)\n" % (item, type(e).__name__))
            continue

finally:
    my_output.close()

### END PROGRAM ###
