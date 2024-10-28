print('Setup the Name Service')


def determine_device():
    while True:
        device_kind = str(input('ROUTER/SWITCH/FIREWALL/EXIT: '))
        if device_kind.lower() == 'router':
            break
        elif device_kind.lower() == 'switch':
            break
        elif device_kind.lower() == 'firewall':
            break
        elif device_kind.lower() == 'exit':
            print('Arigatou!')
            quit()
        else:
            print('Incorrect input! Try again!')

    return device_kind


def host_input():

    device_address = str(determine_device())

    automation_protocols = ['netmiko', 'paramiko', 'telnet']

    while True:
        ip = input(str('IP: '))
        hostname = input(str('Hostname: '))

        with open('/etc/hosts', 'a') as f:
            f.write(ip + ' ' + hostname + '\n')

        for protocol in automation_protocols:

            with open(f'/code-wev/configuration_push/network-infrastructure/{protocol}/devices/{device_address}_address.cfg', 'a') as i:
                i.write(ip + '\n')

        is_continue = input('Do you want to add more? Y/N: ')
        if is_continue.lower() == 'y':
            continue
        elif is_continue.lower() == 'n':
            print('Arigatou!')
            break
        else:
            print('Invalid Input!')


def modify_line(filename, line_number, new_content):
    # Read all lines from the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Check if the line_number is within the range
    if line_number < 1 or line_number > len(lines):
        print("Line number is out of range.")
        return

    # Modify the specified line (line_number is 1-based index)
    lines[line_number - 1] = new_content + '\n'

    # Write the updated lines back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)


def main():
    verify_usage = input('Add or Modify or Exit: ')
    if verify_usage.lower() == 'add':
        host_input()
    elif verify_usage.lower() == 'modify':
        line_number = int(input('Line #: '))
        hostname_ip = input('Enter new ip and hostname: ')
        modify_line('/etc/hosts', int(line_number), str(hostname_ip))
    elif verify_usage.lower() == 'exit':
        print('Arigatou!')
        quit()
    else:
        print('Wrong input! Please try again!')


if __name__ == '__main__':
    (main())
