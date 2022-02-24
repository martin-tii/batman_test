import re
import subprocess

def parse_info(interface):
    info = {}
    rx = re.findall("RX packets [0-9]*\s", interface)  # find all matches for mtu
    if (len(rx) > 0):
        info['RX'] = rx[0].replace("RX packets", "").strip()  # use the first match
    tx = re.findall("TX packets [0-9]*\s", interface)  # find all matches for mtu
    if (len(tx) > 0):
        info['TX'] = rx[0].replace("TX packets", "").strip()  # use the first match
    inetMatches = re.findall("inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\s",
                             interface)  # find all matches for inet
    if (len(inetMatches) > 0):
        info['inet'] = inetMatches[0].replace("inet", "").strip()  # use the first match
    # add more here
    return info

def parse_name(interface):
    parts = interface.split(":")
    return parts[0]  # grab the name

def parse_interface(interface):
    name = parse_name(interface)
    info = parse_info(interface)
    return name, info

def parse_file(data):
    interfaces = data.split("\n\n")
    parsed = {}
    for interface in interfaces:
        name, info = parse_interface(interface)
        parsed[name] = info
    return parsed

Interface = "enxa0cec8ddd84e" # you will need to specify the interface
output1 = subprocess.check_output(["ifconfig", Interface])
print(parse_file(output1.decode('utf-8'))) # store it in a variable and process it

