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
        elif choice == "2":
            n = int(input("Enter the number of die rolls: "))
            die_roll(n)
        elif choice == "3":
            n = int(input("Enter the number of card draws: "))
            drawing_card(n)
        elif choice == "4":
            n = int(input("Enter the number of coin tosses: "))
            compound_coin_toss(n)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()