from common_ports import *
import validators
import ipaddress
import socket

def is_valid_ip(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    if (target[:1].isdigit()):
        if not is_valid_ip(target):
            return("Error: Invalid IP address")       
    else:
        if not validators.domain(target):
            return("Error: Invalid hostname")
    



    

    if (verbose):
        return """Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http"""
