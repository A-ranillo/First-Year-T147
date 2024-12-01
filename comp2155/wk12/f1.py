import telnetlib
import time

connection = telnetlib.Telnet(
    host="192.168.153.139",
    port=30001
)
#
# connection.read_until(b"Username: ", timeout=2)
# connection.write(b"\n")
# time.sleep(1)
# connection.read_until(b"Password: ", timeout=2)
# connection.write(b"cisco1\n")
# time.sleep(1)
connection.write(b"show ip int brief\n")
time.sleep(1)
connection.write(b"\n")
time.sleep(1)
output = connection.read_very_eager()
print(output.decode())