import urllib.request
import urllib.parse
from netaddr import IPNetwork, IPAddress

# global dict with URLs for each feed
FEEDS = {
    'spamhaus': 'https://www.spamhaus.org/drop/drop.txt'
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

def test_check_spamhaus():
    ip_to_test = '192.203.252.1'
    if(check_spamhaus(ip_to_test)):
        print('[+] Spamhaus threat feed test passed')
    else:
        print('[-] Spamhaus threat feed test failed')

test_check_spamhaus()
