
"""Items used by the RPG characters."""

import random
from dice import Dice


class Item:
    """Represent a general item in the game."""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Item(name={self.name!r})"


class Weapon(Item):
    """Represent a dice-based weapon with an optional special effect."""

    def __init__(
        self,
        name: str,
        damage_dice: Dice,
        damage_bonus: int = 0,
        min_damage: int = 0,
        special_effect: str | None = None,
        special_chance: float = 0.0,
    ):
        super().__init__(name)
        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus
        self.min_damage = min_damage
        self.special_effect = special_effect
        self.special_chance = special_chance

    def roll_damage(self) -> int:
        """Roll damage, respecting the configured minimum."""
        return max(self.damage_dice.roll() + self.damage_bonus, self.min_damage)

    def activate_special(self) -> bool:
        """Return whether the special effect triggers this attack."""
        return random.random() < self.special_chance

    def __repr__(self) -> str:
        return (
            f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r}, "
            f"damage_bonus={self.damage_bonus}, min_damage={self.min_damage}, "
            f"special_effect={self.special_effect!r}, "
            f"special_chance={self.special_chance})"
        )


class Armor(Item):
    """Represent armor that provides defense and damage bonuses."""

    def __init__(self, name: str, defense_bonus: int, damage_bonus: int = 0):
        super().__init__(name)
        self.defense_bonus = defense_bonus
        self.damage_bonus = damage_bonus

    def __repr__(self) -> str:
        return (
            f"Armor(name={self.name!r}, defense_bonus={self.defense_bonus}, "
            f"damage_bonus={self.damage_bonus})"
        )


class ArcheryWeapon(Weapon):
    """Represent an archery weapon with a hit chance."""

    def __init__(
        self,
        name: str,
        damage_dice: Dice,
        hit_threshold: int,
        damage_bonus: int = 0,
    ):
        super().__init__(name, damage_dice, damage_bonus)
        self.hit_threshold = hit_threshold
        self.hit_dice = Dice(sides=20)

    def roll_hit(self) -> bool:
        """Return whether the D20 roll meets the hit threshold."""
        return self.hit_dice.roll() >= self.hit_threshold

    def __repr__(self) -> str:
        return (
            f"ArcheryWeapon(name={self.name!r}, "
            f"damage_dice={self.damage_dice!r}, "
            f"hit_threshold={self.hit_threshold}, "
            f"damage_bonus={self.damage_bonus})"
        )


class Potion(Item):
    """Represent a single-use mana or healing potion."""

    def __init__(self, name: str, effect: str, potency: int):
        if type(potency) is not int or potency <= 0:
            raise ValueError("Potion potency must be a positive integer.")

        super().__init__(name)
        self.effect = effect
        self.potency = potency
        self.used = False

    def __repr__(self) -> str:
        return (
            f"Potion(name={self.name!r}, effect={self.effect!r}, "
            f"potency={self.potency})"
        )

    def apply_mana_bonus(self, character) -> None:
        """Increase the mage's current and maximum mana once."""
        if self.effect != "mana":
            raise ValueError("This potion does not provide mana.")
        if self.used:
            raise ValueError("This potion has already been used.")

        character.mana += self.potency
        character.mana_max += self.potency
        self.used = True

    def apply_healing(self, character) -> None:
        """Restore HP through Character.heal once."""
        if self.effect != "healing":
            raise ValueError("This potion does not provide healing.")
        if self.used:
            raise ValueError("This potion has already been used.")

        character.heal(self.potency)
        self.used = True
