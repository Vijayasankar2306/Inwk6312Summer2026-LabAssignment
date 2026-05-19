import yaml
from jinja2 import Template
from netmiko import ConnectHandler

# Load YAML
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

# Device-specific data
device_data = {
    "R1": {
        "loopback_ip": "150.1.1.1",
        "subinterfaces": [
            {"vlan": 14, "ip": "155.1.14.1"},
            {"vlan": 13, "ip": "155.1.13.1"},
            {"vlan": 12, "ip": "155.1.12.1"},
        ],
        "rip_networks": ["155.1.12.0", "155.1.13.0", "155.1.14.0", "150.1.0.0"]
    },
    "R2": {
        "loopback_ip": "150.1.2.2",
        "subinterfaces": [
            {"vlan": 12, "ip": "155.1.12.2"}
        ],
        "rip_networks": ["155.1.12.0", "150.1.2.0"]
    },
    "R3": {
        "loopback_ip": "150.1.3.3",
        "subinterfaces": [
            {"vlan": 13, "ip": "155.1.13.3"}
        ],
        "rip_networks": ["155.1.13.0", "150.1.3.0"]
    },
    "R4": {
        "loopback_ip": "150.1.4.4",
        "subinterfaces": [
            {"vlan": 14, "ip": "155.1.14.4"}
        ],
        "rip_networks": ["155.1.14.0", "150.1.4.0"]
    }
}

# Load Jinja template
with open("config_template.j2") as f:
    template = Template(f.read())

# Deploy config
for hostname, device in devices.items():

    print(f"\nConnecting to {hostname}...")

    config = template.render(**device_data[hostname])

    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_config_set(config.split("\n"))

    print(output)

    connection.disconnect()

    print(f"{hostname} configuration complete.")
