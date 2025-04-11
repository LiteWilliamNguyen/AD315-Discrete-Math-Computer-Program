def multi_base_numerical_converter(number):
    """Convert a number into binary, octal, and hexadecimal forms."""
    """decimal_number = number"""
    """Need to remove '0b' from binary_form, '0o' from octal_form, and '0x' from hexadecimal_form"""
    binary_form = bin(number)[2:]
    octal_form = oct(number)[2:]
    hexadecimal_form = hex(number)[2:].upper()
    
    return binary_form, octal_form, hexadecimal_form

    
if __name__ == "__main__":
    print("Multi-Base Numerical Converter")
    print("-----------------------------")
    number = int(input("Enter a positive integer: "))
    print("Select option to display the result:")
    print("1. Binary")
    print("2. Octal")
    print("3. Hexadecimal")
    print("4. All formats")

    choice = int(input("Enter your choice (1-4): "))
    binary_form, octal_form, hexadecimal_form = multi_base_numerical_converter(number)

    if choice == 1:
        print(f"Binary: {binary_form}")
    elif choice == 2:
        print(f"Octal: {octal_form}")
    elif choice == 3:
        print(f"Hexadecimal: {hexadecimal_form}")
    elif choice == 4:
        print(f"Decimal: {number}")
        print(f"Binary: {binary_form}")
        print(f"Octal: {octal_form}")
        print(f"Hexadecimal: {hexadecimal_form}")
    else:
        print("Invalid choice.")