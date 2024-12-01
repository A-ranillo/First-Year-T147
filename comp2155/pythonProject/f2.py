import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname='192.168.153.138',
    username='root',
    password='pnet',
    port=22,
)

stdin, stdout, stderr = client.exec_command("fastfetch", get_pty=True)
stdin.write("test3\n")
stdin.write("test3\n")
stdin.close()