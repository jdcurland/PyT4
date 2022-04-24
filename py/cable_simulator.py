from scapy.all import *
import csv
from threading import Thread
from collections import deque

import byte_logic
from byte_logic import t4interface


network_adapter="VirtualBox Host-Only Network"

conf.layers.filter([Ether, IP, UDP, ARP])

packetqueue = deque()



def add_packetqueue(pkt: Packet):
    packetqueue.append(pkt)

def read_packetqueue():
    while True:
        queue_length = len(packetqueue)
        print(queue_length, end='\r')
        if queue_length > 0:
            packet = packetqueue.popleft()
            t4interface(packet)
            
        else:
            time.sleep(.05)
        

thread = Thread(target=read_packetqueue, daemon=True)
thread.start()
print('start')
# sniff(iface=network_adapter, prn=byte_logic.t4interface, store=0)
sniff(iface=network_adapter, prn=add_packetqueue, store=0)