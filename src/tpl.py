from jinja2 import Environment, FileSystemLoader, Template

env = Environment(
    loader=FileSystemLoader('./templates'),
)


def get_template(template_name: str) -> Template:
    return env.get_template(template_name)


__all__ = [
    get_template,
]