# dns_archive v1.0 Help File

# Description:
  This python script generates a hostfile which can be used to access websites 
  in the event DNS is unavailable.  The input is a list of websites (see websites.txt)
  and the output is a hostfile for inclusion in your specific operating system.

# Why is this script needed?:
  You use DNS everyday as your browse the Internet and may not even realize it.
  Every website on the Internet has a unique IP address, and looks something like this:
  192.168.150.125 (example).  When accessing a website your device needs to know the
  website's unique address.  Similar as if you were going to mail a letter to a friend, 
  you need to know your friend's mailing address.  Unfortunately, remembering the IP
  addresses for all the websites you visit would be hard to do.  This is why DNS exists.
  DNS takes a website name (domain) such as Google.com, Facebook.com Amazon.com, etc., 
  and maps it to the website's IP address automatically so you don't have to remember it.
  
  There are a limited number of DNS servers around the world which create this mapping.
  Therefore it has long been theorized that if a nefarious individual or organization 
  were cause these servers to fail, then it would effectively bring the Internet down.
  In 2016 this actually happened to a small extent when a cyber attack occurred against
  the DNS provider Dyn (see link below for more information).
  
  This script is a method for a user to save the DNS information for websites of
  their choosing so they can be potentially accessed in the event of a future DNS
  outage.  The script generates a "host file" which is a manual mapping of websites to
  IP addresses which you can save on your computer.  Once created, your computer will
  first look at your local host file to see if it already knows the IP address of the
  website you are trying to access.  If you have already run this script and have the
  mapping, then you will not need DNS or any of the worldwide DNS servers.
  Note: in order to create the host file this script needs DNS to be available and 
  therefore must be run before any DNS outages.  It is recommended that you run this
  script in advance of any outages, save the host file, and update it as needed.

  Dyn attack:  https://www.wired.com/2016/10/internet-outage-ddos-dns-dyn/

# Prerequisites:
   Python v2 is needed to execute the script.  The following provides basic directions
   on installing Python on your respective operating system.

   Windows users: As of Windows 8.1 you will need to install Python v2, then dnspython.
   1.) Download and install python from https://www.python.org/downloads/
   Note: Choose any version of Python that starts with "2", not "3".
   2.) Select all default settings, except for on the 'Customize Python'
   screen click "Add python.exe to Path" and choose "Will be installed to local hard-drive".
   3.) Download dnspython from https://github.com/rthalley/dnspython
   4.) Create a folder in C: name 'dnspython' and extract the contents of the downloaded dnspython archive to C:\dnspython.
   5.) Click Start, type 'cmd', right click 'Command Prompt' and choose 'Run as administrator'
   6.) Run the following commands:
   	cd c:\dnspython
	python setup.py install

   MacOS users: As of MacOs Majave you will need to first install pip, then dnspython.
   From a Terminal window type the following:
   	sudo easy_install pip
	sudo pip install dnspython	
		
   Linux users:  None, both python and dns.resolver should be natively installed.

# Execution instructions
  Edit the provided websites.txt to include the websites (one-per-line) you wish to
  save DNS information for.  Recommended websites to include are those you might need to 
  access in the event of an emergency, such as: news outlets, medical information,
  maps, social media (for communications), and government or police assistance.  Once
  edited place websites.txt in the same directory as dns_archive.py.  
  Run dns_archive from a command prompt or terminal window with: 
  	 python dns_archive.py

# Editing and/or replacing your existing host file
  The following website provide directions on how to edit the host file on your
  respective operating system.  You will either need to copy/paste the contents of this
  script's output to your existing host file, or replace your existing host file entirely 
  based on your situation.  Do not forget to save your original host file somewhere
  safe so that you can revert back to it when needed.
    
   Modifying hostfiles: https://support.rackspace.com/how-to/modify-your-hosts-file/

