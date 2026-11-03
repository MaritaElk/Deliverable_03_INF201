import random


class Dice:
    """Represent a dice with a configurable number of sides."""
    def __init__(self, sides: int = 6):
        """
        Initialize a dice with a specified number of sides.

        Args:
            sides (int): Number of sides. Default is 6.
                         Must be at least 2.

        Raises:
            ValueError: If the number of sides is less than 2.
        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")

        self.sides = sides

    def roll(self) -> int:
        """
        Roll the dice and return a random integer.

        Returns:
            int: A random integer between 1 and the number of sides.
        """
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """
        Return a string representation of the dice.

        Returns:
            str: The dice representation in the format Dice(sides=n).
        """
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """
        Roll the dice by calling the object directly.

        Returns:
            int: A random integer between 1 and the number of sides.
        """
        return self.roll()