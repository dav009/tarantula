import codecs
import json
import itertools
from os import listdir, path, makedirs

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

def assure_folder_exists(filepath):
    if not path.exists(filepath):
        makedirs(filepath)

def remove_file(filepath):
    try:
        os.remove(filepath)
    except Exception:
        pass

def join_files_in_folder(path_to_folder, f):
    result = list()
    for filename in get_files_in_folder(path_to_folder):
        complete_file_path = path.join(path_to_folder, filename)
        result.append(f(complete_file_path))
    return result

def join_json(path_to_folder):

    def load_json(path_to_file):
        f = codecs.open(path_to_file, 'r', 'utf-8')
        json_object = json.loads("\n".join([line for line in f]))
        f.close()
        return json_object

    return join_files_in_folder(path_to_folder, load_json)


