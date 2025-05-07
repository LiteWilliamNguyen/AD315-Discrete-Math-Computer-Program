import math

def calculate_permutation(n, r):
    #P(n,r) = n! / (n-r)!
    #invalid input
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError("Inputs must be integers")
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid input for permutation: Ensure that 0 ≤ r ≤ n and both are non-negative.")
    return math.factorial(n) // math.factorial(n - r)

def calculate_combination(n, r):
    #C(n,r) = n! / (r! * (n-r)!)
    #invalid input
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError("Inputs must be integers")
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid input for combination: Ensure that 0 ≤ r ≤ n and both are non-negative.")
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))