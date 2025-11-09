from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def shopUnlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "(|@FNaS 1:5|) OR (|Mario| AND |Withered Mario| AND |Phantom Mario| AND |Nightmare Mario| AND |Luiginette|) OR (|Yoshi| AND |Tails| AND |Withered Yoshi| AND |Phantom Yoshi| AND |Nightmare Yoshi| AND |Nightmare Tails|) OR (|Tails| AND |Withered Tails| AND |Phantom Tails| AND |Nightmare Tails|) OR (|@FNaS 2:11|) OR (|Mario| AND |Toy Mario| AND |Luiginette| AND |Withered Mario| AND |Withered Toy Mario| AND |Phantom Mario| AND |Phantom Luiginette| AND |Nightmare Mario|) OR (|Yoshi| AND |Tails| AND |Toy Yoshi| AND |Withered Yoshi| AND |Withered Toy Yoshi| AND |Phantom Yoshi| AND |Nightmare Yoshi| AND |Nightmare Tails|) OR (|Tails| AND |Taingle| AND |Withered Tails| AND |Phantom Tails| AND |Phantom Taingle| AND |Nightmare Tails|) OR (|'15 Golden Sonic| AND |Balloon Toad| AND |Withered Sonic| AND |Withered Tails| AND |Nightmare Tails|) OR (|Sonic| AND |Mario| AND |Yoshi| AND |Tails| AND |Toy Sonic| AND |Withered Toy Sonic|) OR (|Sonic| AND |Mario| AND |Yoshi| AND |Tails| AND |Toy Mario| AND |Withered Toy Mario|) OR (|Sonic| AND |Mario| AND |Yoshi| AND |Tails| AND |Toy Yoshi| AND |Withered Toy Yoshi|) OR (|Taingle| AND |Withered Sonic| AND |Withered Mario| AND |Withered Yoshi| AND |Withered Tails| AND |Salvage Sonic| AND |Withered Toy Sonic| AND |Withered Toy Mario| AND |Withered Toy Yoshi| AND |The Toymare|) OR (|@FNaS 1:5| AND |@FNaS 2:11| AND |@FNaS 3:11| AND |@FNaS 4:6| AND |@FNaS 5:2|) OR (|@FNaS 3:11|) OR (|Sonic| AND |Toy Sonic| AND |Withered Sonic| AND |Salvage Sonic| AND |Withered Toy Sonic| AND |Nightmare Sonic|) OR (|Mario| AND |Toy Mario| AND |Luiginette| AND |Withered Mario| AND |Withered Toy Mario| AND |Phantom Mario| AND |Nightmare Mario|) OR (|Mario| AND |Yoshi| AND |Withered Mario| AND |Withered Yoshi| AND |Phantom Mario| AND |Phantom Yoshi| AND |Nightmare Mario| AND |Nightmare Yoshi|) OR (|Sonic| AND |Mario| AND |Yoshi| AND |Tails| AND |Toy Sonic| AND |Toy Mario| AND |Toy Yoshi| AND |Salvage Sonic| AND |Withered Toy Sonic| AND |Withered Toy Mario| AND |Withered Toy Yoshi| AND |'27 Golden Sonic|) OR (|Tails| AND |'15 Golden Sonic| AND |Withered Tails| AND |'17 Golden Sonic| AND |Phantom Tails| AND |'27 Golden Sonic| AND |Nightmare Tails| AND |Nightmare Golden Sonic| AND |Origin Sonic| AND |Shadow Sonic|) OR (|Balloon Toad| AND |Withered Tails| AND |Salvage Sonic| AND |Phantom Balloon Toad| AND |Nightmare Tails|) OR (|Taingle| AND |Withered Sonic| AND |Withered Mario| AND |Withered Yoshi| AND |Withered Tails| AND |Salvage Sonic| AND |Withered Toy Sonic| AND |Withered Toy Mario| AND |Withered Toy Yoshi| AND |Phantom Balloon Toad| AND |Phantom Taingle| AND |Nightmare Tails| AND |The Toymare|) OR (|Sonic| AND |Toy Sonic| AND |Withered Sonic| AND |Salvage Sonic| AND |Withered Toy Sonic| AND |Nightmare Sonic| AND |The Toymare| AND |Nightmare Golden Sonic|) OR (|Mario| AND |Toy Mario| AND |Luiginette| AND |Withered Mario| AND |Withered Toy Mario| AND |Phantom Mario| AND |Nightmare Mario| AND |The Toymare|) OR (|Yoshi| AND |Tails| AND |Toy Yoshi| AND |Withered Yoshi| AND |Withered Toy Yoshi| AND |Phantom Yoshi| AND |Nightmare Yoshi| AND |Nightmare Tails| AND |The Toymare|) OR (|Tails| AND |Taingle| AND |Withered Tails| AND |Phantom Tails| AND |Nightmare Tails| AND |The Toymare|) OR (|@FNaS 1:5| AND |Withered Sonic| AND |Withered Mario| AND |Withered Yoshi| AND |Withered Tails| AND |'17 Golden Sonic| AND |Salvage Sonic| AND |Phantom Mario| AND |Phantom Yoshi| AND |Phantom Tails| AND |'27 Golden Sonic| AND |Nightmare Sonic| AND |Nightmare Mario| AND |Nightmare Yoshi| AND |Nightmare Tails| AND |Nightmare Golden Sonic| AND |@FNaS 5:2|)"

def allChallenges(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|@FNaS 1:5| AND |@FNaS 2:11| AND |@FNaS 3:11| AND |@FNaS 4:6| AND |@FNaS 5:2|"
    
def canReachCategory(world: World, multiworld: MultiWorld, state: CollectionState, player: int, category: str, count: str):
    """Can the player reach `count` number of locations with category `category`?"""
    reachable = 0
    for location in multiworld.get_locations(player):
        cats = world.location_name_to_location[location.name].get("category", {})
        if category in cats:
            if state.can_reach_location(location.name, player):
                reachable += 1
    return reachable >= int(count)