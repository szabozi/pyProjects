import random
import re


class DecisionMaker:

    @staticmethod
    def roll_dice(sides=20):
        """
        Roll a die with the given number of sides.
        Default: D20
        """
        if sides < 1:
            raise ValueError("Number of sides must be at least 1!")
        return random.randint(1, sides)

    @staticmethod
    def roll_custom_dice(expression="1d20"):
        """
        Roll dice based on a custom expression (e.g. '2d6, '3d10+5').
        """
        match = re.match(r"(\d+)d(\d+)([+-]\d+)?", expression)
        if not match:
            raise ValueError("Invalid dice expression!")

        num_dice, sides, modifier = match.groups()
        num_dice = int(num_dice)
        sides = int(sides)
        modifier = int(modifier) if modifier else 0

        total = sum(DecisionMaker.roll_dice(sides) for _ in range(num_dice))
        return total + modifier

    @staticmethod
    def yes_no_question(probability=50):
        """
        Determine the results of a yes/no question based on probability.
        Probability is given as a percentage chance of 'yes'.
        Default: 50% chance of 'yes'
        """
        if not (0 <= probability <= 100):
            raise ValueError("Probability must be between 0 and 100!")
        roll = DecisionMaker.roll_dice(100)
        return roll <= probability

    @staticmethod
    def complex_decision(options):
        """
        Make a complex decision from a list of options.
        Each option is a dictionary with 'result' and 'weight'.
        """
        if not options:
            raise ValueError("Options list cannot be empty!")

        total_weight = sum(option['weight'] for option in options)

        if total_weight <= 0:
            raise ValueError("Total weight must be greater than 0!")

        roll = DecisionMaker.roll_dice(total_weight)
        current = 0
        for option in options:
            current += option['weight']
            if roll <= current:
                return option['result']


oracle = DecisionMaker()
result = oracle.yes_no_question(60)
print(f"Yes/No Results: {'Yes' if result else 'No'}")

decision = DecisionMaker.complex_decision([
    {'result': 'Go left', 'weight': 5},
    {'result': 'Go right', 'weight': 3},
    {'result': 'Go straight', 'weight': 2}
])
print(f"Complex Decision Result {decision}")

custom_roll = DecisionMaker.roll_custom_dice("2d6+3")
print(f"Custom Dice Roll Results: {custom_roll}")
