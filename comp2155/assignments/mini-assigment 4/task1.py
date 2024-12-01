router_stuff = [
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":3001},
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":3002},
    {"host":"192.168.153.139","username":"","secret":"cisco1","port":3005},
]

for i, stuff in enumerate(router_stuff, start=1):
    with open(f"router_{i}.txt", "w") as f:
        f.write(f"host: {stuff['host']}\n")
        f.write(f"username: {stuff['username']}\n")
        f.write(f"password: {stuff['secret']}\n")
        f.write(f"port: {stuff['port']}\n")
