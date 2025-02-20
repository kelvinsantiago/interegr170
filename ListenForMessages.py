import socket

# An IP address of 0.0.0.0 means that the socket will listen for 
# messages on all network interfaces. This is useful when you want to
# listen for messages on a specific port from any device on the network.
# The port number is the same as the port number that the send script
# is sending messages to.
ip = "0.0.0.0"
port = 29110

# Create a socket object that will be used to listen for messages. The
# first argument is the address family, which is AF_INET for IPv4. The
# second argument is the socket type, which is SOCK_DGRAM for UDP. The
# socket object is stored in the variable sock.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port number. This tells the
# socket to listen for messages sent to the specified IP address and
# port number.
sock.bind((ip, port))

while True:

    # The recvfrom method is used to listen for messages. The first
    # argument is the maximum number of bytes that can be received in
    # the message.
    data, addr = sock.recvfrom(4096)

    # The message is received as bytes, so it must be decoded to a
    # string before it can be used. The encoding used here is utf-8,
    # which is a common encoding for text. The strip method is used to
    # remove any whitespace characters from the beginning and end of
    # the string.
    dataStr = data.decode("utf-8").strip()

    # Print the message to the console. This is useful for debugging
    # purposes. However, in a project such as the one for which you
    # are creating a controller, this message would be interpreted
    # as a command and used to control the device or enter data in
    # the corresponding spot.
    print(f"Received from: {addr}")
    print(f"Received message: {dataStr}")

    # If the message is "exit", the loop will break and the socket will
    # be closed. This is useful for stopping the script when you are
    # done testing without having to force quit the script.
    if dataStr == "exit":

        sock.close()
        break
