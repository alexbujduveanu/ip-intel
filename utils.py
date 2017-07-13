import socket

# return true if valid, false if not
def check_ip_validity(ip):
    try:
        socket.inet_aton(ip)
        # legal
        return True
    except socket.error:
        # Not legal
        return False

def check_alexa_top_one_million(ip):
    # TODO check an ip against this list
    return
