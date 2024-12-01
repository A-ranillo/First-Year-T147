import paramiko
import time
from datetime import datetime


class SSHUwU:
    def __init__(self):
        self.__hostname='192.168.153.139'
        self.__username='root'
        self.__password='pnet'
        self.__port=22
        self.__ssh_client = paramiko.SSHClient()
        self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__ssh_client.connect(hostname=str(self.__hostname), username=str(self.__username), password=str(self.__password), port=int(str(self.__port)))
        self.__shell = None
        self.__output = None

    def ssh_runner(self):
        self.__shell = self.__ssh_client.invoke_shell()

    def commandline(self):
        shell = self.__ssh_client.invoke_shell()
        shell.send(b"ll\n")
        time.sleep(5)
        output = shell.recv(10000000000)
        self.__output = output.decode("utf-8")
        return self.__output

    def exec_command(self):
        stdin, stdout, stderr = self.__ssh_client.exec_command("ll", get_pty=True)
        self.__output = stdout.read().decode()
        return self.__output

    def __del__(self):
        self.__ssh_client.close()

    def save_output(self):
        today = datetime.now()
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        hour = today.strftime("%H")
        minutes = today.strftime("%M")
        with open(f"command_{day}_{month}_{year}-{hour}_{minutes}.txt", 'w') as file:
            file.write(self.__output)
        return