from jinja2 import Environment, PackageLoader, select_autoescape
from constants import constants


class TemplateManager:
    # Environment from which all templates will be loaded. Required for Jinja imports
    env: Environment = None

    @classmethod
    def initialize_environment(cls, render_type: str):
        """ Initialize class variables.

        :return: None
        """

        # Set the class environment so that it relies on the right folder and also auto-escapes our custom tmp files
        cls.env = Environment(
            loader=PackageLoader('template_manager', 'templates/{}'.format(render_type)),
            autoescape=select_autoescape(['html', 'xml', 'tmp'])
        )

    @classmethod
    def render_template(cls, **kwargs) -> str:
        """ Render the template after the provided name.

        :param kwargs: Data used for the template rendering.
        :return: Rendered text for the requested template. Includes any subtemplates in the hierarchy.
        """

        input_data: dict = kwargs['input_data']

        for k, v in kwargs['input_args'].items():
            input_data['input_args_{}'.format(k)] = v

        render_type: str = kwargs['input_data']['render_type']
        # Set the environment to load from specific render type template
        cls.initialize_environment(render_type)

        template_filename: str = "base.tmp"
        template = cls.env.get_template(template_filename)
        return template.render(input_data)
