import itertools
from os import listdir, path

'''
takes a dictionary of
 {
   "paramName1": [paramValue11, paramValue12, paramVa13],
   "paramName2": [paramValue21, paramValue22, paramVa23]
   ...
 }

 generates a list of combinations among values and params 
 [
    {"paramName1": "paramValue11", "paramName2": "paramValue21"},
    {"paramName1": "paramValue12", "paramName2": "paramValue21"},
    ...
    ..
 ]
'''


def combine_parameters(list_of_parameters):
    keys = list()
    values = list()
    for key, value in list_of_parameters.items():
        keys.append(key)
        values.append(value)
    return [dict(zip(keys, result)) for result in list(itertools.product(*values))]


def get_files_in_folder(path_to_folder):
    filtered_files_in_folder = list(filter(lambda x: not x.startswith("."),listdir(path_to_folder)))
    return filtered_files_in_folder


def get_input_output_pairs(path_to_folder, output_folder):
    filtered_files_in_folder = get_files_in_folder(path_to_folder)
    input_output_pairs = [(path.join(path_to_folder, f), path.join(output_folder, f)) for f in filtered_files_in_folder]
    return input_output_pairs
