'''
import socket    
fqdn = socket.getfqdn()
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
ipAddre = socket.gethostbyaddr(hostname)

print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr) 
print(fqdn)

print(ipAddre)
#How to get the IP address of a client using socket
'''
import os

command = "hostname -I"
ip = os.system(command)

print(ip)
