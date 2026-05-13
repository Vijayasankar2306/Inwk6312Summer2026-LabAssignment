from jinja2 import Environment, FileSystemLoader
import yaml

# Create Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load Jinja template
template = ENV.get_template("router_template.j2")

# Open YAML file
with open("routers.yml") as f:

    # Load YAML data
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Render configuration
output = template.render(routers=data["routers"])

# Print output
print(output)
