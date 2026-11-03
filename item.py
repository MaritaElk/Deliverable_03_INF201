class Item:
    """Represent a general item in the game."""

    def __init__(self, name: str):
        """
        Initialize an item.

        Args:
            name (str): Name of the item.
        """
        self.name = name

    def __repr__(self) -> str:
        """
        Return a string representation of the item.

        Returns:
            str: The item representation including its name.
        """
        return f"Item(name={self.name!r})"