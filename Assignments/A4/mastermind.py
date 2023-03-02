from logic import *

colors = ["red", "blue", "green", "purple"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color.


# Only one color per position.


# First Guess
knowledge.add()

# Second Guess
knowledge.add()

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
