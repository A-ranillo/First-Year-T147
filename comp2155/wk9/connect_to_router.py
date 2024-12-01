from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type="cisco_ios_telnet",
    host="192.168.153.138",
    username="",
    password="",
    port=30002,
    secret="cisco1"
)