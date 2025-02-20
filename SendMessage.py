import socket
from datetime import datetime as dt

# The IP address of the device you want to send the message to. In this
# case, we are sending a message to all devices on the network because
# we are using the broadcast address. The port is a random port number
# that the test app will be listening on.
ip = "192.168.7.255"
port = 29110

# The reason that the content of message is the current time is to make
# it easy to see if the message is being received by the test app since
# the test app will display the message it receives and it will be
# obvious if the message is different than the previous one. However,
# the message you would send in your project is going to contain to
# follow a specific structure that meets the needs of your project.
msg = dt.now().strftime("%H:%M:%S.%f")

# Create a socket object that will be used to send the message. The
# first argument is the address family, which is AF_INET for IPv4. The
# second argument is the socket type, which is SOCK_DGRAM for UDP. The
# socket object is stored in the variable sock.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This line is required to send a message to the broadcast address. It
# tells the socket to send the message to all devices on the network.
# Attempting to send the message to the broadcast address without this
# line will result in a permission error.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# The message must be encoded to bytes before it can be sent over the
# network. This is because the network can only send bytes. The
# encoding used here is utf-8, which is a common encoding for text.
sock.sendto(msg.encode('utf-8'), (ip, port))

# The purpose of this line is confirmation that the message was sent.
# It is not required for the message to be sent, but it is helpful for
# debugging purposes.
print(f"Sent to {ip}:{port}")
print(f"Message: {msg}")

# Close the socket when done. This is important because the socket will
# remain open and continue to use resources until it is closed.
sock.close()
