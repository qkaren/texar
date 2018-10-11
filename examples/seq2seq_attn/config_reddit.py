
num_epochs = 100
display = 50 #100

#data_path = '../transformer/data/tf_data'
data_path = '/home/hzt/qin/msr_texar/data_small/'
source_vocab_file = data_path + '/vocab.txt'
target_vocab_file = data_path + '/vocab.txt'

train = {
    'batch_size': 32,
    'allow_smaller_final_batch': False,
    'source_dataset': {
        "files": data_path + '/train.query',
        'vocab_file': source_vocab_file,
        'max_seq_length': 50
    },
    'target_dataset': {
        'files': data_path + '/train.query', #'/train.response',
        'vocab_file': target_vocab_file,
        'max_seq_length': 50
    }
}
val = {
    'batch_size': 32,
    'shuffle': False,
    'source_dataset': {
        "files": data_path + '/dev.query',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': data_path + 'dev.query', #'/dev.response',
        'vocab_file': target_vocab_file,
    }
}
test = {
    'batch_size': 32,
    'shuffle': False,
    'source_dataset': {
        "files": data_path + '/test.query',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': data_path + '/test.response',
        'vocab_file': target_vocab_file,
    }
}
