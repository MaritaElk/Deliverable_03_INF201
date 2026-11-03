import random


class Dice:
    def __init__(self, sides: int = 6):
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")

        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Return a string representation of the dice."""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Roll the dice when the object is called."""
        return self.roll()