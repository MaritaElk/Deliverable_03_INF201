
"""Interactive RPG battle simulator."""

from character import Character
from warrior import Warrior
from mage import Mage
from dice import Dice
from items import Weapon
from battle import Battle


def choose_game_mode() -> str:
    """Let the user select a game mode."""

    game_modes = {
        "0": "exit",
        "1": "player_vs_computer",
        "2": "computer_vs_computer",
        "3": "player_vs_player"
    }

    print("\n========== GAME MODE ==========")
    print("1. Player vs Computer")
    print("2. Computer vs Computer")
    print("3. Player vs Player")
    print("0. Exit Game")

    while True:
        choice = input(
            "\nChoose game mode (0-3): "
        ).strip()

        if choice in game_modes:
            return game_modes[choice]

        print("Invalid choice. Please enter 0, 1, 2, or 3.")


def choose_character(role: str) -> Character:
    """Create a character of the selected class."""

    character_classes = {
        "1": Warrior,
        "2": Mage
    }

    print(
        f"\n========== {role.upper()} SELECTION =========="
    )

    print("1. Warrior")
    print("2. Mage")

    while True:
        choice = input(
            "\nChoose character class (1-2): "
        ).strip()

        if choice in character_classes:
            break

        print("Invalid choice. Please enter 1 or 2.")

    while True:
        name = input(
            f"Enter {role} name: "
        ).strip()

        if name:
            break

        print("Character name cannot be empty.")

    return character_classes[choice](name)


def choose_weapon(character: Character) -> None:
    """Create and equip a weapon for the character."""

    weapons = {
        "1": ("Dagger", 4, 10, 11, "extra_attack", 0.30),
        "2": ("Sword", 8, 10, 15, "ignore_armor", 0.20),
        "3": ("Axe", 12, 10, 19, "miss", 0.25)
    }

    print(
        f"\n========== WEAPON SELECTION: "
        f"{character.name} =========="
    )

    print("0. No weapon (10 base damage)")
    print("1. Dagger (11-14 damage, 30% extra attack)")
    print("2. Sword (15-18 damage, 20% ignore armor)")
    print("3. Axe (19-22 damage, 25% miss chance)")

    while True:
        choice = input(
            "\nChoose weapon (0-3): "
        ).strip()

        if choice == "0":
            character.weapon = None
            print(
                f"{character.name} will fight without a weapon."
            )
            return

        if choice in weapons:
            break

        print("Invalid choice. Please enter 0, 1, 2, or 3.")

    (
        weapon_name,
        dice_sides,
        damage_bonus,
        min_damage,
        special_effect,
        special_chance
    ) = weapons[choice]

    character.weapon = Weapon(
        name=weapon_name,
        damage_dice=Dice(dice_sides),
        damage_bonus=damage_bonus,
        min_damage=min_damage,
        special_effect=special_effect,
        special_chance=special_chance
    )

    print(
        f"{character.name} equipped {character.weapon.name}."
    )


def choose_attack(character: Character) -> bool | None:
    """Choose magic, a regular attack, or exit the battle."""

    print(f"HP: {character.hp}/{character.hp_max}")

    if isinstance(character, Mage):
        print(
            f"Mana: {character.mana}/{character.mana_max}"
        )

        if character.mana < 10:
            print("1. Regular attack (+5 mana)")
            print("0. Exit Battle")

            while True:
                choice = input(
                    "\nChoose action (0-1): "
                ).strip()

                if choice == "0":
                    return None

                if choice == "1":
                    return False

                print("Invalid choice. Please enter 0 or 1.")

        print("1. Magic attack (10 mana, double base damage)")
        print("2. Regular attack (+5 mana)")
        print("0. Exit Battle")

        while True:
            choice = input(
                "\nChoose action (0-2): "
            ).strip()

            if choice == "0":
                return None

            if choice == "1":
                return True

            if choice == "2":
                return False

            print("Invalid choice. Please enter 0, 1, or 2.")

    print("1. Regular attack")
    print("0. Exit Battle")

    while True:
        choice = input(
            "\nChoose action (0-1): "
        ).strip()

        if choice == "0":
            return None

        if choice == "1":
            return False

        print("Invalid choice. Please enter 0 or 1.")


def run_battle(battle: Battle, game_mode: str) -> None:
    """Connect player choices to the battle manager."""

    print("\n========== BATTLE START ==========")
    print(f"{battle.hero.name} vs {battle.enemy.name}")

    if game_mode == "computer_vs_computer":
        battle.simulate_battle()

    elif game_mode == "player_vs_computer":
        battle.simulate_battle(
            choose_hero=choose_attack
        )

    else:
        battle.simulate_battle(
            choose_hero=choose_attack,
            choose_enemy=choose_attack
        )


def start_game() -> bool:
    """Set up characters and their weapons before a battle."""

    print("\n========== GAME SETUP ==========")

    game_mode = choose_game_mode()

    if game_mode == "exit":
        return False

    # Hero setup
    hero = choose_character("Hero")
    choose_weapon(hero)

    # Enemy setup
    enemy = choose_character("Enemy")
    choose_weapon(enemy)

    # Create the battle
    battle = Battle(
        hero=hero,
        enemy=enemy
    )

    print("\n========== GAME READY ==========")
    print(f"Game mode: {game_mode}")
    print(f"Hero: {hero.name}")
    print(f"Enemy: {enemy.name}")

    run_battle(battle, game_mode)

    return True


def main() -> None:
    """Run the game and allow repeated battles."""

    while True:
        if not start_game():
            break

        while True:
            play_again = input(
                "\nPlay again? (y/n): "
            ).strip().lower()

            if play_again in ("y", "n"):
                break

            print("Invalid choice. Please enter y or n.")

        if play_again == "n":
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
