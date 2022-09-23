import paramiko

def sshClient(host, port, user, password, command):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password, port=port)
    _stdin, _stdout,_stderr = client.exec_command(command)
    print(_stdout.read().decode())
    client.close()

while True:
    cmd = input("enter the command: ")
    server_list = [
    {"user": "ubuntu", "pass": "password", "host": "localhost", "port": "2222"},
    {"user": "ubuntu", "pass": "password", "host": "localhost", "port": "3333"}
    ]

    for server in server_list:
        user = server["user"]
        password = server["pass"]
        host = server["host"]
        port = server["port"]
        sshClient2(host, port, user, password, cmd)
