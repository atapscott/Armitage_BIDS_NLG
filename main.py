import json
import argparse

from template_manager import *


def parse_arguments():

    parser = argparse.ArgumentParser(
        description='Template-based BIDS report language generation')

    parser.add_argument('-t', action="store", dest='parent_template_name', default='base_report')

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    input_args = parse_arguments()

    parent_template_name: str = input_args.parent_template_name

    input_data = json.load(open('data/sample_meg.json'))

    TemplateManager.initialize()

    rendered_template: str = TemplateManager.render_template(parent_template_name, input_data=input_data)

    print(rendered_template)

    with open('renderedReportResult.txt', 'w') as out:
        out.write("{} ".format(rendered_template))


