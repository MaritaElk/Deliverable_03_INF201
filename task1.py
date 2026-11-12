# Object-oriented game simulator

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, damage: int) -> None:
        """Reduce character HP when taking damage."""
        self._hp = max(self._hp - damage, 0)

    def heal(self, amount: int) -> None:
        """Restore HP without exceeding max HP."""
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target) -> None:
        """Attack and deal damage to target character."""
        target.take_damage(self.damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Check if character is alive."""
        return self._hp > 0
