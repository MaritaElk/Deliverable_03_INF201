from character import Character


class Mage(Character):
    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        mana_max: int = 30
    ) -> None:
        super().__init__(name, hp_max, damage)
        self.mana_max = mana_max
        self.mana = mana_max

    def attack(self, target) -> None:
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)
