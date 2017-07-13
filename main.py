import argparse
import os
import datetime
from whois_info import *
from utils import *

def main():
    args = setup_argparse()

    # check if single IP or list of IPs
    # multiple IP implementation
    if(args.l != 'empty'):
        print("Multiple IP case")
    elif(args.i != 'emtpy'):
        print("Single IP case")
        check_whois_for_ip(args.i)
        reverse_lookup(args.i)
    else:
        print('Something went wrong')
        exit()

def setup_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", nargs='?', default="empty")
    parser.add_argument("-i", nargs='?', default="empty")
    return parser.parse_args()

# gets all domains corresponding to the IP
def reverse_lookup(ip):
    print('--------------------------------')
    print('DNS Info')
    print('--------------------------------')

    try:
        data = socket.gethostbyaddr(ip)
        domain = data[0]
        print('[+] Domain name is ' + domain)
    except Exception as e:
        print('[-] IP provided does not resolve')
    print('\n')

'''
    try:
        data = socket.gethostbyaddr(ip)
        for domain in data:
            hostname = str(domain)
            if 'in-addr.arpa' not in hostname and not check_ip_validity(hostname):
                print('[+] Domain name is ' + hostname)
    except Exception as e:
        print('[-] IP provided does not resolve')
    print('\n')
'''
# return true if valid, false if not
def check_ip_validity(ip):
    try:
        socket.inet_aton(ip)
        # legal
        return True
    except socket.error:
        # Not legal
        return False



if __name__ == '__main__':
    main()
