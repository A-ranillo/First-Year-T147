from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type="cisco_ios_telnet",
    host="192.168.153.139",
    username="",
    password="",
    port=30002,
    secret="cisco1"
)
connection.enable()
connection.config_mode()
connection.send_command("username november privilege 15 secret HelloWorld!")
connection.disconnect()
