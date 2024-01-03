from jinja2 import Environment, FileSystemLoader

import os
import subprocess
import sys

TEMPLATES_DIR = "/templates"
PRETTIER_PARSER_CHOICES = ("yaml",)


if __name__ == "__main__":
    template = os.environ.get("TEMPLATE")
    debug = os.environ.get("DEBUG", "0").lower() in ("1", "true")
    pretty = os.environ.get("PRETTY", "0").lower() in ("1", "true")
    prettier_parser = os.environ.get("PRETTIER_PARSER")

    if not template:
        raise Exception("TEMPLATE is required")

    if pretty:
        if not prettier_parser:
            raise Exception("PRETTIER_PARSER is required if PRETTY is turned on")

        if prettier_parser not in PRETTIER_PARSER_CHOICES:
            string = ", ".join(PRETTIER_PARSER_CHOICES)
            raise Exception(f"PRETTIER_PARSER must be one of: {string}")

    context = {}

    for arg in sys.argv[1:]:
        key, value = arg.split("=", 1)
        context[key] = value

    if debug:
        sys.stdout.write("Configuration\n")
        sys.stdout.write("-------------\n")
        sys.stdout.write(f"template: {template}\n")
        sys.stdout.write(f"debug: {debug}\n")
        sys.stdout.write(f"pretty: {pretty}\n")
        sys.stdout.write(f"prettier_parser: {prettier_parser}\n")
        sys.stdout.write(f"context: {context}\n\n")

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template(template)
    rendered = template.render(context)

    if pretty:
        cmd = f"prettier --parser {prettier_parser}"
        rendered = subprocess.check_output(cmd, input=rendered, shell=True, text=True)

    sys.stdout.write(rendered)
