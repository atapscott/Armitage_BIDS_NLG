import json
from templates.sentence_templates import SentenceTemplateManager

if __name__ == '__main__':
    input_data = json.load(open('data/sample_meg.json'))

    rendered_templates = list(SentenceTemplateManager.get_rendered_templates(input_data))
    with open('renderedReportResult.txt', 'w') as out:
        for tn, tt in rendered_templates:
            out.write("{} ".format(tt))
