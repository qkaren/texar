
num_epochs = 100
display = 100

data_path = '../transformer/data/tf_data'
#
#data_path = '/home/hzt/qin/msr_texar/data/'
#data_path = '/space/hzt/msr_dialog/data/'
source_vocab_file = data_path + '/vocab.txt'
target_vocab_file = data_path + '/vocab.txt'
#data_path = '/home/hzt/qin/msr_texar/texar/examples/text_style_transfer/data/yelp/'
#source_vocab_file = data_path + '/vocab'
#target_vocab_file = data_path + '/vocab'

train = {
    'batch_size': 64,
    'allow_smaller_final_batch': False,
    'source_dataset': {
        "files": data_path + '/train.query',
        #"files": data_path + '/sentiment.train.text',
        'vocab_file': source_vocab_file,
        'max_seq_length': 100
    },
    'target_dataset': {
        'files': data_path + '/train.response',
        #"files": data_path + '/sentiment.train.text',
        'vocab_file': target_vocab_file,
        'max_seq_length': 50
    }
}
val = {
    'batch_size': 64,
    'shuffle': False,
    'source_dataset': {
        "files": data_path + '/dev.query',
        #"files": data_path + '/sentiment.dev.text',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': data_path + '/dev.response',
        #"files": data_path + '/sentiment.dev.text',
        'vocab_file': target_vocab_file,
    }
}
test = {
    'batch_size': 64,
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
