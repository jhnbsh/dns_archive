#!/usr/bin/python
# Program: dns_archive v1.2
# Description:
# This python script generates a hostfile which can be used to access websites
# in the event DNS is unavailable. The input is a list of websites (see websites.txt)
# and the output is a hostfile for inclusion in your specific operating system.
# A 30s timeout will skip websites that either timeout or no longer exist.
# Errors and all relevant DNS exceptions will also be commented into the results.

import dns.resolver

# Configure resolver and timeout
dnsResolve = dns.resolver.Resolver()
dnsResolve.lifetime = 30  # overall query timeout in seconds
dnsResolve.timeout = 30   # per-retry timeout

### START PROGRAM ###

print(
    "\n Hello friend. \n The script is running.  Please wait. \n"
)

# Read websites from file
with open("websites.txt", "r") as f:
    striped_websites = [elem.strip() for elem in f if elem.strip()]

# Open output host file
with open("hosts.txt", "w") as my_output:
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
                my_output.write(f"{rdata} \t {item}\n")

        except dns.exception.Timeout:
            # Timed out — include as commented out entry with note
            print(f"Timeout for {item}, skipping but recording.")
            my_output.write(f"# TIMEOUT \t {item} (failed to resolve)\n")
            continue

        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            # No DNS answer or domain not found — comment out
            print(f"No DNS answer for {item}, skipping.")
            my_output.write(f"# NOANSWER/NXDOMAIN \t {item} (failed to resolve)\n")
            continue

        except Exception as e:
            # Catch-all for any other lookup errors, comment out
            print(f"Error resolving {item}: {e}")
            my_output.write(
                f"# ERROR \t {item} (failed: {type(e).__name__})\n"
            )
            continue

### END PROGRAM ###
