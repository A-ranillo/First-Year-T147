import napalm

driver = napalm.get_network_driver("ios")

device = driver(
    hostname="192.168.26.128",
    usernmae="",
    password="",
    optional_args={"port":30006, "secret":"cisco1"}
)