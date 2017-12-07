
# reads from socket until "\r\n"
def read_from_socket(s):
    result = b""
    while 1:
        data = s.recv(256)
        if data[-2:] == b"\r\n":
            result += data[:-2]
            break
        result += data
#   if result != "":
#       print "read : %s" % result
    return result.decode("utf-8")

# sends all on socket, adding "\r\n"
def send_to_socket(s, msg):
#   print "respond : %s" % msg
    msg = str(msg)
    s.sendall(msg.encode("utf-8") + b"\r\n")
