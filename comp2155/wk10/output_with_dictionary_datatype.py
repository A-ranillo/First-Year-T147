from netmiko import ConnectHandler

connection = ConnectHandler(
    host="192.168.153.138",
    username="",
    password="",
    device_type="cisco_ios_telnet",
    secret="cisco1",
    port=30002
)

output = connection.send_command("show ip int brief", use_textfsm=True)
if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)

print(output)

# for result in output:
#     print(result["interface"])
#     print(result["ip_address"])
#     print(result["status"])