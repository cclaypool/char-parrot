## Model configuration

# Whether to use the GPU for computation
gpu = False
# The type of recurrent model to use: "gru" or "lstm" (case insensitive)
model_type = "gru"
# File containing the training dataset. This is an example dataset containing
# one of Grimms' Fairy Tales from Project Gutenberg
dataset_file = "the_golden_bird.txt"
# Whether the training is case-sensitive
case_sensitive = True
# The number of previous characters the model will use
# to predict the next character
time_steps = 16
# The size of each batch of training examples
batch_size = 32
# The size of the hidden state of the recurrent layer(s)
hidden_size = 128
# The number of recurrent layers
nb_layers = 1
# The rate of dropout after the each layer
dropout = 0.2
# The learning rate for the RMSprop optimizer
learning_rate = 0.002
# Whether to zero the hidden state of the recurrent layer(s)
# after each batch of training examples
zero_hidden = True
