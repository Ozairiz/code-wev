#!/bin/bash

echo 'python virtual environment initialized...'
 apt install python3-pip -y
 apt install python3-virtualenv -y

echo 'creating virtual environment directory...'
 mkdir ~/python_venv

echo 'python3.10 installation...'
 apt update
 apt install software-properties-common -y
 add-apt-repository ppa:deadsnakes/ppa -y
 apt update
 apt install python3.10 python3.10-venv python3.10-distutils -y

echo 'creating virtual environment...'
 read -p 'Enter the folder name: ' folder_name
 python3.10 -m venv ~/python_venv/$folder_name
 source ~/python_venv/$folder_name/bin/activate
 sudo apt  install ansible