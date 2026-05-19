from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",   # R01
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",   # R02
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",   # R03
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    }
]

for device in devices:

    net_connect = Netmiko(**device)

    output = net_connect.send_command("show version")

    net_connect.disconnect()

    # Find "Configuration register"
    result = output.find("Configuration register")

    begin = int(result)

    # Extract the full line
    end = output.find("\n", begin)

    print(device['ip'] + " => " + output[begin:end])
