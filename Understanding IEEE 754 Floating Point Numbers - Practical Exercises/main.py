#Understanding IEEE 754 Floating Point Numbers - Practical Exercises


import struct
import decimal
import sys
import numpy as np
import matplotlib.pyplot as plt

#1. Convert Decimal to IEEE 754 Format
"""Write a function to convert a decimal number to its IEEE 754 
32-bit single-precision floating-point binary representation."""


def convert_decimal_to_ieee754(decimal):
    # Convert decimal to float
    float_num = float(decimal)
    
    # Use struct.pack to convert float to binary
    binary = struct.pack('>f', float_num)
    
    # Convert binary to binary string
    binary_str = ''.join(format(byte, '08b') for byte in binary)
    
    return binary_str

# Test the function
print("Converting 3.14 to IEEE 754: "+convert_decimal_to_ieee754(3.14))


#2. Arithmetic Operations
"""Perform the following arithmetic operations in your chosen programming language and show the IEEE 754 results:
0.1 + 0.2
1.0/3.0"""

print("0.1 + 0.2: " ,  0.1 + 0.2, "IEEE 754: "+ convert_decimal_to_ieee754(0.1 + 0.2))
print("1.0/3.0: " ,  1.0/3.0, "IEEE 754: "+ convert_decimal_to_ieee754(1.0/3.0))    
"""The discrepancies observed from the expected decimal results are due to the limitations of floating-point representation in computers.
The expected result is 0.3, but the actual result is 0.30000000000000004. This discrepancy is due to the way floating-point numbers are represented in binary.
In binary, 0.1 is represented as 0.00011001100110011... (a repeating fraction), and 0.2 is represented as 0.0011001100110011... (also a repeating fraction). 
When you add these two numbers, the result is not exactly 0.3, but rather a close approximation."""

#3. Special Values Handling
"""Write code to generate positive infinity, negative infinity, and NaN using arithmetic operations. 
Verify by checking their properties (like checking if NaN is not equal to itself)."""

# Generate positive infinity
pos_inf = 1e308 * 1e308
print(pos_inf)  # prints: inf

# Generate negative infinity
neg_inf = -1e308 * 1e308
print(neg_inf)  # prints: -inf

# Generate NaN
nan = pos_inf + neg_inf
print(nan)  # prints: nan

# Verify properties
print("pos_inf == float('inf')")
print(pos_inf == float('inf'))  # prints: True
print("neg_inf == float('-inf')")
print(neg_inf == float('-inf'))  # prints: True
print("nan == nan")
print(nan == nan)  # prints: False
print("nan != nan")
print(nan != nan)  # prints: True
print("pos_inf > neg_inf") 
print(pos_inf > neg_inf)  # prints: True
print("pos_inf + neg_inf")  
print(pos_inf + neg_inf)# prints: nan
print("nan + pos_inf")  
print(nan + pos_inf)  # prints: nan
print("nan + neg_inf") 
print(nan + neg_inf)  # prints: nan

#4. Rounding Modes
"""Experiment with different rounding modes available in your programming environment. 
Provide examples where different rounding modes lead to different results."""

# Set the decimal context to use 2 decimal places
decimal.getcontext().prec = 4

# Define a number to round
num = 1.2345

# Round using different rounding modes
print("Round to nearest:", decimal.Decimal(num).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP))
print("Round up:", decimal.Decimal(num).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_CEILING))
print("Round down:", decimal.Decimal(num).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_FLOOR))


# Define another number to round
num = 1.2355

# Round using different rounding modes
print("\nRound to nearest:", decimal.Decimal(num).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP))
print("Round up:", decimal.Decimal(num).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_CEILING))
print("Round down:", decimal.Decimal(num).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_FLOOR))


#5. Underflow and Overflow
"""Demonstrate underflow and overflow scenarios with specific examples."""
# Define a very small number
small_number= sys.float_info.min/2
# Print the small number
print("Small number:", small_number)
# Perform an arithmetic operation that causes underflow
result = small_number / 2
# Print the result
print("Result:", result)
"""perform an arithmetic operation that causes underflow by dividing small_num by 2. The result is zero, which is an example of underflow."""

# Define a very large number
large_num = sys.float_info.max * 2

# Print the large number
print("Large number:", large_num)

# Perform an arithmetic operation that causes overflow
result = large_num * 2

# Print the result
print("Result:", result)
"""perform an arithmetic operation that causes overflow by multiplying large_num by 2. The result is infinity, which is an example of overflow."""


#6. Visualizing Precision Loss
"""Create a plot to visualize the loss of precision that occurs as numbers become very small (denormalized numbers) or very large."""
# Create an array of numbers from 1e-100 to 1e100
numbers = np.logspace(-100, 100, 1000)

# Calculate the absolute error for each number
absolute_error = np.abs(numbers - np.float32(numbers))

# Create a plot of the absolute error
plt.plot(numbers, absolute_error)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number')
plt.ylabel('Absolute Error')
plt.title('Loss of Precision for Small and Large Numbers')
plt.show()

#Comparative Study
"""Compare how different programming languages or systems handle IEEE 754 arithmetic differently. 
This can involve differences in default rounding modes, how exceptions like overflow or underflow are handled, etc."""

"""
Between Java and Python, handling IEEE 754 arithmetic:
Java throws an exception when an overflow or underflow occurs, while Python simply returns the appropriate infinity or zero value.
"""