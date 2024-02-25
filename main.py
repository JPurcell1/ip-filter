import re
import_file = "sample_list.txt"

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_address = file.read()

ip_address = re.findall("\d+\.\d+\.\d+\.\d+", ip_address)

for address in ip_address:
  if address in remove_list:
    ip_address.remove(address)
  
print(ip_address)