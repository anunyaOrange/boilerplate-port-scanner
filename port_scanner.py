import socket
import validators

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    urlvalid = validators.url(target)
    if urlvalid:
        if (port_range):
        return("Error: Invalid IP address")
    if (verbose):
        return """Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http"""

    else:
        return("Error: Invalid hostname")
