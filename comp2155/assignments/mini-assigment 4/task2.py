with open(f"ospf_routing_protocol.txt", "w") as f:
    f.write(f"router ospf 1")
    f.write(f"0.0.0.0 0.0.0.0 area 0")
    f.write(f"110")
    f.write(f"default-information originate always")