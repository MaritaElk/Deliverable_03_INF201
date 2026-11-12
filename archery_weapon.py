from weapon import Weapon
from dice import Dice


class ArcheryWeapon(Weapon):
    """Represent an archery weapon with a hit chance."""

    def __init__(
        self,
        name: str,
        damage_dice: Dice,
        hit_threshold: int,
        damage_bonus: int = 0
    ):
        """
        Initialize an archery weapon.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice used to determine damage.
            hit_threshold (int): Minimum D20 roll required to hit.
            damage_bonus (int): Additional damage added to the dice roll.
                                Default is 0.
        """
        super().__init__(name, damage_dice, damage_bonus)

        self.hit_threshold = hit_threshold
        self.hit_dice = Dice(sides=20)

    def roll_hit(self) -> bool:
        """
        Roll the hit dice to determine if the attack hits.

        Returns:
            bool: True if the roll meets the hit threshold,
                  otherwise False.
        """
        # Roll the D20 and compare with the hit threshold
        return self.hit_dice.roll() >= self.hit_threshold

    def __repr__(self) -> str:
        """
        Return a string representation of the archery weapon.

        Returns:
            str: The weapon's name, damage dice, hit threshold,
                 and damage bonus.
        """
        return (
            f"ArcheryWeapon(name={self.name!r}, "
            f"damage_dice={self.damage_dice!r}, "
            f"hit_threshold={self.hit_threshold}, "
            f"damage_bonus={self.damage_bonus})"
        )