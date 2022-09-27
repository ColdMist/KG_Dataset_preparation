from nltk.corpus import wordnet as wn
import pandas as pd
import numpy as np
import nltk
nltk.download('wordnet')

def obtain_text_WN(ids):
    '''
    @param ids: the sysnet text which needs to find the defination
    @return:
    '''
    converted_texts_for_ids = [wn.synset(i).definition() for i in ids]
    print(converted_texts_for_ids)
    converted_texts_with_ids = [ids[i]+ ' : ' + converted_texts_for_ids[i] for i in range(len(ids))]
    return converted_texts_for_ids, converted_texts_with_ids

if __name__ == "__main__":
    data_dir = ''
    data = pd.read_table('/home/mirza/PycharmProjects/RotatE_FrameWork-_Lanaguage_model/data/wn9/entity2id.txt', header=None)
    converted_ids, converted_ids_with_orig = obtain_text_WN(data[0].values)
    converted_table_entities = np.c_[data[1].values , converted_ids_with_orig]
    entities_df_with_previous_values = pd.DataFrame(converted_table_entities, columns=['original_text', 'retrieved_text'])
    entities_df_with_previous_values.to_csv('/home/mirza/PycharmProjects/RotatE_FrameWork-_Lanaguage_model/data/wn9/entities_.dict', header=None, index=False, sep = '\t')
    entities_df_with_previous_values.to_excel('/home/mirza/PycharmProjects/RotatE_FrameWork-_Lanaguage_model/data/wn9/entities_with_previous_values.xlsx',  index=False)