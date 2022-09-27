import pandas as pd
import numpy as np
import os

def create_dict(data, key, value):
    '''
    @param data: the original data in dataframe where the key values need to be generated
    @param key: the key of the dictionary
    @param value: the value of the dictionary
    @return: the created dictionray with key value pairs
    '''
    dictionary = dict(zip(data[key], data[value]))
    return dictionary

def mapper(data, map_dict, cols = None):
    '''
    @param data: the dataframe where the values need to be mapped
    @param map_dict: the mapping dictionaries as key value pairs
    @param cols: the columns to be affected by the change
    @return: data: updated dataframe where the values are changed
    '''
    for col in cols:
        data[col] = data[col].map(map_dict)
    return data

if __name__ == "__main__":
    data_dir = 'datasets'
    data_set = 'WN18RR_old/mapped'
    exchange_data = 'entities_with_previous_values.csv'
    save_location = 'updated'

    train_data = pd.read_table(os.path.join(f'{data_dir}/{data_set}', 'train.txt'), header = None, dtype=str)
    test_data = pd.read_table(os.path.join(f'{data_dir}/{data_set}', 'test.txt'), header = None, dtype=str)
    valid_data = pd.read_table(os.path.join(f'{data_dir}/{data_set}', 'valid.txt'), header=None, dtype=str)

    train_data = train_data[[0,1,2]]
    test_data = test_data[[0,1,2]]
    valid_data = valid_data[[0,1,2]]

    entity_dictionary = pd.read_table(os.path.join(f'{data_dir}/{data_set}', exchange_data), header = None, sep='\t', dtype=str)
    entity_dictionary_dictionary_map = create_dict(entity_dictionary, 0, 1)

    train_data_mapped = mapper(train_data, entity_dictionary_dictionary_map, [0,2])
    test_data_mapped = mapper(test_data, entity_dictionary_dictionary_map, [0,2])
    valid_data_mapped = mapper(valid_data, entity_dictionary_dictionary_map, [0,2])

    train_data_mapped.to_csv(os.path.join(f'{data_dir}/{data_set}', f'{save_location}/train.txt'), header=None, index = False, sep='\t')
    test_data_mapped.to_csv(os.path.join(f'{data_dir}/{data_set}', f'{save_location}/test.txt'), header=None, index = False, sep='\t')
    valid_data_mapped.to_csv(os.path.join(f'{data_dir}/{data_set}', f'{save_location}/valid.txt'), header=None, index = False, sep='\t')

