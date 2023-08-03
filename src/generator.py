import sys
import logging
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
cloud_infra_values= {"env_name": "Infoblox HackFest 2023",
              "aws_acc_name": "cyberintel infoblox"}

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("base-vpc.j2")
content = template.render(cloud_infra_values)
filename = "base-vpc.py"
with open("artifact/{}".format(filename), mode="w", encoding="utf-8") as message:
    message.write(content)
    logging.info(f"info: {filename}")

artifact_file = Path("artifact/{}".format(filename))
if artifact_file.is_file():
    logging.info("artifact file created successfully")
    exec(open(artifact_file).read())
