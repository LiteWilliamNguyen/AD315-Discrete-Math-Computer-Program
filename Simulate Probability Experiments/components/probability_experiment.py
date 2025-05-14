import random
from collections import Counter

# Function to simulate a coin toss experiment
# Write a program to simulate tossing a coin 100 times, count the number of heads and tails, and plot the results.
def coin_toss(n):
    outcomes = [random.choice(["Heads", "Tails"]) for _ in range(n)]
    count = Counter(outcomes)
    return count

# Function to simulate a die roll experiment
# Simulate rolling a six-sided die 60 times, print the frequency of each outcome, and plot the distribution.
def die_roll(n):
    outcomes = [random.randint(1,6) for _ in range(n)]
    count = Counter(outcomes)
    return count

# Function to simulate drawing a card from a shuffled deck
# Simulate drawing a card from a shuffled deck 20 times, count how many are red, and plot the count of red versus black cards.
def drawing_card(n):
    if n is None:
        raise ValueError("Invalid deck")
    if n < 0:
        raise ValueError("Invalid deck")
    else:
        # Create a deck of cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [suit for suit in suits for _ in range(13)]
        random.shuffle(deck)
        # Draw cards
        draws = deck[:n]
        # Count the number of red and black cards
        red_count = sum( 1 for card in draws if card in ['Hearts', 'Diamonds'])
        black_count = sum( 1 for card in draws if card in ['Clubs', 'Spades'])
        return red_count, black_count
    

# Simulate coin toss and compute compound events
# Simulate flipping two coins 50 times, count the outcomes, and plot both scenarios: both heads and at least one head.
def compound_coin_toss(n):
    if n == 0:
        return []
    else:
        outcomes = [(random.choice(['Heads', 'Tails']), random.choice(['Heads', 'Tails'])) for _ in range(n)]
        # Count the number of outcomes where both coins are heads
        both_heads = sum(1 for a , b in outcomes if a=='Heads' and b=='Heads')
        # Count the number of outcomes where at least one coin is heads
        at_least_one_heads = sum(1 for a , b in outcomes if a=='Heads' or b=='Heads')
        return both_heads, at_least_one_heads