from netmiko import ConnectHandler

connection = ConnectHandler(
    host="192.168.153.138",
    username="root",
    password="pnet",
    port=22,
    device_type="linux"
)