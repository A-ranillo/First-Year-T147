from connect_to_linux import *

commands = "touch f1_fri_8am.txt,mkdir dir1_fri_8am".split(",")

#connection.send_config_set(commands)
connection.send_config_from_file("commands_linux.txt")

output = connection.send_command("ls")
print(output)