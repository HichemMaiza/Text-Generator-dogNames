import numpy as np
import pickle

def read_parameters(file_name):

    with open(file_name, 'rb') as handle:
        parameters = pickle.load(handle)
    return parameters


def read_data(file_name):
    
    data = open(file_name, 'r').read()
    data = data.lower()
    chars = list(set(data))
    data_size, vocab_size = len(data), len(chars)

    char_to_ix = { ch:i for i,ch in enumerate(sorted(chars)) }
    ix_to_char = { i:ch for i,ch in enumerate(sorted(chars)) }

    return char_to_ix, ix_to_char

def sample(parameters, char_to_ix, seed):
    
    # Retrieve parameters and relevant shapes from "parameters" dictionary
    Waa, Wax, Wya, by, b = parameters['Waa'], parameters['Wax'], parameters['Wya'], parameters['by'], parameters['b']
    vocab_size = by.shape[0]
    n_a = Waa.shape[1]

    # Create the one-hot vector x for the first character (initializing the sequence generation)
    x = np.zeros(shape = (vocab_size,1))
    a_prev = np.zeros(shape=(n_a,1))
    
    # Create an empty list of indices, this is the list which will contain the list of indices of the characters to generate
    indices = []
    idx = -1 
    
    counter = 0
    newline_character = char_to_ix['\n']
    
    while (idx != newline_character and counter != 50):
        
        # Step 2: Forward propagation 
        a = np.tanh(np.dot(Wax,x)+np.dot(Waa,a_prev)+b)
        z = np.dot(Wya,a)+by
        y = softmax(z)
        
        # Step 3: Sample the index of a character within the vocabulary from the probability distribution y
        idx = np.random.choice(list(range(vocab_size)) , p = y.ravel())
        # Append the index to "indices"
        indices.append(idx)
        
        # Step 4: Overwrite the input character as the one corresponding to the sampled index.
        x = np.eye(vocab_size)[idx].T.reshape(vocab_size,-1)
   
        # Update "a_prev" to be "a"
        a_prev = a
        
        
    if (counter == 50):
        indices.append(char_to_ix['\n'])
    
    return indices

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) 

def print_sample(sample_ix, ix_to_char):
    txt = ''.join(ix_to_char[ix] for ix in sample_ix)
    txt = txt[0].upper() + txt[1:]  # capitalize first character 
    print ('%s' % (txt, ), end='') 


"""
data  = open("Dog_Names.csv", 'r').read().split('\n')[1:-1] 
names = []
for couple in data:
    names.append(couple.split(',')[0])
fh = open("dogs.txt", "a") 
for i in names:
    fh.write(i+'\n') 
fh.close 
"""