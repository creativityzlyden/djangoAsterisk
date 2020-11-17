import paramiko

host = 'host'
user = 'user'
secret = 'pass'
port = 22

client = paramiko.SSHClient()


def connect_asterisk():
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)


def start_asterisk():
    connect_asterisk()
    stdin, stdout, stderr = client.exec_command('ifconfig -a')
    data = stdout.read()
    print(data)


def restart_asterisk():
    connect_asterisk()
    stdin, stdout, stderr = client.exec_command('core restart gracefully')
    data = stdout.read()
    print(data)


def exit_asterisk():
    connect_asterisk()
    stdin, stdout, stderr = client.exec_command('exit')
    data = stdout.read()
    print(data)
