# Attentional Seq2seq model.
# Hyperparameters not specified here will take the default values.

num_units = 1000 #256
beam_width = 10

embedder = {
    'dim': num_units
}
encoder = {
    'rnn_cell_fw': {
        'kwargs': {
            'num_units': num_units
        },
        'num_layers': 2,
        #'dropout': {
        #    'input_keep_prob': 0.5
        #}
    }
}
decoder = {
    'rnn_cell': {
        'kwargs': {
            'num_units': num_units
        },
        #'dropout': {
        #    'input_keep_prob': 0.5,
        #    'output_keep_prob': 0.5
        #},
    },
    'attention': {
        'kwargs': {
            'num_units': num_units,
        },
        'attention_layer_size': num_units
    }
}

opt = {
    'optimizer': {
        'type':  'AdamOptimizer',
        'kwargs': {
            'learning_rate': 0.001
        },
    },
    "gradient_clip": {
        "type": "clip_by_global_norm",
        "kwargs": {"clip_norm": 5.}
    },
}
