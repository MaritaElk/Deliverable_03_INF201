from character import Character

class Warrior(Character):
    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        armor: int = 5
    ) -> None:
        super().__init__(name, hp_max, damage)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        reduced_damage = max(damage - self.armor, 0)
        super().take_damage(reduced_damage)
