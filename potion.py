from item import Item


class Potion(Item):
    """Represent a potion that provides mana or healing."""

    def __init__(
        self,
        name: str,
        effect: str,
        potency: int
    ):
        """
        Initialize a potion.

        Args:
            name (str): Name of the potion.
            effect (str): Type of effect, such as mana or healing.
            potency (int): Strength of the potion's effect.
        """
        
        # Validate potion potency
        if type(potency) is not int or potency <= 0:
            raise ValueError("Potion potency must be a positive integer.")
        
        super().__init__(name)

        self.effect = effect
        self.potency = potency

        # Track whether the potion has been used
        self.used = False

    def __repr__(self) -> str:
        """
        Return a string representation of the potion.

        Returns:
            str: The potion's name, effect, and potency.
        """
        return (
            f"Potion(name={self.name!r}, "
            f"effect={self.effect!r}, "
            f"potency={self.potency})"
        )

    def apply_mana_bonus(self, character) -> None:
        """
        Apply a mana bonus to a character once.

        Args:
            character: Character receiving the mana bonus.

        Raises:
            ValueError: If the potion does not provide mana
                        or has already been used.
        """
        if self.effect != "mana":
            raise ValueError("This potion does not provide mana.")

        if self.used:
            raise ValueError("This potion has already been used.")

        # Increase current and maximum mana
        character.mana += self.potency
        character.mana_max += self.potency

        # Mark the potion as used
        self.used = True

    def apply_healing(self, character) -> None:
        """
        Restore a character's health once.

        Args:
            character: Character receiving the healing.

        Raises:
            ValueError: If the potion does not provide healing
                        or has already been used.
        """
        if self.effect != "healing":
            raise ValueError("This potion does not provide healing.")

        if self.used:
            raise ValueError("This potion has already been used.")

        # Restore health without exceeding maximum health
        character.health = min(
            character.health + self.potency,
            character.health_max
        )

        # Mark the potion as used
        self.used = True