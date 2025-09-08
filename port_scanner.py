from common_ports import *
import validators
import ipaddress
import sys
import socket

def is_valid_ip(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    targetIP = ""
    if (target[:1].isdigit()):
        if not is_valid_ip(target):
            return("Error: Invalid IP address")
        else:
            targetIP = target
    else:
        if not validators.domain(target):
            return("Error: Invalid hostname")
        else:
            try:
                targetIP = socket.gethostbyname(target)
            except socket.gaierror:
                return("Error: Invalid hostname")
    
    lines = [f"Open ports for {target} ({targetIP})"]
    lines.append("PORT     SERVICE")

    try:
        for port in range(port_range[0],port_range[1]):
            print(f"start with TARGET: {target} PORT: {port}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((targetIP,port))
            if result ==0:
                print("Port {} is open".format(port))
                lines.append(f"{port}")
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

    

    if (verbose):
        joined_string = "\n".join(lines)
        print(joined_string)
        return joined_string
#         return """Open ports for scanme.nmap.org (45.33.32.156)
# PORT     SERVICE
# 22       ssh
# 80       http"""
    return 1
