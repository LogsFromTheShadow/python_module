from ex0.Creaturecard import Creature_card

if __name__ == "__main__":
    fire_dragon = Creature_card("Fire_dragon", 5, "Legendary", "Creature", 7, 5)
    target = "Goblin Warrior"

    print("=== DataDeck Card Foundation ===")

    print()

    print("CreatureCard Info:")
    dragon_state = fire_dragon.play(game_state={})
    print(dragon_state)

    print()

    print(f"Playing {fire_dragon.name} with 6 mana available:")
    sufficient_mana = fire_dragon.is_playable(6)
    print(f"Playable: {sufficient_mana}")
    
    attack_turn = {"card_played": fire_dragon.name,
                   "mane_used": fire_dragon.cost,
                   "effect": "creature summon to battlefield"}
    print(f"Play result: {attack_turn}")

    print()

    fire_dragon.attack_target(target)

    print("Testing insufficient mana (3 available):")
    spell = fire_dragon.is_playable(3)
    print(f"Playable: {spell}")

    print()

    print("Abstract pattern successfully demonstrated!")
