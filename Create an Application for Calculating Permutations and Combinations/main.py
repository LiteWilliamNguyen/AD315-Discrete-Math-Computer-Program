from math_logic import calculate_permutation, calculate_combination

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("=== Permutation and Combination Calculator ===")
    print("1. Calculate Permutation P(n, r)")
    print("2. Calculate Combination C(n, r)")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (0-2): ")

        if choice == '0':
            print("Exiting program.")
            break

        elif choice in ['1', '2']:
            n = get_integer("Enter value of n (total items): ")
            r = get_integer("Enter value of r (items chosen or arranged): ")

            try:
                if choice == '1':
                    result = calculate_permutation(n, r)
                    print(f"\nPermutation P({n}, {r}) = {result}\n")
                else:
                    result = calculate_combination(n, r)
                    print(f"\nCombination C({n}, {r}) = {result}\n")
            except ValueError as e:
                print(f"Error: {e}")

        else:
            print("Invalid choice. Please enter 0, 1, or 2.")
            
if __name__ == "__main__":
    main()
