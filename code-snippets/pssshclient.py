import paramiko


class CustomSSHClient:
    def __init__(self, hostname, port, user, passwd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname, port, user, passwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode('ascii')


if __name__ == '__main__':
    ssh = CustomSSHClient('192.168.43.223', 22, 'training', 'training')
    op = ssh.check_output('cal 1 2018')
    print(op)