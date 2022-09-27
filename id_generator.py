import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import os

def write_dic(path,d):
    """
    :param

    path: path where to be saved
    d: dictionary to be written in txt

    """
    f=open (path,"w")
    keys=d.keys()
    for k in keys:
        print(str(k)+'\t'+str(d[k]))
        f.write(str(k)+'\t'+str(d[k]))
        f.write("\n")
    f.close()

def write_to_txt_file(path, data):
    """
    :param

    path: path where to be saved
    data: triples to be written in txt


    """
    f = open(path, "w")
    for i in range(data.shape[0]):
        line = ''
        for j in range(data.shape[1]):
            if(j==0):
                line = str(data[i][j])
            else:
                line = line + '\t' + str(data[i][j])
        f.write(line)
        f.write("\n")
        print(line)
    f.close()

if __name__ == "__main__":
    data_dir = 'datasets/WN18RR_old/mapped/updated'

    train_data_dir = os.path.join(data_dir, 'train.txt')
    test_data_dir = os.path.join(data_dir, 'test.txt')
    valid_data_dir = os.path.join(data_dir, 'valid.txt')

    train_triples = pd.read_table(train_data_dir, header=None, sep='\t', dtype=str)
    test_triples = pd.read_table(test_data_dir, header=None, sep='\t', dtype=str)
    validation_triples = pd.read_table(valid_data_dir, header=None, sep= '\t', dtype=str)

    frames = [train_triples, test_triples, validation_triples]
    result = pd.concat(frames)
    result_in_array = np.array(result)

    result_in_array = pd.DataFrame(result_in_array)
    all_entities = list(result_in_array[0].unique()) + list(result_in_array[2].unique())
    all_entities = np.unique(all_entities)

    all_relations =list(result_in_array[1].unique())

    pd.DataFrame(all_entities).to_csv(os.path.join(data_dir,'entities.dict'), header=None, index=True, sep='\t')
    pd.DataFrame(all_relations).to_csv(os.path.join(data_dir, 'relations.dict'), header=None, index=True, sep='\t')


