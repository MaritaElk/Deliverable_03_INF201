from item import Item
from dice import Dice


class Weapon(Item):
    """Represent a weapon that uses dice to determine damage."""

    def __init__(self, name: str, damage_dice: Dice):
        """
        Initialize a weapon.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice used to calculate weapon damage.
        """
        super().__init__(name)

        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """
        Roll the weapon's damage dice.

        Returns:
            int: The damage determined by the dice roll.
        """
        # Use the weapon's dice to calculate damage
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """
        Return a string representation of the weapon.

        Returns:
            str: The weapon's name and damage dice.
        """
        return (
            f"Weapon(name={self.name!r}, "
            f"damage_dice={self.damage_dice!r})"
        )