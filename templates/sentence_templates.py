import string
import json

from templates.key_word_templates import KeyWordTemplateManager

class CF(string.Formatter):
    def __init__(self):
        super(CF, self).__init__()

    def vformat(self, format_string, args, kwargs):
        format_labels: list = [fname for _, fname, _, _ in string.Formatter().parse(format_string) if fname]
        for format_label in format_labels:
            kwargs[format_label.split('_')[-1]] = SentenceTemplateManager.render_key_words(format_label, kwargs)
            format_string = format_string.replace(format_label, format_label.split('_')[-1])
        return super(CF, self).vformat(format_string, args, kwargs)


class SentenceTemplateManager:

    sentence_templates: dict = json.load(open('templates/sentence_templates.json', 'r'))

    @classmethod
    def render_key_words(cls, input_data_label: str, input_data: dict) -> str:
        if isinstance(input_data_label, str) and '_' not in input_data_label:
            return input_data[input_data_label]
        else:
            field_name: str = input_data_label.split('_')[-1]
            sub_filter_name: str = input_data_label.split('_')[-2]
            input_data_value: str = cls.render_key_words(field_name, input_data)
            key_word_filter = KeyWordTemplateManager.get_key_word_filter(sub_filter_name)
            return key_word_filter(field_name=field_name, data_value=input_data_value, input_data=input_data)

    # TODO just iterating the sentence documente. Should include proper report templates to manage the macro structure.
    @classmethod
    def get_rendered_templates(cls, input_data: dict) -> (str, str):
        for template_name, template_text in cls.sentence_templates.items():
            rendered_template = CF().format(template_text, **input_data)
            yield (template_name, rendered_template)
