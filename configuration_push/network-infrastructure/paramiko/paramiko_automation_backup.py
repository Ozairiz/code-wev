import paramiko
import datetime
import getpass
import re
from time import sleep


def user_input():
    return input("Username: ")


def pass_input():
    return getpass.getpass()


def border_line(inp):
    print(f'***********************************{inp}***********************************************')


def date_now():
    return datetime.datetime.now()


def extract_hostname(config_output):
    """Extract the hostname from the configuration output."""
    # Use a regular expression to find the hostname in the output
    match = re.search(r'hostname (\S+)', config_output)
    if match:
        return match.group(1)
    else:
        return 'unknown'


def determine_device():
    while True:
        while True:
            ask_device_kind = str(input(f'''

            #########################################################
            #               CHOOSE A DEVICE TYPE:                   #
            #                      ROUTER                           #
            #                      SWITCH                           #
            #                      FIREWALL                         #
            #                                                       #
            #                        or                             #
            #                                                       #
            #                        ALL                            #
            #               EXIT                                    #
            #                                                       #
            ################## ENTER YOUR CHOICE: ###################
                                        '''))

            if ask_device_kind.lower() == 'router':
                break
            elif ask_device_kind.lower() == 'switch':
                break
            elif ask_device_kind.lower() == 'firewall':
                break
            elif ask_device_kind.lower() == 'all':
                break
            elif ask_device_kind.lower() == 'exit':
                print('Arigatou!')
                quit()
            else:
                print('Incorrect input! Try again!')

        return ask_device_kind


def main():

    device_kind = str(determine_device())

    if device_kind == 'all':
        all_device = ['router', 'switch']

        username = user_input()
        password = pass_input()

        for device in all_device:

            with open(f"/code-wev/configuration_push/network-infrastructure/paramiko/devices/{device}_address.cfg",
                      "r") as ip_file:
                ip_addresses = ip_file.read().splitlines()

            for ip in ip_addresses:
                print(f"Processing {ip}...")

                # Setup SSH connection
                net_connect = paramiko.SSHClient()
                net_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy)
                net_connect.connect(ip, username=username, password=password, port=22)

                border_line(ip)

                # Invoke shell and send command
                device_connect = net_connect.invoke_shell()
                device_connect.send(b'terminal length 0\n')  # Disable pagination
                sleep(1)
                device_connect.send(b'show run\n')
                sleep(2)  # Wait a bit for the command to start processing

                # Read output
                output_container = b''
                while True:
                    if device_connect.recv_ready():
                        data = device_connect.recv(4096)
                        output_container += data
                        if b'--More--' in data:
                            device_connect.send(b' ')
                        elif b'#' in data and not device_connect.recv_ready():
                            break
                        sleep(0.5)

                # Decode output to string
                output_str = output_container.decode('ascii')

                # Extract hostname
                hostname = extract_hostname(output_str)

                # Use hostname to name the backup file
                if hostname == 'unknown':
                    filename = f'/code-wev/configuration_push/network-infrastructure/paramiko/device_backups/{device}/{ip}_backup.cfg'
                else:
                    filename = f'/code-wev/configuration_push/network-infrastructure/paramiko/device_backups/{device}/{hostname}.cfg'

                # Write output to file
                with open(filename, 'w') as file:
                    file.write(output_str)

                print(f"Configuration from {ip} saved as {filename}.")
                print(date_now())

                # Close connection
                net_connect.close()

    else:

        username = user_input()
        password = pass_input()

        with open(f"/code-wev/configuration_push/network-infrastructure/paramiko/devices/{device_kind}_address.cfg",
                  "r") as ip_file:
            ip_addresses = ip_file.read().splitlines()

        for ip in ip_addresses:
            print(f"Processing {ip}...")

            # Setup SSH connection
            net_connect = paramiko.SSHClient()
            net_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            net_connect.connect(ip, username=username, password=password, port=22)

            border_line(ip)

            # Invoke shell and send command
            device_connect = net_connect.invoke_shell()
            device_connect.send(b'terminal length 0\n')  # Disable pagination
            sleep(1)
            device_connect.send(b'show run\n')
            sleep(2)  # Wait a bit for the command to start processing

            # Read output
            output_container = b''
            while True:
                if device_connect.recv_ready():
                    data = device_connect.recv(4096)
                    output_container += data
                    if b'--More--' in data:
                        device_connect.send(b' ')
                    elif b'#' in data and not device_connect.recv_ready():
                        break
                    sleep(0.5)

            # Decode output to string
            output_str = output_container.decode('ascii')

            # Extract hostname
            hostname = extract_hostname(output_str)

            # Use hostname to name the backup file
            if hostname == 'unknown':
                filename = f'/code-wev/configuration_push/network-infrastructure/paramiko/device_backups/{device_kind}/{ip}_backup.cfg'
            else:
                filename = f'/code-wev/configuration_push/network-infrastructure/paramiko/device_backups/{device_kind}/{hostname}.cfg'

            # Write output to file
            with open(filename, 'w') as file:
                file.write(output_str)

            print(f"Configuration from {ip} saved as {filename}.")
            print(date_now())

            # Close connection
            net_connect.close()


if __name__ == '__main__':
    main()
