#text adventure
import random

inv = {
    'consumables': {
        'medkit':1
    },
    'equipment' : {
        'letter':{
            'type': 'quest item',
        },
        'rebar spear': {
            'type': 'weapon',
            'durability': 50,
            'max durability':100,
            'damage' : 10,
      },
    },
    'equipped': {
        'weapon': 'rebar spear'
    }
}

