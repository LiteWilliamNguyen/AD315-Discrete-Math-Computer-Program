from logic import conjunction, disjunction, negation, implication, biconditional
# Function to get boolean input from the user
def get_boolean_input(prompt):
    # Loop until valid input is provided
    while True:
        # Get user input and strip any leading/trailing whitespace
        value = input(f"{prompt} (Enter 1 for True or 0 For False): ").strip()
        # Check if input is either "0" or "1"
        if value in ["0", "1"]:
            # Return the boolean equivalent of the input
            return bool(int(value))
        # If input is not "0" or "1", print an error message
        print("Invalid input. Please enter 1 or 0.")

# Function to display the results of logical operations
def display(a, b):
    # Print header for results
    print("Results: ")
    # Print the results of conjunction, disjunction, negation, implication, and biconditional operations
    print(f"A AND B: {conjunction(a, b)}")
    print(f"A OR B: {disjunction(a, b)}")
    print(f"NOT A: {negation(a)}")
    print(f"NOT B: {negation(b)}")
    print(f"A -> B (Implication): {implication(a, b)}")
    print(f"A <-> B (Biconditional): {biconditional(a, b)}")

# Function to generate a truth table for logical operations
def generate_truth_table():
    # Print header for truth table
    print("\nTruth Table:")
    print(f"{'A':<5}{'B':<5}{'A AND B':<10}{'A OR B':<10}{'NOT A':<8}{'NOT B':<8}{'A → B':<8}{'A ↔ B'}")
    print("-" * 60)
    # Loop through all possible combinations of A and B
    for a in [False, True]:
        for b in [False, True]:
            # Print the results of each operation for the current combination of A and B
            print(f"{int(a):<5}{int(b):<5}"
                  f"{int(conjunction(a, b)):<10}"
                  f"{int(disjunction(a, b)):<10}"
                  f"{int(negation(a)):<8}"
                  f"{int(negation(b)):<8}"
                  f"{int(implication(a, b)):<8}"
                  f"{int(biconditional(a, b))}")

# Main function
def main():
    # Print welcome message and menu options
    print("=== Logical Operations Evaluator ===")
    print("Select an option:")
    print("1. Evaluate Logical Operations with custom inputs")
    print("2. Generate Truth Table")
    # Get user's choice
    choice = input("Enter 1 or 2: ").strip()

    # Handle user's choice
    if choice == '1':
        # Get custom inputs for A and B
        a = get_boolean_input("Enter value for A")
        b = get_boolean_input("Enter value for B")
        # Display the results of logical operations
        display(a, b)
    elif choice == '2':
        # Generate truth table
        generate_truth_table()
    else:
        # Print error message if invalid choice is made
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()