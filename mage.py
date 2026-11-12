
"""Mage specialization."""

from character import Character
from items import Weapon


class Mage(Character):
    """Character that can choose between magic and regular attacks."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        mana_max: int = 30,
        weapon: Weapon | None = None,
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.mana_max = mana_max
        self.mana = mana_max

    def attack(self, target, use_magic: bool = True) -> None:
        """Use magic if selected and affordable; otherwise regain 5 mana."""
        if use_magic and self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)
