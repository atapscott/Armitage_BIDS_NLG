import os
from constants import constants

def get_path_supported_data_files(path: str) -> list:
    supported_data_files: list = []
    file_names = os.listdir(path)  # get all files' and folders' names in the current directory

    for file_name in file_names:  # loop through all the files and folders
        new_file_path = os.path.join(os.path.abspath(path), file_name)
        if os.path.isdir(new_file_path):  # check whether the current object is a folder or not
            supported_data_files += get_path_supported_data_files(new_file_path)
        else:
            is_supported, rendering_type = is_supported_bids_data(file_name)
            if is_supported:
                supported_data_files.append((new_file_path, rendering_type))

    return supported_data_files


def is_supported_bids_data(file_name: str) -> (bool, str):
    supported_formats: set = (
        ('_meg.json', constants.MEG_TECHNIQUE),
        ('dataset_description.json', constants.DATASET_DESCRIPTION),
    )

    for supported_format in supported_formats:
        if supported_format[0] in file_name:
            return True, supported_format[1]

    return False, ''
