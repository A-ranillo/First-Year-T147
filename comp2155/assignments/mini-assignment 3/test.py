import paramiko
import time
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname='192.168.153.139',
    username='root',
    password='pnet',
    port=22,
)

shell = client.invoke_shell()

command = shell.send(b"ls -la\n")
time.sleep(5) #wait for the response of command
response = shell.recv(1000000000000)
response = response.decode("utf-8")

time.sleep(2)

print(response)
# stdin, stdout, stderr = client.exec_command("telnet 192.168.153.138 30002", get_pty=True)
# print(stdout.read().decode())
# stdin.close()