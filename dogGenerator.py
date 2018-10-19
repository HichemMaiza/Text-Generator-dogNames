from utils import*
import sys 

def main() : 
    # read model parameters
    parameters = read_parameters("dogsModel.pickle")
    # read data 
    char_to_ix, ix_to_char = read_data("dogs.txt")

    seed = np.random.randint(100)
    #seed = 0

    if sys.argv[1]: 
        names = int(sys.argv[1]) 
    else:
        names = 5

    for name in range(names):
        sampled_indices = sample(parameters, char_to_ix, seed)
        print_sample(sampled_indices, ix_to_char)
        seed+=1

if __name__ == '__main__': 
    main()