#!/usr/bin/env python

import  socket
import  messages_robocup_ssl_wrapper_pb2
from grSim_Commands_pb2 import grSim_Commands, grSim_Robot_Command

multicast_if_addr='192.168.3.9'
multicast_group='224.5.23.2'
multicast_port=10020

my_addr='0.0.0.0'
server_address=(my_addr, multicast_port)

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

mreq=socket.inet_aton(multicast_group)+socket.inet_aton(multicast_if_addr)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#make protobuf instance
ssl_wrapper = messages_robocup_ssl_wrapper_pb2.SSL_WrapperPacket()

while True:

    data    = sock.recv(1024)
    ssl_wrapper.ParseFromString(data)
    print   '-------------------------------------------'
    print   ssl_wrapper
