from get_power_set import get_power_set

def main():
    user_input = input("Provide the set elements, each separated by a space: ").strip()
    if not user_input:
        print("Input cannot be empty.")
        return
    
    input_set = set(user_input.split())
    power_set = get_power_set(input_set)

    print("Power Set: ")
    for subset in power_set:
        print(subset)


if __name__ == "__main__":
    main()