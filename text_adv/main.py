# courier text adventure
import random

# Character state dictionary (provided by you)
character = {
    "name": "playername",  # You can change this to the player's input name
    "stats": {
        "health": 100,
        "stamina": 75,
        "strength": 10
    },
    "inventory": {
        "consumables": {
            "medkit": 1
        },
        "equipment": {
            "letter": {
                "type": "quest item"
            },
            "rebar spear": {
                "type": "weapon",
                "durability": 50,
                "max durability": 100,
                "damage": 10
            }
        },
        "equipped": {
            "weapon": "rebar spear",
            "item": "medkit"
        }
    }
}


def display_inventory(player):
    """
    Displays the player's inventory, including consumables, equipment, and equipped items.
    """
    inv = player.get("inventory", {})

    print("\n-- Inventory --")

    # Equipped
    equipped = inv.get("equipped", {})
    print("Equipped:")
    for slot, item in equipped.items():
        print(f"  {slot.title()}: {item}")

    # Consumables
    consumables = inv.get("consumables", {})
    print("\nConsumables:")
    if consumables:
        for item, count in consumables.items():
            print(f"  {item} (x{count})")
    else:
        print("  None")

    # Equipment
    equipment = inv.get("equipment", {})
    print("\nEquipment:")
    if equipment:
        for item_name, attributes in equipment.items():
            print(f"  {item_name.title()}:")
            for attr, value in attributes.items():
                print(f"    {attr.title()}: {value}")
    else:
        print("  None")


def starting_area(player):
    """
    Handles the interaction in the starting area.

    Args:
        player (dict): The full character dictionary.

    Returns:
        str: The direction the player chooses to move.
    """
    print("\nYou awaken in a quiet clearing surrounded by thick forest.")
    print("The only visible path leads to the north.\n")

    while True:
        user_input = input("> ").strip().lower()

        if user_input in ["go north", "north", "n"]:
            print("\nYou push through the foliage and head north, deeper into the unknown...")
            return "north"

        elif user_input in ["character", "stats", "inventory"]:
            print("\n-- Character Info --")
            print(f"Name: {player.get('name', 'Unknown')}")
            print("Stats:")
            for stat, value in player.get("stats", {}).items():
                print(f"  {stat.title()}: {value}")
            display_inventory(player)

        elif user_input in ["look", "look around"]:
            print("\nYou are in a grassy clearing. The air smells of moss and bark.")
            print("The forest presses in from all sides, except for a narrow trail to the north.")

        else:
            print("\nYou can't do that here. Try going 'north' or type 'character' to check your stats and gear.")
