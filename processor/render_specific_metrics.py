from processor import metrics


def participant_data_metrics(input_data):
    data_rows: list = [r for r in input_data['rows'] if r['participant_id'] != 'sub-emptyroom']
    input_data['SubjectAmount'] = len(data_rows)
    female_data_rows = [r for r in data_rows if r['sex'] == 'Female']
    age_magnitude = [float(r['age']) for r in data_rows]
    right_handed_data_rows = [r for r in data_rows if r['dominant_hand'] == 'Right']

    input_data['SubjectAmount'] = len(data_rows)
    input_data['FemaleAmount'] = len(female_data_rows)
    input_data['AverageAge'] = metrics.mean(age_magnitude)
    input_data['StdDevAge'] = round(metrics.standard_deviation(age_magnitude), 2)
    input_data['RightHandedRatio'] = 'all' if len(data_rows) == len(right_handed_data_rows) else '{}/{}'.format(
        len(right_handed_data_rows), len(data_rows))

    return input_data
