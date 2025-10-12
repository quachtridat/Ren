#!/usr/bin/env python3
import argparse
import pathlib
from jinja2 import Template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a cogs-dependent config INI from template")
    parser.add_argument("--cogs-dir", type=str, default="cogs", help="Directory containing cogs")
    parser.add_argument("--template-file", type=str, default="config.ini.j2", help="Template file name")
    args = parser.parse_args()

    cogs_path = pathlib.Path(args.cogs_dir)
    cogs = [d.name for d in cogs_path.iterdir() if d.is_dir() and (d / "info.json").exists()]

    with open(args.template_file, "r") as f:
        template: Template = Template(f.read())

    print(template.render(cogs=cogs, cogs_dir=args.cogs_dir))
