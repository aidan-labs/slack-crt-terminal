# netmiko_utils.py

# Standard imports
import os
# Third-Party imports
from dotenv import load_dotenv
from netmiko import ConnectHandler

# Load environment variables from a .env file
load_dotenv()
# Retrieve switch credentials from environment variables
name = os.getenv("NAME")
password = os.getenv("PASSWORD")

# Dictionary to define all the switches and their connection details
# Ensure the key matches the value in "get_updated_options" function in "views.py" to add a switch
all_switch_configs = {
    # Location 1
    "test_closet": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    "closet_01": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    "closet_02": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    # Location 2
    "closet_11": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    "closet_12": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    # Location 3
    "closet_13": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    "closet_14": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    # Location 4
    "closet_17": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
    "closet_18": {"device_type": "cisco_ios", "host": "1.1.1.1", "username": "admin", "password": "password",},
}

# Function to send any command to a switch and retrieve the output
def send_command(device_config, command):
    try:
        with ConnectHandler(**device_config) as net_connect:
            net_connect.enable()
            output = net_connect.send_command(command)
            return output
    except Exception as e:
        return str(e)

# Function to show the interface status for a specific interface
def show_int(device_config, command_input):
    try:
        with ConnectHandler(**device_config) as net_connect:
            net_connect.enable()
            command = f"sh int {command_input}"
            output = net_connect.send_command(command)
            return output
    except Exception as e:
        return str(e)

# Function to show the running configuration of a specific interface
def show_run_int(device_config, command_input):
    try:
        with ConnectHandler(**device_config) as net_connect:
            net_connect.enable()
            command = f"sh run int {command_input}"
            output = net_connect.send_command(command)
            return output
    except Exception as e:
        return str(e)

# Function to send a set of configuration commands to the device
def send_set_config(device_config, config_commands):
    try:
        with ConnectHandler(**device_config) as net_connect:
            net_connect.enable()
            output = net_connect.send_config_set(config_commands)
            return output
    except Exception as e:
        return str(e)
