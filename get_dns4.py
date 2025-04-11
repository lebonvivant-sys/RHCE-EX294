import dns.resolver

domain = "klaverviertjes.nl"
nameserver = "192.168.1.4"

def main():
    print('Opvragen A records {} met nameserver {}.'.format(domain,nameserver))
   
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(str(nameserver), domain))
        for name, node in zone.nodes.items():
            rdatasets = node.rdatasets
            for rdataset in rdatasets:
                for rdata in rdataset:
                    if rdataset.rdtype == 1:
                        print( name, ";",rdata)
        
    except Exception as e:
            print("[*] NS {} refused zone transfer!".format(nameserver))
   
if __name__ == '__main__':
    main()