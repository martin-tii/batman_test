
import subprocess

import signal



MAC = '00:0e:8e:9d:b0:c2:' # you will need to verify this addres with ifconfig 

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(10)  



def get_interfaces():
    interfaces = []
    proc = subprocess.Popen(['batctl', 'n'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    i = 0
    for x in proc.stdout:
        aux = x.split()
        i += 1
        if i > 2:
            interfaces.append((aux[0]).decode("utf-8"))
            interfaces = list(dict.fromkeys(interfaces))
    return interfaces



def tcpdump():
    aux = []
    interface = get_interfaces()
    if len(interface) > 1:
        print('Available Interfaces: ')
        for node in range(len(interface)):
            print(node + 1 + ' ' + interface[node])
        dev = input("\nEnter the interface you would like to test : ")
    else:
        dev = interface[0]
    p = subprocess.Popen(["batctl", 'td', dev], stdout=subprocess.PIPE, bufsize=1)
    try:
        for line in iter(p.stdout.readline, b''):
            decoded=line.decode("utf-8")
            if 'BAT ' + MAC in decoded and not 'ttl 50' in decoded : 
            	aux2 = decoded.split('tq ')[1].split(',')[0]           	 
            	aux.append(aux2)
        p.stdout.close()
        p.wait()
    except Alarm:
    	return aux

