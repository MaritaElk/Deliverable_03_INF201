
"""Warrior specialization."""

from character import Character
from items import Weapon


class Warrior(Character):
    """Defensive character with damage-reducing armor."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        armor: int = 5,
        weapon: Weapon | None = None,
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, damage: int, ignore_armor: bool = False) -> None:
        """Reduce incoming damage by armor unless it is ignored."""
        reduced_damage = damage if ignore_armor else max(damage - self.armor, 0)
        super().take_damage(reduced_damage)
