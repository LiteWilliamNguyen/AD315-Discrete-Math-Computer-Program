from itertools import chain, combinations

def get_power_set(input_set):
    "Generate the power set of a set"
    #Convert input_set to a list
    s = list(input_set)
    #Generates all possible combinations of the input set with lengths ranging from 0 to the length of the input set. 
    power_set = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    #Converts each combination back into a set and returns the list of all subsets.
    return [set(item) for item in power_set]