
"""Base character for the RPG battle simulator."""

from items import Weapon


class Character:
    """Represent a character with HP and an optional weapon."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, damage: int, ignore_armor: bool = False) -> None:
        """Reduce this character's HP, without going below zero."""
        self._hp = max(self._hp - max(damage, 0), 0)

    def heal(self, amount: int) -> None:
        """Restore HP, without exceeding the character's maximum."""
        self._hp = min(self._hp + max(amount, 0), self.hp_max)

    def attack(self, target) -> None:
        """Attack with base damage, or with the equipped weapon."""
        if self.weapon is None:
            target.take_damage(self.damage)
            return

        weapon = self.weapon

        # Axe: chance to miss the attack
        if weapon.special_effect == "miss" and weapon.activate_special():
            print(f"{self.name} misses with {weapon.name}!")
            return

        damage = weapon.roll_damage()

        # Sword: chance to ignore armor
        ignore_armor = (
            weapon.special_effect == "ignore_armor"
            and weapon.activate_special()
        )

        target.take_damage(damage, ignore_armor=ignore_armor)

        if ignore_armor:
            print(f"{self.name}'s {weapon.name} ignores armor!")

        # Dagger: chance to attack a second time
        if (
            weapon.special_effect == "extra_attack"
            and target.is_alive
            and weapon.activate_special()
        ):
            target.take_damage(weapon.roll_damage())
            print(f"{self.name} makes an extra attack with {weapon.name}!")

    def introduce(self) -> None:
        """Introduce the character."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Return current HP (read-only)."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Return whether the character has HP remaining."""
        return self._hp > 0

