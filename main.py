import argparse
import os
import whois
import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", nargs='?', default="empty")
    parser.add_argument("-i", nargs='?', default="empty")

    args = parser.parse_args()

    # check if single IP or list of IPs
    if(args.l != 'empty'):
        print("Multiple IP case")
    elif(args.i != 'emtpy'):
        print("Single IP case")
        check_whois(args.i)
    else:
        print('Something went wrong')
        exit()

    exit()

def check_whois(ip):
    print('ip is ' + str(ip))
    domain = whois.whois(str(ip))

    print('[+] Whois org for ' + str(ip))
    print('\t' + domain['org'])

    print('[+] Whois country for ' + str(ip))
    print('\t' + domain['country'])

    print('[+] Whois registrar for ' + str(ip))
    print('\t' + domain['registrar'])

    print('[+] Whois create date for ' + str(ip))
    print('\t' + domain['creation_date'].strftime("%B %d, %Y"))

    # can have multiple dates, parse the first for now
    print('[+] Whois record update dates for ' + str(ip))
    for date in domain['updated_date']:
        print('\t' + date.strftime("%B %d, %Y"))
    exit()

if __name__ == '__main__':
    main()
