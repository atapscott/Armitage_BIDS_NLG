from jinja2 import Environment, PackageLoader, select_autoescape


class TemplateManager:

    env: Environment = None

    @classmethod
    def initialize(cls):
        cls.env = Environment(
            loader=PackageLoader('template_manager', 'templates'),
            autoescape=select_autoescape(['html', 'xml', 'tmp'])
        )

    @classmethod
    def render_template(cls, template_name: str, **kwargs) -> str:
        template_filename: str = "{}.tmp".format(template_name)
        template = cls.env.get_template(template_filename)
        return template.render(kwargs['input_data'])
