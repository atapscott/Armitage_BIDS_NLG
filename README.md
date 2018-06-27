# _Armitage_  - BIDS Report NLG

Simple program for template-based natural language rendering of reports based on [BIDS](http://bids.neuroimaging.io/) neuroimaging data. 

## Getting Started

* Use a Python 3.6 distribution
* Install requirements (mainly Jinja2 and numpy)
```
pip install requirements
```

## Running

Just run the _main.py_ file:
```
python main.py
```
The main file uses default values to auto-generate a report:

* _data/_ - BIDS files should be placed under this directory to allow Armitage probe to find them.
* _renderedReportResults.txt_ - Default output file

Running with a -d argument outputs the raw data and the pre-processed input data
```
python main.py -d
```

Then we use the interactive prompt to select some supported BIDS data file
```
1:participant_data
C:\Users\alant\PycharmProjects\NeuroReportNLG\data\OMEGA_RestingState_sample_20180626_150722\participants.tsv
```

Automatically fetches the _base.tmp_ template from the participant_data folder and renders it hierarchically if necessary.
Debug mode would allow us to see the input pre-processed data
```
{'AverageAge': 27.4,
 'FemaleAmount': 2,
 'RightHandedRatio': 'all',
 'StdDevAge': 5.0,
 'SubjectAmount': 5,
 'input_args_d': True,
 'render_type': 'participant_data',
 'rows': [OrderedDict([('participant_id', 'sub-0007'),
                       ('age', '21'),
                       ('sex', 'Male'),
                       ('dominant_hand', 'Right')]),
          OrderedDict([('participant_id', 'sub-0006'),
                       ('age', '30'),
                       ('sex', 'Male'),
                       ('dominant_hand', 'Right')]),
          OrderedDict([('participant_id', 'sub-0004'),
                       ('age', '28'),
                       ('sex', 'Female'),
                       ('dominant_hand', 'Right')]),
          OrderedDict([('participant_id', 'sub-0003'),
                       ('age', '35'),
                       ('sex', 'Female'),
                       ('dominant_hand', 'Right')]),
          OrderedDict([('participant_id', 'sub-0002'),
                       ('age', '23'),
                       ('sex', 'Male'),
                       ('dominant_hand', 'Right')]),
          OrderedDict([('participant_id', 'sub-emptyroom'),
                       ('age', 'n/a'),
                       ('sex', 'n/a'),
                       ('dominant_hand', 'n/a')])]}
```

And then the resulting rendered template

```
5 subjects (2 females), 27.4+-5.0 years old, all of them right handed, participated in the study.

```