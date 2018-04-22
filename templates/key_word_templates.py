import sys

class KeyWordTemplateManager:

    keyword_rendering_filters: dict = {
        'PLAIN': 'plain_filtering',
        'dc': 'filter_channel_name',
        'dw': 'filter_dewar_positioning',
        'not-if-true': 'not_if_true',
        'enumerate-list': 'enumerate_list',
        'enumerate-list-hz': 'enumerate_list_hz'
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

    @staticmethod
    def not_if_true(**kwargs) -> str:
        field_name, data_value, input_data = KeyWordTemplateManager.parse_args(kwargs)
        return "" if data_value == 'true' else " not"

    @staticmethod
    def enumerate_list(**kwargs) -> str:
        field_name, data_value, input_data = KeyWordTemplateManager.parse_args(kwargs)
        unit = kwargs['unit']
        result_str = ""
        for index, value in enumerate(data_value):
            if index < len(data_value) - 1:
                result_str = result_str + "{}{}, ".format(value, unit if unit else '')
            else:
                result_str = result_str[:-2]
                result_str = result_str + " and {}{}".format(value, unit if unit else '')
        return result_str

    @staticmethod
    def enumerate_list_hz(**kwargs) -> str:
        kwargs['unit'] = 'Hz'
        return KeyWordTemplateManager.enumerate_list(**kwargs)
