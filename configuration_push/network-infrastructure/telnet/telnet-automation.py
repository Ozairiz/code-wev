#!/bin/python3

import telnetlib
import datetime
import getpass


def user_input():
    user_name = input("Username: ")
    return user_name


def pass_input():
    pass_word = getpass.getpass()
    return pass_word


def connect_network():
    with open('ip_address.txt') as p:
        ip_address = p.read().splitlines()

        username = user_input()
        password = pass_input()

        for ip in ip_address:
            tn = telnetlib.Telnet(ip)
            tn.read_until(b'Username: ')
            tn.write(username.encode('ascii') + b'\n')
            if password:
                tn.read_until(b'Password: ')
                tn.write(password.encode('ascii') + b'\n')

                tn.write(b'enable\n'),
                tn.write(b'cisco\n'),
                tn.write(b'config t\n'),
                tn.write(b'int l30\n'),
                tn.write(b'ip address 30.30.30.30 255.255.255.255\n'),
                tn.write(b'description LOOPBACK30!!!\n'),
                tn.write(b'end\n'),
                tn.write(b'exit\n'),

                print(tn.read_all().decode('ascii'))

        time = datetime.datetime.now()
        print(time)

 if __name__ ==  '__main__' 
 connect_network()

# enhance how to add the interfaces (i.e for loop)
