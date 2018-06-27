import json
import csv
import argparse
import loader.file_probe
from constants import constants
from pprint import pprint
import processor.render_specific_metrics

from template_manager import *


def parse_arguments():
    """Main method to parse the input arguments.

    :return: The object with all the parsed arguments or their default value.
    """

    # Add the parsing of arguments
    parser = argparse.ArgumentParser(
        description='Template-based BIDS report natural language generation')

    # Add the debug parameter
    parser.add_argument('-d', action='store_true')

    args = parser.parse_args()

    return args


def select_file_path_render_type() -> (str, str):
    # Get the input BIDS data
    supported_data_files: list = loader.file_probe.get_path_supported_data_files('data')

    print()
    print('Select render_type and data input:')
    print()
    for i, supported_data_file in enumerate(supported_data_files):
        print("{}:{}".format(i, supported_data_file[1]))
        print(supported_data_file[0])

    print()
    selected_data_index: int = int(input("Choose input data: "))

    return supported_data_files[selected_data_index]


def load_file(file_path: str):
    file_data = None
    if '.json' in file_path:
        file_data = json.load(open(file_path))
    elif '.tsv' in file_path:
        with open(file_path, 'r') as infile:
            json_data_rows: list = [d for d in csv.DictReader(infile, delimiter='\t')]
            file_data: dict = {'rows': json_data_rows}
    return file_data


def add_render_specific_metrics(render_type: str, input_data: dict):
    if hasattr(processor.render_specific_metrics, '{}_metrics'.format(render_type)):
        metric_function = getattr(processor.render_specific_metrics, '{}_metrics'.format(render_type))
        input_data = metric_function(input_data)

    return input_data


if __name__ == '__main__':

    print('Running _Armitage_  - BIDS Report NLG')

    # Fetch the input arguments
    input_args = parse_arguments()

    file_path, render_type = select_file_path_render_type()

    input_data = load_file(file_path)

    input_data = add_render_specific_metrics(render_type, input_data)

    input_data['render_type'] = render_type

    # Render the root patter, hierarchically rendering all the sub-patterns
    rendered_template: str = TemplateManager.render_template(input_args=vars(input_args), input_data=input_data)

    # Print data for debug mode
    if input_args.d:
        # Print the raw data
        pprint(input_data)
        print()
        # Print the result in stdout
        print(rendered_template)

    # Output the same result in a text file in the OUTFILE path
    with open(constants.OUTFILE, 'w') as out:
        out.write("{} ".format(rendered_template))
