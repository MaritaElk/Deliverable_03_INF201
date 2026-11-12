
"""Manage turn-based battles between two characters."""

from collections.abc import Callable

from character import Character
from mage import Mage


class Battle:
    """Manage attacks and rounds until a character loses or the battle ends."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy
        self.round_number = 0
        self.exited = False

    def perform_attack(
        self,
        attacker: Character,
        defender: Character,
        choose_attack: Callable[[Character], bool | None] | None = None
    ) -> bool:
        """Perform one turn. Return False if a player exits the battle."""

        print(f"\n========== {attacker.name.upper()}'S TURN ==========")

        if choose_attack is None:
            use_magic = True
            print(f"{attacker.name} attacks automatically.")
        else:
            use_magic = choose_attack(attacker)

            if use_magic is None:
                self.exited = True
                return False

        hp_before = defender.hp

        if isinstance(attacker, Mage):
            magic_attack = use_magic and attacker.mana >= 10

            attacker.attack(defender, use_magic=use_magic)

            print(
                f"Attack type: {'Magic' if magic_attack else 'Regular'}"
            )
            print(
                f"Mana remaining: {attacker.mana}/{attacker.mana_max}"
            )
        else:
            attacker.attack(defender)

        print(f"Damage dealt: {hp_before - defender.hp}")
        print(
            f"{defender.name} HP: {defender.hp}/{defender.hp_max}"
        )

        return True

    def play_round(
        self,
        choose_hero: Callable[[Character], bool | None] | None = None,
        choose_enemy: Callable[[Character], bool | None] | None = None
    ) -> bool:
        """Let hero attack, then enemy if alive. Return False if exited."""

        if not (self.hero.is_alive and self.enemy.is_alive) or self.exited:
            return False

        self.round_number += 1

        print(
            f"\n========== ROUND {self.round_number} =========="
        )

        # Hero attacks first
        if not self.perform_attack(
            self.hero,
            self.enemy,
            choose_hero
        ):
            return False

        # Enemy attacks only if still alive
        if self.enemy.is_alive:
            if not self.perform_attack(
                self.enemy,
                self.hero,
                choose_enemy
            ):
                return False

        print("\n========== ROUND STATUS ==========")
        print(
            f"{self.hero.name}: "
            f"{self.hero.hp}/{self.hero.hp_max} HP"
        )
        print(
            f"{self.enemy.name}: "
            f"{self.enemy.hp}/{self.enemy.hp_max} HP"
        )

        return True

    def simulate_battle(
        self,
        choose_hero: Callable[[Character], bool | None] | None = None,
        choose_enemy: Callable[[Character], bool | None] | None = None
    ) -> Character | None:
        """Run rounds to completion or until a player exits."""

        while (
            self.hero.is_alive
            and self.enemy.is_alive
            and not self.exited
        ):
            self.play_round(choose_hero, choose_enemy)

        if self.exited:
            print("\n========== BATTLE EXITED ==========")
            print("The battle ended without a winner.")
            return None

        winner = (
            self.hero if self.hero.is_alive else self.enemy
        )

        print("\n========== BATTLE FINISHED ==========")
        print(f"Winner: {winner.name}")
        print(f"Rounds played: {self.round_number}")

        return winner
