from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",   # R01
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",   # R02
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",   # R03
        "username": "student",
        "password": "Meilab123",
        "port": 22
    }
]

for device in devices:

    net_connect = ConnectHandler(**device)

    output = net_connect.send_command(
        "show ip route",
        use_textfsm=True
    )

    print("\n" + "=" * 60)
    print(f"Router: {device['ip']}")
    print("=" * 60)

    print(type(output))

    for route in output:
        protocol = route.get("protocol", "")
        network = route.get("network", "")
        distance = route.get("distance", "")
        metric = route.get("metric", "")

        print(f"{protocol} {network} {distance} {metric}")

    net_connect.disconnect()
