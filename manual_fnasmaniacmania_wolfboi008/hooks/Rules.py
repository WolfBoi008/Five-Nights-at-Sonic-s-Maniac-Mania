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
    return "|@Sonic's 1:ALL| OR |@Bunny Hop:ALL| OR |@Yoshi's Island:ALL| OR |@Critter Lab:ALL| OR |@Abandoned Sonic's 1:ALL| OR |@Sonic's 2:ALL| OR |@Plumber Trouble:ALL| OR |@Double Dinos:ALL| OR |@Taingled Foxes:ALL| OR |@Light Fright:ALL| OR |@Bounce Blade:ALL| OR |@Burning Blitz:ALL| OR |@Splash Shooter:ALL| OR |@Winding Away:ALL| OR |@Abandoned Sonic's 2:ALL| OR |@Sonic's 3:ALL| OR |@Hectic Hedgehogs:ALL| OR |@Pipework Plaza:ALL| OR |@Ground Pound:ALL| OR |@Storage Struck:ALL| OR |@Failed Experiment:ALL| OR |@Toad Rally:ALL| OR |@Torn Apart:ALL| OR |@Burned to Ashes:ALL| OR |@Speedy Surroundings:ALL| OR |@Mario Mayhem:ALL| OR |@Dinosaur Dread:ALL| OR |@Two-Tailed Trails:ALL| OR |@Chaos Challenge:ALL| OR |@'90s Diner:ALL|"

def allChallenges(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|@FNaS 1:5| AND |@FNaS 2:11| AND |@FNaS 3:11| AND |@FNaS 4:6| AND |@FNaS 5:2|"