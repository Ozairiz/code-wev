#!/bin/bash

read -p "setup DNS: Y/N: " user_input

# Using a while loop to repeat the prompt if the input is not valid
while true; do
  if [[ "$user_input" == "y" || "$user_input" == "Y" ]]; then
    python3 /code-wev/configuration_push/network-infrastructure/dns_script/hostname_ip.py
    break
  elif [[ "$user_input" == "n" || "$user_input" == "N" ]]; then
    echo 'quit'
    break
  else
    echo 'Please try again!'
    read -p "setup DNS: Y/N: " user_input  # Prompt again for valid input
  fi
done

read -p "a. Deploy | b. Backup: " user_config

while true; do
    if [[ "$user_config" == "a" || "$user_config" == "A" ]]; then
        python3 /code-wev/configuration_push/network-infrastructure/netmiko/netmiko-automation.py
        exit 0
    elif [[ "$user_config" == "b" || "$user_config" == "B" ]]; then
        python3 /code-wev/configuration_push/network-infrastructure/paramiko/paramiko_automation_backup.py
        exit 0
    else
        echo 'Please try again!'
        read -p "a. Deploy | b. Backup: " user_config
    fi
done
