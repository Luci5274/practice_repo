# courier text adventure
import random

# --- Character state dictionary ---
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
            "caps": 10
        },
        "equipment": {
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

# --- List of world destinations (excluding Freeson) ---
destinations = [
    "Ironfall",
    "Mistwood",
    "Grayhaven",
    "Stonebridge",
    "Emberfield"
]

# --- Dictionary of available global commands ---
available_commands = {
    'help': 'show this help message',
    'look': 'inspect your surroundings',
    'inventory': 'open your inventory',
    'use': 'use an item (like a medkit)',
    'go': '(needs to be paired with a direction e.g., "north")',
    'save': 'save the game',
    'quit': 'exit the game',
    'attack': 'strike with your equipped weapon'
}

def show_help():
    """Prints the list of available commands and their descriptions."""
    print('\nAvailable commands:')
    for command, description in available_commands.items():
        print(f'- {command:<10} -- {description}')

def display_inventory(player):
    """Displays the player's inventory, including consumables, equipment, and equipped items."""
    inv = player.get("inventory", {})

    print("\n-- Inventory --")
    print("Equipped:")
    for slot, item in inv.get("equipped", {}).items():
        print(f"  {slot.title()}: {item}")

    print("\nConsumables:")
    for item, count in inv.get("consumables", {}).items():
        print(f"  {item} (x{count})")

    print("\nEquipment:")
    for item_name, attributes in inv.get("equipment", {}).items():
        print(f"  {item_name.title()}:")
        for attr, value in attributes.items():
            print(f"    {attr.title()}: {value}")

def attack(player):
    """
    Calculates and displays the attack damage based on the player's stamina,
    weapon damage, and weapon durability.

    Formula: stamina * (damage * 10 / durability)
    """
    try:
        equipped_weapon_name = player["inventory"]["equipped"]["weapon"]
        weapon = player["inventory"]["equipment"][equipped_weapon_name]
        damage = weapon["damage"]
        durability = weapon["durability"]
        stamina = player["stats"]["stamina"]

        if durability == 0:
            print(f"\nYour {equipped_weapon_name} is broken! It can't be used.")
            return

        attack_value = stamina * ((damage * 10) / durability)
        print(f"\nYou strike with your {equipped_weapon_name}!")
        print(f"Damage dealt: {round(attack_value, 2)}")

    except KeyError as e:
        print(f"\nAttack failed: missing data - {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

def handle_global_command(command, player):
    """
    Checks and executes any recognized global command.
    Returns True if the command was handled, False otherwise.
    """
    if command in ["help", "h"]:
        show_help()
    elif command in ["inventory", "character", "stats"]:
        display_inventory(player)
    elif command == "attack":
        attack(player)
    elif command in ["quit", "exit"]:
        print("\nYou sit back down in the cabin and decide not to continue today.")
        exit()
    else:
        return False
    return True

def freeson(player):
    """
    Placeholder for Freeson — the main town hub where players can shop and take missions.
    """
    PO_inv = {}
    freeson_commands = {
        "general store": "buy and sell items",
        "post office": "pick up or turn in deliveries"
    }

    print("\n[Placeholder] You have arrived in Freeson.")
    print("You see a post office, a general store, and the town square with a few people milling about.")

    while True:
        user_input = input("> ").strip().lower()

        if handle_global_command(user_input, player):
            continue

        if user_input in ['post office', 'post', 'go to post office', 'go to post', 'p o']:
            print(f'Hello, {character["name"]}')

        elif user_input == "leave":
            return "starting_area"

        else:
            print("\nYou can look around, visit places, or type 'help' for available options.")

def starting_area(player):
    """Handles the interaction in the starting area and accepts player input."""
    print('It seems your only option is to go *NORTH* to Freeson.')

    while True:
        user_input = input("> ").strip().lower()

        if handle_global_command(user_input, player):
            continue

        if user_input in ["go north", "north", "n"]:
            print("\nYou make your way down the road to the north, Freeson becoming larger in the distance.")
            return "freeson"

        else:
            print("\nYou can't do that here. Try going 'north' or type 'character' to check your stats and gear.")

def game_loop(player):
    """Main game loop that controls flow between different areas or game scenes."""
    locations = {
        "starting_area": starting_area,
        "freeson": freeson
    }

    current_location = "starting_area"

    while True:
        location_func = locations.get(current_location)

        if not location_func:
            print(f"\nError: Unknown location '{current_location}'. Exiting game.")
            break

        next_location = location_func(player)

        if next_location == "end":
            print("\nThank you for playing. More content coming soon!")
            break

        current_location = next_location

if __name__ == '__main__':
    # Ask for the player's name
    character['name'] = input('What is your name?: ')

    # Introductory narrative
    print("\nYou wake up in a small cabin.")
    print("You rested here last night on your way to Freeson, a nearby town, to the *NORTH*.")
    print("What would you like to do?")

    # Start the game loop
    game_loop(character)
