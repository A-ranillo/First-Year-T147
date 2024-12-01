from netmiko import ConnectHandler

router_stuff = [
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":3001},
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":3002},
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":3005},
]

for i, stuff in enumerate(router_stuff, start=1):
    connection = ConnectHandler(
        host=f"{stuff['host']}",
        username=f"{stuff['username']}",
        password="",
        device_type="cisco_ios_telnet",
        secret=f"{stuff['secret']}",
        port=stuff['port']
    )

