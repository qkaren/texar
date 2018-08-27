# -*- coding: utf-8 -*-
"""
configurate the hyperparameters, based on command line arguments.
"""
import argparse
import copy
import os

def load_hyperparams():
    """
        main function to define hyperparams
    """
    # pylint: disable=too-many-statements
    class Hyperparams(): pass
    args = Hyperparams()
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--wbatchsize', type=int, default=2048)
    argparser.add_argument('--start_epoch', type=int, default=0)
    argparser.add_argument('--mode', type=str,
                           default='train_and_evaluate',
                           help='can also be test mode')
    argparser.add_argument('--src_language', type=str, default='en')
    argparser.add_argument('--tgt_language', type=str, default='de')
    argparser.add_argument('--filename_prefix', type=str, default='processed.')
    argparser.add_argument('--model_dir', type=str, default='default')
    argparser.add_argument('--model_filename', type=str, default='')
    argparser.add_argument('--verbose', type=int, default=0)
    argparser.add_argument('--test_batch_size', type=int, default=64)
    argparser.add_argument('--eval_steps', type=int, default=2000)
    argparser.add_argument('--max_training_steps', type=int, default=500000,\
        help='''max training steps. In most cases, the model can converge in
             the small default max_train_epoch epoches,
             so this argument is not use.''')
    argparser.add_argument('--warmup_steps', type=int, default=16000)
    argparser.add_argument('--lr_constant', type=float, default=2)
    argparser.add_argument('--max_train_epoch', type=int, default=20)
    argparser.add_argument('--random_seed', type=int, default=1234)
    argparser.add_argument('--log_disk_dir', type=str)
    argparser.add_argument('--beam_width', type=int, default=5)
    argparser.add_argument('--alpha', type=float, default=0.6,\
        help=' length_penalty=(5+len(decode)/6) ^ -\alpha')
    argparser.add_argument('--save_eval_output', default=1, \
        help='save the eval output to file')
    argparser.add_argument('--eval_interval_epoch', type=int, default=1)
    argparser.add_argument('--eval_criteria', type=str, default='bleu')
    argparser.add_argument('--pre_encoding', type=str, default='spm')
    argparser.add_argument('--max_decode_len', type=int, default=256)
    argparser.parse_args(namespace=args)
    args.input = 'temp/run_{}_{}_{}/data'.format(
        args.src_language, args.tgt_language, args.pre_encoding)

    # pylint: disable=attribute-defined-outside-init
    # pylint: disable=no-member
    args.filename_suffix = '.' + args.pre_encoding +'.txt'
    args.train_src = os.path.join(args.input, \
        '{}train.{}{}'.format(args.filename_prefix,
                              args.src_language, args.filename_suffix))
    args.train_tgt = os.path.join(args.input, \
        '{}train.{}{}'.format(args.filename_prefix,
                              args.tgt_language, args.filename_suffix))
    args.dev_src = os.path.join(args.input, \
        '{}dev.{}{}'.format(args.filename_prefix,
                            args.src_language, args.filename_suffix))
    args.dev_tgt = os.path.join(args.input, \
        '{}dev.{}{}'.format(args.filename_prefix,
                            args.tgt_language, args.filename_suffix))
    args.test_src = os.path.join(args.input, \
        '{}test.{}{}'.format(args.filename_prefix,
                             args.src_language, args.filename_suffix))
    args.test_tgt = os.path.join(args.input, \
        '{}test.{}{}'.format(args.filename_prefix,
                             args.tgt_language, args.filename_suffix))

    args.vocab_file = os.path.join(args.input, \
        args.filename_prefix + 'vocab.pickle')
    log_params_dir = '{}_{}/'.format(\
        args.src_language, args.tgt_language, args.wbatchsize, \
        args.max_train_epoch, args.lr_constant, args.warmup_steps)
    args.log_dir = os.path.join(args.log_disk_dir, log_params_dir)
    args.hidden_dim = 512
    args.word_embedding_hparams = {
        'name': 'lookup_table',
        'dim': args.hidden_dim,
        'initializer': {
            'type': 'random_normal_initializer',
            'kwargs': {
                'mean':0.0,
                'stddev':args.hidden_dim**-0.5,
            },
        }
    }
    encoder_hparams = {
        'position_embedder_hparams': {
            'name': 'sinusoids',
        },
        'dim': args.hidden_dim,
        'initializer': {
            'type': 'variance_scaling_initializer',
            'kwargs': {
                'scale':1.0,
                'mode':'fan_avg',
                'distribution':'uniform',
            },
        },
    }
    decoder_hparams = copy.deepcopy(encoder_hparams)
    decoder_hparams['embedding_tie'] = True
    decoder_hparams['max_decoding_length'] = args.max_decode_len
    loss_hparams = {
        'label_confidence': 0.9,
    }

    opt_hparams = {
        'learning_rate_schedule':
            'constant.linear_warmup.rsqrt_decay.rsqrt_depth',
        'lr_constant': args.lr_constant * (args.hidden_dim ** -0.5),
        'static_lr': 1e-3,
        'warmup_steps': args.warmup_steps,
        'max_training_steps': args.max_training_steps,
        'Adam_beta1':0.9,
        'Adam_beta2':0.997,
        'Adam_epsilon':1e-9,
    }

    print('logdir:{}'.format(args.log_dir))
    if not os.path.exists(args.log_dir):
        os.makedirs(args.log_dir)
    return {
        'encoder_hparams': encoder_hparams,
        'decoder_hparams': decoder_hparams,
        'loss_hparams': loss_hparams,
        'opt_hparams': opt_hparams,
        'args': args,
        }