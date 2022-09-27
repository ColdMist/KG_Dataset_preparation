import numpy as np
import pandas as pd
import os

def compare(dataset_A, dataset_B):
    '''
    @param dataset_A: First dataset to compare
    @param dataset_B: Second dataset to compare
    @return: an intersection between the two datasets
    '''
    dataset_difference = pd.concat([dataset_A, dataset_B]).drop_duplicates(keep=False)
    return dataset_difference

if __name__ == "__main__":
    data_A_directory = 'datasets/WN18RR_old/mapped'
    data_B_directory = 'datasets/WN18RR_new'
    dataset_A = pd.read_table(os.path.join(data_A_directory, 'train.txt'), header=None, dtype=str)
    dataset_B = pd.read_table(os.path.join(data_B_directory, 'train.txt'), header=None, dtype=str)
    dataset_difference = compare(dataset_A, dataset_B)
    dataset_difference.to_csv(f'{data_A_directory}train_diff.csv', sep='\t', header=None, index=False)
