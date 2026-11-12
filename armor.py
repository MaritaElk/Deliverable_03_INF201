from items import Item


class Armor(Item):
    """Represent armor that provides defense and damage bonuses."""

    def __init__(
        self,
        name: str,
        defense_bonus: int,
        damage_bonus: int = 0
    ):
        """
        Initialize an armor item.

        Args:
            name (str): Name of the armor.
            defense_bonus (int): Additional defense provided by the armor.
            damage_bonus (int): Additional attack damage. Default is 0.
        """
        super().__init__(name)

        self.defense_bonus = defense_bonus
        self.damage_bonus = damage_bonus

    def __repr__(self) -> str:
        """
        Return a string representation of the armor.

        Returns:
            str: The armor's name, defense bonus, and damage bonus.
        """
        return (
            f"Armor(name={self.name!r}, "
            f"defense_bonus={self.defense_bonus}, "
            f"damage_bonus={self.damage_bonus})"
        )