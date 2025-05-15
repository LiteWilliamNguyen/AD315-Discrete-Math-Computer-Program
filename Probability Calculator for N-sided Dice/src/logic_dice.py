import random
from collections import Counter

#Develop a program that calculates the probability distribution when rolling M number of N-sided dice.
#Write a function that simulates rolling M number of N-sided dice once and returns the sum of the outcomes.
def roll_dice(num_dice, num_sides):
    return sum(random.randint(1, num_sides) for _ in range(num_dice))

#Create a function to simulate rolling M number of N-sided dice K times and record the results.
def simulate_rolling_dice(num_dice, num_sides, num_rolls):
    return [roll_dice(num_dice, num_sides) for _ in range(num_rolls)]


#Write a function to calculate the probability of each possible sum when M number of N-sided dice are rolled.
def calculate_probability(num_dice, num_sides, num_rolls):
    outcomes  = simulate_rolling_dice(num_dice, num_sides, num_rolls)
    counter = Counter(outcomes)
    total_rolls = len(outcomes)
    probabilities = {outcome: count / total_rolls for outcome, count in counter.items()}
    return probabilities