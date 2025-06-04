"""Write a program to generate an arithmetic sequence.
The program should ask for the first term, common difference, and the number of terms."""
def generate_arithmetic_sequence(first_term, common_difference, number_of_terms):
    sequence = []
    current_term = first_term
    if number_of_terms <= 0:
        return None
    else: 
        for _ in range(number_of_terms):
            sequence.append(current_term)
            current_term += common_difference
        return sequence
#Calculate the sum of an arithmetic or geometric sequence.
def calculate_sum(sequence):
    if sequence is None:
        return None
    if len(sequence) == 0:
        return 0
    return sum(sequence)

def generate_geometric_sequence(first_term, common_ratio, number_of_terms):
    sequence = []
    current_term = first_term
    if number_of_terms <= 0:
        return None
    else:
        for _ in range(number_of_terms):
            sequence.append(current_term)
            current_term *= common_ratio 
            #Same thing as current_term = current_term * common_ratio
        return sequence


