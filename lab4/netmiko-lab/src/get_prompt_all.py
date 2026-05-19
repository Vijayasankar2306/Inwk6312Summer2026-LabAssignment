from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",   # R01
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",   # R02
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",   # R03
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    }
]

for device in devices:
    print(f"\nConnecting to {device['ip']}...")

    net_connect = Netmiko(**device)

    # Default prompt
    print(f"Default prompt: {net_connect.find_prompt()}")

    # Disable mode
    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")

    # Enable mode
    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}")

    net_connect.disconnect()
