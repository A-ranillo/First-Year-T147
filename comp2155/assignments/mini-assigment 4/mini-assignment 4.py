from netmiko import ConnectHandler

router_stuff = [
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":30001},
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":30002},
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":30005},
]

for i, stuff in enumerate(router_stuff, start=1):
    with open(f"router_{i}.txt", "w") as f:
        f.write(f"host: {stuff['host']}\n")
        f.write(f"username: {stuff['username']}\n")
        f.write(f"password: {stuff['secret']}\n")
        f.write(f"port: {stuff['port']}\n")

with open(f"ospf_routing_protocol.txt", "w") as f:
    f.write(f"router ospf 1")
    f.write(f"net 0.0.0.0 0.0.0.0 area 0")
    f.write(f"distance 110")
    f.write(f"default-information originate always")
    f.close()

command_stuff = (
    f"router ospf 1",
    f"network 0.0.0.0 0.0.0.0 area 0",
    f"distance 110",
    f"default-information originate always"
)

for stuff in router_stuff:
    connection = ConnectHandler(
        host=f"{stuff['host']}",
        username=f"{stuff['username']}",
        password="",
        device_type="cisco_ios_telnet",
        secret=f"{stuff['secret']}",
        port=stuff['port']
    )

    connection.enable()
    connection.config_mode()
    connection.send_config_set(command_stuff)
    connection.disconnect()