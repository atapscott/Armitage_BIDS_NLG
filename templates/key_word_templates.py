import sys

class KeyWordTemplateManager:

    keyword_rendering_filters: dict = {
        'PLAIN': 'plain_filtering',
        'dc': 'filter_channel_name',
        'dw': 'filter_dewar_positioning'
    }

    @classmethod
    def get_key_word_filter(cls, filter_name: str):
        function_name: str = cls.keyword_rendering_filters[filter_name]
        return getattr(KeyWordTemplateManager, function_name)

    @staticmethod
    def parse_args(kwargs: dict):
        return kwargs['field_name'], kwargs['data_value'], kwargs['input_data']

    @staticmethod
    def plain_filtering(**kwargs) -> str:
        field_name, data_value, input_data = KeyWordTemplateManager.parse_args(kwargs)
        return data_value

    @staticmethod
    def filter_channel_name(**kwargs) -> str:
        field_name, data_value, input_data = KeyWordTemplateManager.parse_args(kwargs)
        return "{} {}{}".format(str(data_value), field_name.replace('ChannelCount', ' channel'),
                                's' if int(data_value) != 1 else '')

    @staticmethod
    def filter_dewar_positioning(**kwargs) -> str:
        field_name, data_value, input_data = KeyWordTemplateManager.parse_args(kwargs)
        return "positioned {}".format(data_value)