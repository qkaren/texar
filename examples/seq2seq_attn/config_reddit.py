
num_epochs = 100
display = 100

data_path = '../../KB_dialog/tf_data'
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
        'files': data_path + '/train.response',
        'vocab_file': target_vocab_file,
        'max_seq_length': 50
    }
}
val = {
    'batch_size': 32,
    'shuffle': False,
    'source_dataset': {
        "files": data_path + '/valid.query',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': data_path + '/valid.response',
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
