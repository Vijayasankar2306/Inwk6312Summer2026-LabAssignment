from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": 22
}

net_connect = ConnectHandler(**device)

# Enter enable mode
net_connect.enable()

# Configuration commands
config_commands = [
    "interface loopback0",
    "ip address 10.10.10.1 255.255.255.255",
    "description LOOPBACK_INTERFACE"
]

output = net_connect.send_config_set(config_commands)

print(output)

# Verify
verify = net_connect.send_command("show ip interface brief")
print("\nUpdated Interfaces:\n")
print(verify)

net_connect.disconnect()
