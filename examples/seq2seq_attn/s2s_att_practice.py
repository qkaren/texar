from __future__ import import absolute_import
from __future__ import import print_function
from __future__ import import division

import importlib
import tensorflow as tf
import texar as tx

flags = tf.flags

config_model = importlib.import_module(FLAGS.config_model)
config_data = importlib.import_module(FLAGS.config.data)

def build_model(batch, train_data):
    source_embedder  = tx.modules.WordEmbedder(
        vocab_size=train_data.source_vocab.size, hparams=config_model.embedder)

    encoder = tx.modules.BidirectionalRNNEncoder(
        hparams=config_model.encoder)

    enc_outputs, _ = encoder(source_embedder(batch['source_text_ids']))

    target_embedder = tx.modules.WordEmbedder(
        vocab_size=train_data.target_vocab.size, hparams=config_model.embedder)

    decoder = tx.modules.AttentionRNNDecoder(
        memory=tf.concat(enc_outputs, axis=2),
        memory_sequence_length=batch['source_length'],
        vocab_size=train_data.target_vocab.size,
        hparams=config_model.decoder)

    training_outputs, _, _ = decoder(
        decoding_strategy='train_greedy',
        inputs=target_embedder(batch['target_text_ids'][:,:-1]),
        sequence_length=batch['target_length'] - 1)

    train_op = tx.core.get_train_op(
        tx.losses.sequence_sparse_softmax_cross_entropy(
            labels=batch['target_text_ids'][:,1:],
            logits=training_outputs.logits,
            sequence_length=batch['target_length'] - 1))

    start_tokens = tf.ones_like(batch['target_length']) * \
            train_data.target_vocab.bos_token_id

    beam_search_outputs, _, _ = \
        tx.modules.beam_search_decode(
            decoder_or_cell,
            embedding=target_embedder,
            start_tokens=start_tokens,
            end_token=train_data.target_vocab.eos_token_id,
            beam_width=config_model.beam_width,
            max_decoding_length=60)



