from items import Item
from dice import Dice


class Weapon(Item):
    """Represent a weapon that uses dice to determine damage."""

    def __init__(
        self,
        name: str,
        damage_dice: Dice,
        damage_bonus: int = 0
    ):
        """
        Initialize a weapon.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice used to calculate weapon damage.
            damage_bonus (int): Additional damage added to the dice roll.
                                Default is 0.
        """
        super().__init__(name)

        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus

    def roll_damage(self) -> int:
        """
        Roll the weapon's damage dice and add the damage bonus.

        Returns:
            int: Total damage from the dice roll and damage bonus.
        """
        # Calculate total damage using dice and bonus
        return self.damage_dice.roll() + self.damage_bonus

    def __repr__(self) -> str:
        """
        Return a string representation of the weapon.

        Returns:
            str: The weapon's name, damage dice, and damage bonus.
        """
        return (
            f"Weapon(name={self.name!r}, "
            f"damage_dice={self.damage_dice!r}, "
            f"damage_bonus={self.damage_bonus})"
        )