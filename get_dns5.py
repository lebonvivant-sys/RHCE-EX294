#!/usr/bin/env python3
import dns.resolver
import yaml
domain = "klaverviertjes.nl"
nameserver = "192.168.1.4"
contents = {}
line = ""
line2 = ""

def main():
    print('Opvragen A records {} met nameserver {}.'.format(domain,nameserver))
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(str(nameserver), domain))
        for name, node in zone.nodes.items():
            rdatasets = node.rdatasets
            for rdataset in rdatasets:
                for rdata in rdataset:
                    if rdataset.rdtype == 1:
                        line = "{}".format(name)
                        line2 = "{}".format(rdata)
                        contents.update({line:line2})
                        print(contents)
        
    except Exception as e:
            print("Error e: {} ".format(e))#
    
    print("Inhoud van contents lijst: {}".format(contents))
  
    print(yaml.dump(contents,default_style=None, explicit_start=True, default_flow_style=False))
      
if __name__ == '__main__':
    main()