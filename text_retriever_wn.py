from nltk.corpus import wordnet as wn
import pandas as pd
import numpy as np
import nltk
import os
#nltk.download('wordnet')

def obtain_text_WN(ids):
    '''
    @param ids: the sysnet text which needs to find the defination
    @return: the converted texts alone, converted texts alongside with previous_values
    '''
    converted_texts_for_ids = [wn.synset(i).definition() for i in ids]
    print(converted_texts_for_ids)
    converted_texts_with_ids = [ids[i]+ ' : ' + converted_texts_for_ids[i] for i in range(len(ids))]
    return converted_texts_for_ids, converted_texts_with_ids

if __name__ == "__main__":
    data_dir = 'WN18_old/mapped'
    entity_file_name = 'entities.dict'
    data = pd.read_table(os.path.join(f"datasets/{data_dir}", entity_file_name), header=None, dtype=str)
    converted_ids, converted_ids_with_orig = obtain_text_WN(data[1].values)
    converted_table_entities = np.c_[data[1].values , converted_ids_with_orig]
    entities_df_with_previous_values = pd.DataFrame(converted_table_entities, columns=['original_text', 'retrieved_text_with_previous_values'])
    entities_df_with_previous_values.to_csv(os.path.join(f"datasets/{data_dir}", 'entities_with_previous_values.csv'), header=None, index=False, sep = '\t')
    entities_df_with_previous_values.to_excel(os.path.join(f"datasets/{data_dir}", 'entities_with_previous_values.xlsx'),  index=False)