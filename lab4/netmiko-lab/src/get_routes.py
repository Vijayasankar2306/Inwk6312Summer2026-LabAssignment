from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
    }
]

for device in devices:

    net_connect = ConnectHandler(**device)

    output = net_connect.send_command("show ip route", use_textfsm=True)

    print("\n" + "=" * 60)
    print(f"Router: {device['ip']}")
    print("=" * 60)

    for route in output:
        protocol = route.get("protocol")
        network = route.get("network")
        distance = route.get("distance")
        metric = route.get("metric")

        print(f"{protocol} {network} {distance} {metric}")

    net_connect.disconnect()
