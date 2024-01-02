from jinja2 import Environment, FileSystemLoader

import os
import sys

TEMPLATES_DIR = "/templates"


if __name__ == "__main__":
    template_file = os.environ["TEMPLATE"]

    context = {}

    for arg in sys.argv[1:]:
        key, value = arg.split("=", 1)
        context[key] = value

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template(template_file)
    result = template.render(context)

    print(result)
