#courrier text adventure
import random

# This dictionary defines the entire player character's state, including stats, inventory, and equipped items
character = {
    "name": "playername",  # You can change this to the player's input name
    "stats": {
        "health": 100,     # You can adjust this to balance difficulty
        "stamina": 75,     # Controls how many actions they can perform before resting
        "strength": 10     # Could influence melee damage or carrying capacity
    },
    "inventory": {  # The player’s carried items, organized by type
        "consumables": {
            "medkit": 1  # Single-use item; use a function to consume and restore health
        },
        "equipment": {
            "letter": {
                "type": "quest item"  # Non-usable, likely for story triggers
            },
            "rebar spear": {
                "type": "weapon",      # Used to identify how it functions
                "durability": 50,      # Goes down with use
                "max durability": 100, # Used to display or repair
                "damage": 10           # How much damage it deals
            }
        },
        # References the equipped weapon's name from equipment
        "equipped": {
            "weapon": "rebar spear",
            'item' : 'medkit'
        }
    }
}

def display_inv():
    # print(f'inventory: {character["inventory"]["equipment"]}')
    equipment = character['inventory']
    print('inventory equipment')
    for itm_name, itm_stats in equipment.items():
        print(f'-{itm_name}:')
    for attr_key, stats in itm_stats.items():
        print(f'--{attr_key}:{stats}')


display_inv()