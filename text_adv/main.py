# courier text adventure
import random

# Character state dictionary
character = {
    "name": "playername",  # This will be replaced with the player's input
    "stats": {
        "health": 100,
        "stamina": 75,
        "strength": 10
    },
    "inventory": {
        "consumables": {
            "medkit": 1,
            'caps' : 10
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

destinations = [
    "Ironfall",
    "Mistwood",
    "Grayhaven",
    "Stonebridge",
    "Emberfield"
]

# Dictionary of commands and their descriptions
available_commands = {
    'help': 'show this help message',
    'look': 'inspect your surroundings',
    'inventory': 'open your inventory',
    'use': 'use an item (like a medkit)',
    'go': '(needs to be paired with a direction e.g., "north")',
    'save': 'save the game',
    'quit': 'exit the game',
}


def show_help():
    """
    Prints the list of available commands and what each does.
    """
    print('\nAvailable commands:')
    for command, description in available_commands.items():
        print(f'- {command:<10} -- {description}')


def display_inventory(player):
    """
    Displays the player's inventory, including consumables, equipment, and equipped items.

    Args:
        player (dict): The character dictionary containing inventory data.
    """
    inv = player.get("inventory", {})

    print("\n-- Inventory --")

    # Equipped items
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

def freeson(player):
    """
    Placeholder for Freeson — the main town hub where players can shop and take missions.

    Args:
        player (dict): The full character dictionary.

    Returns:
        str: The next location or action (currently ends the game).
    """
    freeson_commands = {}

    print("\n[Placeholder] You have arrived in Freeson.")
    print("You see a post office, a general store, and the town square with few people milling about.")
    if user_input in ['help', 'h']:
            show_help()
            for key,value in freeson_commands.items():
                print(f'{key} --{value}')

def starting_area(player):
    """
    Handles the interaction in the starting area and accepts player input.

    Args:
        player (dict): The full character dictionary.

    Returns:
        str: The direction the player chooses to move (e.g., 'north').
    """
    print('It seems your only option is to go *NORTH* to Freeson.')

    while True:
        user_input = input("> ").strip().lower()

        if user_input in ["go north", "north", "n"]:
            print("\nYou make your way down the road to the north, Freeson becoming larger in the distance.")
            return "north"  # Tell game_loop to update location

        elif user_input in ["character", "stats", "inventory"]:
            print("\n-- Character Info --")
            print(f"Name: {player.get('name', 'Nameless Courier')}")
            print("Stats:")
            for stat, value in player.get("stats", {}).items():
                print(f"  {stat.title()}: {value}")
            display_inventory(player)

        elif user_input in ["look", "look around"]:
            print("\nYou are in a grassy clearing. The air smells of moss and bark.")
            print("The forest presses in from all sides, except for a narrow trail to the north.")

        elif user_input in ['help', 'h']:
            show_help()

        elif user_input in ['quit', 'exit']:
            print("\nYou sit back down in the cabin and decide not to continue today.")
            exit()

        else:
            print("\nYou can't do that here. Try going 'north' or type 'character' to check your stats and gear.")




def game_loop(player):
    """
    Main game loop that controls flow between different areas or game scenes.

    Args:
        player (dict): The full character dictionary.
    """
    current_location = "starting_area"

    while True:
        if current_location == "starting_area":
            next_location = starting_area(player)
            if next_location == "north":
                current_location = "freeson"

        elif current_location == "freeson":
            next_location = freeson(player)
            if next_location == "end":
                print("\nThank you for playing. More content coming soon!")
                break

        else:
            print(f"\nError: Unknown location '{current_location}'. Exiting game.")
            break


if __name__ == '__main__':
    # Ask for the player's name
    character['name'] = input('What is your name?: ')

    # Introductory narrative
    print("\nYou wake up in a small cabin.")
    print("You rested here last night on your way to Freeson, a nearby town, to the *NORTH*.")
    print("What would you like to do?")

    # Start the game loop
    game_loop(character)
