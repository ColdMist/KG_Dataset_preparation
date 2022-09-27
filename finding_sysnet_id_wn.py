import pandas as pd
from nltk.corpus import wordnet as wn
import os


def find_wn_ids(entities_list):
    '''
    @param entities_list: List of entities integer like needs to be converted
    @return: entities_str: converted entities, count: the count of entities converted
    '''
    entities_str = []
    count = 0
    for entity in entities_list:
        for i in ['a', 's', 'r', 'n', 'v']:
            try:
                converted_value = wn.synset_from_pos_and_offset(i, int(entity)).name()
                entities_str.append([entity, converted_value])
                count+=1
                break
            except:
                continue
    return entities_str, count

if __name__ == "__main__":
    data = 'datasets/WN18_old'
    entities_dir = os.path.join(data, 'entities.dict')
    entities = pd.read_table(entities_dir, header=None, dtype=str)
    entities_list = entities[1].values
    entities_str, count = find_wn_ids(entities_list)
    pd.DataFrame(entities_str).to_csv(os.path.join(data,'entities_mapped.csv'), sep='\t', header=None, index=False)
