import whois
from ipwhois import IPWhois

def check_whois_for_domain(ip):
    print('--------------------------------')
    print('WHOIS Info')
    print('--------------------------------')

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

def check_whois_for_ip(ip):
    print('\n')
    print('--------------------------------')
    print('WHOIS Info')
    print('--------------------------------')

    obj = IPWhois(ip)
    res = obj.lookup_whois()

    city = res["nets"][0]['city']
    if(city != None and city.strip() != ''):
        print('[+] Whois city found: ' + str(city))

    state = res["nets"][0]['state']
    if(state != None and state.strip() != ''):
        print('[+] Whois state found: ' + str(state))


    country = res["nets"][0]['country']
    if(country != None and country.strip() != ''):
        print('[+] Whois country found: ' + str(country))

    created = res["nets"][0]['created']
    if(created != None and created.strip() != ''):
        print('[+] Whois create date found found ' + str(created))

    updated = res["nets"][0]['updated']
    if(updated != None and updated.strip() != ''):
        print('[+] Whois update date found ' + str(updated))

    print('\n')
