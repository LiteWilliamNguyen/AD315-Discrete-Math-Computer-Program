from components.probability_experiment import coin_toss, die_roll, compound_coin_toss, drawing_card

def main():
    print("Probability Experiment Menu:")
    print("1. Coin Toss")
    print("2. Die Roll")
    print("3. Drawing Card")
    print("4. Compound Coin Toss")
    print("5. Quit")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            n = int(input("Enter the number of coin tosses: "))
            coin_toss(n)
            print(f"Coin toss results: {coin_toss(n)}")
        elif choice == "2":
            n = int(input("Enter the number of die rolls: "))
            die_roll(n)
            print(f"Die roll results: {die_roll(n)}")
        elif choice == "3":
            n = int(input("Enter the number of card draws: "))
            red_count, black_count = drawing_card(n)
            print(f"Drawing card results: Red={red_count}, Black={black_count}")
        elif choice == "4":
            n = int(input("Enter the number of coin tosses: "))
            both_heads, at_least_one_heads = compound_coin_toss(n)
            print(f"Compound coin toss results: Both heads={both_heads}, At least one head={at_least_one_heads}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()