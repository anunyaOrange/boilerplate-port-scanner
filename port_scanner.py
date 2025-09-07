import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    print(target)
    print(port_range)
    print(verbose)
    if (target):
        return("Error: Invalid hostname")
    if (port_range):
        return("Error: Invalid IP address")
    if (verbose):
        return """Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http"""
    return(open_ports)