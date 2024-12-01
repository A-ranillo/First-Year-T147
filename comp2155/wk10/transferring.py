from netmiko import ConnectHandler, file_transfer

connection = ConnectHandler(
    host="192.168.153.139",
    username="root",
    password="pnet",
    device_type="linux",
    port=22
)
direction = "put" #put local => remote; get remote => local
src_file = "./output_with_dictionary_datatype.py"
dst_file = "./shorky.py"
file_system_root = "/root"



result = file_transfer(
    ssh_conn=connection,
    source_file=src_file,
    dest_file=dst_file,
    direction=direction,
    file_system=file_system_root
)

print(result)