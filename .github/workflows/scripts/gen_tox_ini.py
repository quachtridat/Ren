#!/usr/bin/env python3
import pathlib
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":
    current_path = pathlib.Path(".")

    cogs = [
        d.name for d in current_path.iterdir()
        if d.is_dir() and (d / "info.json").exists()
    ]

    templates_path = current_path / ".github" / "workflows" / "scripts" / "templates"
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template("tox.ini.j2")

    tox_ini = template.render(cogs=cogs)
    tox_ini_path = pathlib.Path("/") / "tmp" / "tox.cog_unit_test.ini"
    tox_ini_path.write_text(tox_ini)
