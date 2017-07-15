import urllib.request
import urllib.parse
from netaddr import IPNetwork, IPAddress

# global dict with URLs for each feed
FEEDS = {
    'spamhaus': 'https://www.spamhaus.org/drop/drop.txt',
    'tor': 'https://check.torproject.org/exit-addresses'
}

def check_spamhaus(ip_string):
    try:
        url = FEEDS['spamhaus']
        resp = urllib.request.urlopen(url)
        data = resp.read().decode('utf-8')

        for line in data.splitlines():
            print('line is ' + line)
            # skip lines that are comments
            if line.startswith(';') or line.rstrip() == '':
                print('line skipped')
                continue

            # example line looks like: 205.210.107.0/24 ; SBL210089
            # get only the CIDR portion
            cidr_string = line.split(';')[0].rstrip()
            print('cidr string is ' + cidr_string)
            if IPAddress(ip_string) in IPNetwork(cidr_string):
                print('[+] IP is on spamhaus drop list')
                return True
        return False
    except Exception as e:
        print('[-] Error encountered in Spamhaus feed function ' + str(e))
        return False

def check_tor(ip_string):
    exit_node_list = []
    try:
        url = FEEDS['tor']
        resp = urllib.request.urlopen(url)
        data = resp.read().decode('utf-8')

        # build list of current tor IPs
        for line in data.splitlines():
            if('ExitAddress' in line):
                ip = line.split(' ')[1]
                exit_node_list.append(ip)

        if(ip in exit_node_list):
            print('[+] IP is a tor exit node')
            return True
        else:
            return False
    except Exception as e:
        print('[-] Error in tor feed function')
        print(str(e))
        return False

def test_check_spamhaus():
    ip_to_test = '192.203.252.1'

    if(check_spamhaus(ip_to_test)):
        print('[+] Spamhaus threat feed test passed')
    else:
        print('[-] Spamhaus threat feed test failed')

def test_check_tor():
    ip_to_test = '185.165.168.186'

    if(check_tor(ip_to_test)):
        print('[+] Tor feed test passed')
    else:
        print('[-] Tor feed test failed')

# test_check_spamhaus()
# test_check_tor()
