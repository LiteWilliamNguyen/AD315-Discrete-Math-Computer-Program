from src.logic_dice import calculate_probability


def main():
    print("Welcome to the Dice Probability Calculator!")
    print("Enter the number of dice, sides, and rolls:")
    try:
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on each die: "))
        num_rolls = int(input("Enter the number of times to roll the dice: "))

        if num_dice <=0 or num_sides <= 0 or num_rolls <= 0:
            raise ValueError("Number of dice, sides, and rolls must be positive integers.")

        probabilities = calculate_probability(num_dice, num_sides, num_rolls)
        print("Probability Distribution:")
        for outcome, probabilities in probabilities.items():
            print(f"{outcome}: {probabilities:.2f}")
    except Exception as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()