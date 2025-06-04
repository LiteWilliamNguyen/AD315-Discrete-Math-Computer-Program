import logic_sequence_generator

def main():
    print("Sequence Generator")
    print("1. Arithmetic Sequence")
    print("2. Geometric Sequence")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        first_term = float(input("Enter the first term: "))
        common_difference = float(input("Enter the common difference: "))
        number_of_terms = int(input("Enter the number of terms: "))
        if number_of_terms <= 0:
            print("Invalid number of terms. Please enter a positive integer.")
            return
        else:
            sequence = logic_sequence_generator.generate_arithmetic_sequence(first_term, common_difference, number_of_terms)
            print("Arithmetic Sequence:", sequence)
            print("Sum:", logic_sequence_generator.calculate_sum(sequence))
    elif choice == '2':
        first_term = float(input("Enter the first term: "))
        common_ratio = float(input("Enter the common ratio: "))
        number_of_terms = int(input("Enter the number of terms: "))
        if number_of_terms <= 0:
            print("Invalid number of terms. Please enter a positive integer.")
            return
        else:
            sequence = logic_sequence_generator.generate_geometric_sequence(first_term, common_ratio, number_of_terms)
            print("Geometric Sequence:", sequence)
            print("Sum:", logic_sequence_generator.calculate_sum(sequence))
    elif choice == '3':
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    
    
    

if __name__ == '__main__':
    main() 