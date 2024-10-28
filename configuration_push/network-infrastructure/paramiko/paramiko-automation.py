import paramiko
import datetime
import getpass
from time import sleep


def user_input():
    user_name = input("Username: ")
    return user_name


def pass_input():
    pass_word = getpass.getpass()
    return pass_word


def boarder_line(inp):
    print(f'''***********************************{inp}***********************************************''')


def date_now():
    date_time = datetime.datetime.now()
    return date_time


def main():
    username = user_input()
    password = pass_input()

    with open("ip_address.cfg", "r") as ip:
        ip_address = ip.read().splitlines()

    with open("configs.cfg", "r") as conf:
        config_file = conf.read()

    for i in ip_address:

        net_connect = paramiko.SSHClient()
        net_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        net_connect.connect(i, username=username, password=password, port=22)

        boarder_line(i)

        device_connect = net_connect.invoke_shell()
        device_connect.send(b'config t\n')
        device_connect.send(bytes(config_file.encode('ascii')))
        sleep(0.5)

        output = device_connect.recv(65535).decode('ascii')
        print(output)

        time = date_now()
        print(time)


if __name__ == '__main__':
    main()

