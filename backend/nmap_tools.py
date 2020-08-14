import nmap3
import sys

def scan_ips_handler(subnet):
    ip =subnet +'/24'
    nmap = nmap3.NmapScanTechniques()
    res =nmap.nmap_ping_scan(ip)
    return res

def scan_ips(subnet):
    ips_alive =scan_ips_handler(subnet)
    ips=[]
    for ip_objet in ips_alive:
        if ip_objet['state']=='up':
            ip = ip_objet['addresses'][0]['addr']
            ips.append(ip)
    return ips

if __name__=="__main__":
    scan_ips(sys.argv[1])
