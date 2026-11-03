class Item:
    """Represent a general item in the game."""

    def __init__(self, name: str, weight: float, value: int):
        """
        Initialize an item.

        Args:
            name (str): Name of the item.
            weight (float): Weight of the item.
            value (int): Value of the item.
        """
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self) -> str:
        """
        Return a string representation of the item.

        Returns:
            str: The item's name, weight, and value.
        """
        return (
            f"Item(name={self.name!r}, "
            f"weight={self.weight}, "
            f"value={self.value})"
        )