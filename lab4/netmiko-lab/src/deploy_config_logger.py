import yaml
import logging
from jinja2 import Template
from netmiko import ConnectHandler

# Logging setup
logging.basicConfig(
    filename="netmiko_lab.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

with open("config_template.j2") as f:
    template = Template(f.read())

for hostname, device in devices.items():

    try:
        logging.info(f"Connecting to {hostname}")

        config = template.render(hostname=hostname)

        connection = ConnectHandler(**device)
        connection.enable()

        output = connection.send_config_set(config.split("\n"))

        logging.info(f"Config pushed to {hostname}")
        print(output)

        connection.disconnect()

    except Exception as e:
        logging.error(f"Error on {hostname}: {str(e)}")
        print(f"Failed on {hostname}")
