import psutil

# source: https://aprenderlinux.org/extraccion-de-informacion-de-hardware-y-sistema-linux-con-python/
# gathering all network interfaces (virtual and physical) from the system
if_addrs = psutil.net_if_addrs()

# printing the information of each network interfaces
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print("n")
        #print(f"Interface :", interface_name)
        if str(address.family) == 'AddressFamily.AF_INET':
            print("[+] IP Address :", address.address)
            #print("[+] Netmask :", address.netmask)
            #print("[+] Broadcast IP :", address.broadcast)
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            pass
            #print("[+] MAC Address :", address.address)
            #print("[+] Netmask :", address.netmask)
            #print("[+] Broadcast MAC :", address.broadcast)


#### Bateria, temperatura, ventiladores
battery = psutil.sensors_battery()
print("[+] Battery Percentage :", round(battery.percent, 1), "%")
print("[+] Battery time left :", round(battery.secsleft/3600, 2), "hr")
print("[+] Power Plugged :", battery.power_plugged)
