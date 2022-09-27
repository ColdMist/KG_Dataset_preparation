import os
from argparse import ArgumentParser
#from utils.indexer import Indexer
import pandas as pd
from sentence_transformers import SentenceTransformer
from torch.nn import functional as F
import numpy as np
import torch
from gensim.models import fasttext
from os.path import join
import pickle

encoder = SentenceTransformer('distilbert-base-nli-mean-tokens')
vec = fasttext.load_facebook_vectors("wiki_corpus/wiki.simple.bin")
print("Loaded vector")

def get_args():
    parser = ArgumentParser(description="embKBQA")
    #parser.add_argument("--output_path", required=True, type=str, help="output path")
    #parser.add_argument("--faiss_index", type=str, default="hnsw", help='hnsw index')
    #parser.add_argument('--index_buffer', type=int, default=50000)
    parser.add_argument("--save_index", action='store_true', help='save indexed file')
    parser.add_argument("--dataset", type=str, default="nations")
    parser.add_argument("--output_postfix", type=str)
    parsed_args = parser.parse_args()
    parsed_args = parsed_args.__dict__
    return parsed_args

def get_vec_lm(text,type="st"):
    # st -> sentence transformer, ft-> fasttext embedding
    return encoder.encode([text]) if type=="st" else vec.get_vector(text).reshape(1,-1)

def process_embedding(datadir,emb_type="st", save_extra=None):

    entities = pd.read_table(join(datadir, "entities.dict"), header=None)
    try:
        relations = pd.read_table(join(datadir, "relations.dict"), header=None)
    except:
        pass

    entities_id = list(entities[0].values)
    entities_text = list(entities[1].values)
    try:
        relations_id = list(relations[0].values)
        relations_text = list(relations[1].values)
    except:
        pass
    entity_embedding = [get_vec_lm(ent,type=emb_type) for ent in entities_text]
    try:
        relation_embedding = [get_vec_lm(rel,type=emb_type) for rel in relations_text]
    except:
        pass
    entity_embedding_arr =np.array(entity_embedding)
    try:
        relation_embedding_arr = np.array(relation_embedding)
    except:
        pass
    np.save(os.path.join(datadir, 'entity_embedding_'+ emb_type + '.npy'), entity_embedding_arr.squeeze(1))
    try:
        np.save(os.path.join(datadir, 'relation_embedding_'+ emb_type + '.npy'), relation_embedding_arr.squeeze(1))
    except:
        pass
    #entity_id_to_emb = dict(zip(entities_id, entity_embedding))
    #rel_id_to_emb = dict(zip(relations_id, relation_embedding))
    #pickle.dump(entity_id_to_emb, open(join(datadir, "lm_ent_emb.pkl" if not save_extra else "lm_ent_emb_"+emb_type+".pkl"), "wb"))
    #pickle.dump(rel_id_to_emb, open(join(datadir,"lm_rel_emb.pkl" if not save_extra else "lm_rel_emb_"+emb_type+".pkl"), "wb"))
    print("Saved the embedding!!")


if __name__ == "__main__":
    args = get_args()

    target_type = "st"

    process_embedding("datasets/WN18RR_old/mapped/updated",emb_type=target_type)
    process_embedding("datasets/WN18RR_old/mapped/updated", emb_type="ft", save_extra=True)
    process_embedding("datasets/WN18RR_old/mapped/updated", emb_type="st", save_extra=True)


