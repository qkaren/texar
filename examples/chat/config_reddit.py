batch_size =256  #256
test_batch_size = 4

max_train_epoch = 100
display_steps = 200

eval_steps = 10000 #4000 #2000

max_decoding_length= 30

filename_prefix = "processed."
input_dir = 'temp/run_query_response_bpe/data'
vocab_file = input_dir + '/processed.vocab.pickle'
