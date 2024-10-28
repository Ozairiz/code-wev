from netmiko import ConnectHandler
from jinja2 import Template
import datetime
import getpass
import stat
import csv
import os

from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException


def user_input():
    user_name = input('Username: ')
    return user_name


def pass_input():
    pass_word = getpass.getpass()
    return pass_word


def divider(p):
    print(f'*******************************************{p}***********************************************')


def time_now():
    time = datetime.datetime.now()
    print(time)


def eigrp_protocol():
    eigrp_configs = ''

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_template/routing_eigrp_jinja.cfg', 'r') as eigrp_j:
        eigrp_template = Template(eigrp_j.read(), keep_trailing_newline=True)

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_input/eigrp_input.csv', 'r') as eigrp_csv:
        eigrp_source = csv.DictReader(eigrp_csv)

        for eigrp_row in eigrp_source:
            eigrp_configs_raw = eigrp_template.render(
                protocol=eigrp_row['Protocol'],
                as_number=eigrp_row['AS-number'],
                network_address=eigrp_row['Network-Address'],
                wildcard_mask=eigrp_row['Wildcard-Mask']
            )

            eigrp_configs += eigrp_configs_raw

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/eigrp_config.cfg', 'w') as e:
        e.write(eigrp_configs)
        os.chmod('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/eigrp_config.cfg', stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        print('EIGRP Template has created!!!')


def ospf_protocol():
    ospf_configs = ''

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_template/routing_ospf_jinja.cfg', 'r') as ospf_j:
        ospf_template = Template(ospf_j.read(), keep_trailing_newline=True)

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_input/ospf_input.csv', 'r') as ospf_csv:
        ospf_source = csv.DictReader(ospf_csv)

        for ospf_row in ospf_source:
            ospf_configs_raw = ospf_template.render(
                protocol=ospf_row['Protocol'],
                as_number=ospf_row['AS-number'],
                network_address=ospf_row['Network-Address'],
                wildcard_mask=ospf_row['Wildcard-Mask'],
                area_number=ospf_row['Area-Number']
            )

        ospf_configs += ospf_configs_raw

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/ospf_config.cfg', 'w') as o:
        o.write(ospf_configs)
        os.chmod('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/ospf_config.cfg', stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        print('OSPF Template has created!!!')


def rip_protocol():
    rip_configs = ''

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_template/routing_rip_jinja.cfg', 'r') as rip_r:
        rip_template = Template(rip_r.read(), keep_trailing_newline=True)

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_input/rip_input.csv', 'r') as rip_csv:
        rip_source = csv.DictReader(rip_csv)

        for rip_row in rip_source:
            rip_configs_raw = rip_template.render(
                protocol=rip_row['Protocol'],
                network_address=rip_row['Network-Address']
            )

        rip_configs += rip_configs_raw

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/rip_config.cfg', 'w') as r:
        r.write(rip_configs)
        os.chmod('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/rip_config.cfg', stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        print('RIP Template has created!!!')


def bgp_protocol():
    bgp_configs = ''

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_template/routing_bgp_jinja.cfg', 'r') as bgp_b:
        bgp_template = Template(bgp_b.read(), keep_trailing_newline=True)

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_input/bgp_input.csv', 'r') as bgp_csv:
        bgp_source = csv.DictReader(bgp_csv)

        for bgp_row in bgp_source:
            bgp_configs_raw = bgp_template.render(
                protocol=bgp_row['Protocol'],
                as_number=bgp_row['AS-number'],
                router_id=bgp_row['Router-ID'],
                neighbor_1=bgp_row['Neighbor1'],
                remote_as1=bgp_row['Remote-AS1'],
                neighbor_2=bgp_row['Neighbor2'],
                remote_as2=bgp_row['Remote-AS2'],
                af_1=bgp_row['AF1'],
                af1_neighbor=bgp_row['AF1-neigbor'],
                af1_network=bgp_row['AF1-network'],
                af1_mask=bgp_row['AF1-mask'],
                af2_neighbor=bgp_row['AF2-neigbor'],
                af2_network=bgp_row['AF2-network'],
                af2_mask=bgp_row['AF2-mask'],
                af3_neighbor=bgp_row['AF3-neigbor'],
                af3_network=bgp_row['AF3-network'],
                af3_mask=bgp_row['AF3-mask']
            )

        bgp_configs += bgp_configs_raw

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/bgp_config.cfg', 'w') as b:
        b.write(bgp_configs)
        os.chmod('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/bgp_config.cfg', stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        print('BGP Template has created!!!')


def interface_config():

    interface_configs = ''

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_template/jinja_interface_template.cfg') as j:
        interface_jinja_template = Template(j.read(), keep_trailing_newline=True)

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/config_input/interface_input.csv') as s:
        interface_file = csv.DictReader(s)

        for row in interface_file:
            interface_config_raw = interface_jinja_template.render(
                interface=row['Interface'],
                ip=row['IP'],
                description=row['Description'],
                bandwidth=row['Bandwidth']
            )

            interface_configs += interface_config_raw

    with open('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/interface_config.cfg', 'w') as int:
        int.write(interface_configs)
        os.chmod('/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/interface_config.cfg', stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        print('Interface Template has created!!!')


def determine_device():
    while True:
        ask_device_kind = str(input(f'''
        
        #########################################################
        #               CHOOSE A DEVICE TYPE:                   #
        #                      ROUTER                           #
        #                      SWITCH                           #
        #                      FIREWALL                         #
        #               EXIT                                    #
        #                                                       #
        ###################ENTER YOUR CHOICE: ###################
                                 '''))

        if ask_device_kind.lower() == 'router':
            break
        elif ask_device_kind.lower() == 'switch':
            break
        elif ask_device_kind.lower() == 'firewall':
            break
        elif ask_device_kind.lower() == 'exit':
            print('Arigatou!')
            quit()
        else:
            print('Incorrect input! Try again!')

    return ask_device_kind


def main():

    while True:

        lets_begin = input(f'''
            #######################################
            #         * LET'S PROCEED... *        #
            #                                     #
            #               Y/N:                  #
            #                                     #
            #######################################
                             ''')

        if lets_begin.lower() == 'y':

            device = str(determine_device())

            while True:
                what_protocol = str(input('''
            ##################################################
            #  WHAT KIND OF TEMPLATE DO YOU WANT TO CREATE?  #
            #                                                #
            #                 INTERFACE                      #
            #                                                #
            #                    or                          #
            #                                                #
            #                 PROTOCOLS:                     #
            #                   EIGRP                        #
            #                   OSPF                         #
            #                   RIP                          #
            #                   BGP                          #
            #                                                #
            #                   Exit                         #
            #                                                #
            #                                                #
            ############## ENTER YOUR CHOICE: ################
                                 '''))
                if what_protocol.lower() == 'eigrp':
                    eigrp_protocol()
                    break
                elif what_protocol.lower() == 'ospf':
                    ospf_protocol()
                    break
                elif what_protocol.lower() == 'rip':
                    rip_protocol()
                    break
                elif what_protocol.lower() == 'bgp':
                    bgp_protocol()
                    break
                elif what_protocol.lower() == 'interface':
                    interface_config()
                    break
                elif what_protocol.lower() == 'exit':
                    print('Arigatou!!!')
                    quit()
                else:
                    print('Wrong input! Try again!!!')

            username = user_input()
            password = pass_input()

            with open(f'/code-wev/configuration_push/network-infrastructure/netmiko/devices/{device}_address.cfg', 'r') as i:
                ip_address = i.read().splitlines()

            with open(f'/code-wev/configuration_push/network-infrastructure/netmiko/configuration_files/{what_protocol}_config.cfg', 'r') as fi:
                final_configs = fi.read().splitlines()


                for ip in ip_address:
                    cisco = {
                        'device_type': 'cisco_ios',
                        'ip': ip,
                        'username': username,
                        'password': password
                    }

                    divider(ip)

                    try:
                        config_deployment = ConnectHandler(**cisco)
                        final_deployment = config_deployment.send_config_set(final_configs)
                        pull_configs = config_deployment.send_command('show run | section route')
                        print('CONFIGURATION DEPLOYED!!!')
                        print(final_deployment + pull_configs)
                    except AuthenticationException:
                        print('Authentication failure: ' + ip)
                        continue
                    except NetMikoTimeoutException:
                        print('Timeout to device: ' + ip)
                        continue
                    except EOFError:
                        print('End of file while attempting device ' + ip)
                        continue
                    except SSHException:
                        print('SSH Issue. Are you sure SSH is enabled? ' + ip)
                        continue
                    except Exception as unknown_error:
                        print('Some other error: ' + str(unknown_error))
                        continue
                    else:
                        pass

                    time_now()

        elif lets_begin.lower() == 'n':
            print('Arigatou!!!')
            quit()
        else:
            print('Wrong input! Try again!!!')


if __name__ == '__main__':
    main()
