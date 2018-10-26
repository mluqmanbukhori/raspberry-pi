# this project can be practise on python programming
# read data character with tcp socket connection - for CLIENT
#   author: muhammad luqman bukhori
#   date  : 26/11/2018 - 08.20 WIB
#   edit  : -

import sys

# define HOST and PORT servers
HOST = 'host'   #replace your server localhost or TCP/IP on your connection
PORT = 28097    #replace your port connection ect. 8080 / 80 / ... any

# lets connect with socket server connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# looping programm, wait for data read
while True:
    data = sock.recv(1024)      # read data from server
    out = data.decode('ascii')  # convert to ascii data
    print (out)                 # print any character data
    if out == 'Z'
      break

# close connection      
sock.close()
