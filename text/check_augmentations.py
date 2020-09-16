import collections


def load_vocab(vocab_file):
  """Loads a vocabulary file into a dictionary."""
  vocab = collections.OrderedDict()
  inv_vocab =  collections.OrderedDict()
  index = 0
  with open(vocab_file, 'r') as f:
    for line in f.readlines():
      token = line.strip('\n')
      vocab[token] = index
      inv_vocab[str(index)] = token
      index += 1
  return vocab, inv_vocab


if __name__ == "__main__":
    vocab, inv_vocab = load_vocab("pretrained_models/bert_base/vocab.txt")


    unsup_file = open("data/back_translation/imdb_back_trans/unsup_in/sample_0.9/para/para_0.txt", 'r')

    vec_file = open("data/proc_data/IMDB/unsup/bt-0.9/0/data.txt", 'r')


    unsup_line = unsup_file.readline()
    print(unsup_line)

    vec_line = vec_file.readline()
    tab_split_vec_line = vec_line.strip('\n').split('\t')
    input_id = tab_split_vec_line[0]
    aug_input_id = tab_split_vec_line[3]


    input_line = []
    input_id_vec = input_id.split(' ')
    for i in input_id_vec:
        input_line.append(inv_vocab[i])


    aug_input_line = []
    aug_input_id_vec = aug_input_id.split(' ')
    for i in aug_input_id_vec:
        aug_input_line.append(inv_vocab[i])

    import pdb
    pdb.set_trace()


