from scapy.all import *
import binascii

network_adapter="VirtualBox Host-Only Network"

ether = Ether(
    # src = '00:04:d7:00:25:80',
    src = 'a8:a1:59:aa:53:d7',
    dst = '08:00:27:78:52:b7'
)

ip = IP(
    dst="192.168.1.1",
    src="192.168.1.3",
    ttl=128
)



def testpacket(data,destport=2002,delay=0):
    if delay > 0:
        time.sleep(delay)

    udp = UDP(

    sport=2000,
    dport=destport
    
    )
    payload = bytearray.fromhex(data)
    raw = payload
    
    # packet = ip/udp/raw
    packet = ether/ip/udp/raw
    # l3.send(packet)
    sendp(packet,iface=network_adapter, verbose=False) # sens packet on layer 2
    print(f'Sent: {data}')
    # l3.send(packet)
    # print(delay)
    # print(f'delay={delay}')
    # print(f'Sent package:{data}')
    # print(f'dport={destport}')

def t4interface(p):
    # time.sleep(.005)
    if p.haslayer('ARP'):
        print('arp found')
        if p['ARP'].psrc == '192.168.1.1':
            print('establish')

            arp = ARP(
                op = 2,
                psrc = '192.168.1.3',
                pdst = '192.168.1.1'
            )

            packet = ether/arp
            sendp(packet,iface=network_adapter) # sens packet on layer 2
        
    if p.haslayer('IP'):
        if p['IP'].dst == '192.168.1.3':
            if p.haslayer('UDP'):
                
                packet_data = binascii.hexlify(bytes(p[UDP].payload))
                print(f"udp received: {packet_data}")
                # time.sleep(.1)    
                data = p['Raw'].load
                destport = p['UDP'].sport
                # with open('out.csv', 'a', newline='') as f:
                #     writer = csv.writer(f)
                #     # write a row to the csv file
                #     writer.writerow(data)
                                    
                if packet_data == b'050900060014':
                                #    85 00 00 06 00 8b
                    bytepackage = '85000006008b'
                    testpacket(bytepackage,destport)

                # if packet_data == b'30000070001;':
                #     bytepackage = 'b300000900c0c9074c'
                #     testpacket(bytepackage,destport)

                if packet_data == b'00090006000f':
                    bytepackage = '8000001b00020010c90300d007303030346437303032646465006e'
                    testpacket(bytepackage,destport)

                if packet_data == b'040900060013':
                    bytepackage = '8416000600a0'
                    testpacket(bytepackage,destport)                    

                if packet_data == b'10090006001f':
                    bytepackage = '900000060096'
                    testpacket(bytepackage,destport)     
                                   #110900090001500a7e
                if packet_data == b'110900090001500a7e':
                    bytepackage = '910000060097'
                    # bytepackage = b'9200000d00558376ca75f40020'
                    testpacket(bytepackage,destport)    

                if packet_data == b'12090007001c3e':
                    bytepackage = '9200000d00558376ca75f40020'
                    testpacket(bytepackage,destport)    

                if packet_data == b'200900070083b3':
                    bytepackage = 'a000002600831f00808080800080808080800080beeb00000000ffffffff286201000000ef87'
                    testpacket(bytepackage,destport)    


                if packet_data == b'1309000900b80bf4dc':
                    bytepackage = '9300000800b80b5e'
                    testpacket(bytepackage,destport) 


                if packet_data == b'000000060006':
                    bytepackage = '8000001b00020010c90300d007303030346437303032646465006e' #echo
                    testpacket(bytepackage)
                                    # 04000006000a
                if packet_data == b'04000006000a':
                    bytepackage = '8416000600a0'
                    testpacket(bytepackage)

                if packet_data == b'0300000600':
                    bytepackage = '8416000600a0'
                    testpacket(bytepackage)
                                    
                if packet_data == b'05000006000b':
                    bytepackage = '85000006008b'
                    testpacket(bytepackage)

                if packet_data == b'3300000700013b':
                    bytepackage = 'b300000900c0c9074c'
                    testpacket(bytepackage)