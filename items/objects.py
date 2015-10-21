# for now each object will be called as object_<object> in the room["objects"] list.
# object "id" is how each object will be called when inspected or scanned - they cannot be taken
# description_scan works the same way as with items - check items.py for more
# state is currently not implemented with objects, only rooms and their descriptions/exits

object_board_AI = {
    "id": ["board_ai", "boardai", "ai"],

    "name": "Sparrow the Space Lorry's Board AI",

    "description": "The board AI has definitely malfunctioned. The monitors display"
                   "\na lot of strange symbols, probably due to the crash."
                   "\nIt will soon run out of reserve energy as it has its own batteries."

}


object_ceiling = {
    "id": ["ceiling"],

    "name": "Ceiling",

    "description": "This is keeping the structure safe from the outside climate."
                   "\nI cannot imagine what would happen if it collapsed on me!",

    "description_scan": "This object is very unstable - it could prove harmful!"
}

object_wrecked_ship = {
    "id": ["wrecked_ship", "ship", "wreckedship", "wrecked"],

    "name": "Wrecked Sparrow the Space Lorry",

    "description": "My ship is badly damaged I do not think I'll be able to use it to escape."
}

object_xfighter = {
    "id": ["xfighter"],

    "name": "X-Fighter",

    "description": "This fighter is odd in it's design,"
                   "\nas it appears its wings open to form an 'x' shape."
                   "\nI could probably scan this to see if it works",

    "description_scan": "This fighter appears to be functional I could use it to escape"
}

object_damagedfighters = {
    "id": ["damagedfighters"],

    "name": "Damaged Fighters",

    "description": "These fighters have seen better days"
}

object_powerlifter = {
    "id": ["powerlifter"],

    "name": "Power Lifters",

    "description": "There must have been some sort of Power Lifter"
                   "\nfight for these to be in that position"
}

object_oddfighters = {
    "id": ["oddfighters"],

    "name": "Odd shaped fighters",

    "description": "These fighters are shaped like a 'H' for some"
                   "\nreason maybe I could scan them to see if they work.",

    "description_scan": "None of them seem to be functional"
}

object_emptyvodka = {
    "id": ["emptyvodka"],

    "name": "Empty Bottle of vodka",

    "description": "This bottle of vodka is empty, I wonder why."
}

object_bunks = {
    "id": ["bunks"],

    "name": "Bunk Beds",

    "description": "These don't look very comfortable"
}

object_mainreactor = {
    "id": ["mainreactor", "main_reactor"],

    "name": "Main Reactor",

    "description": "This large reactor powers this ship, I could probably scan it.",

    "description_scan": "It is a nuclear reactor, better not get to close."
}

object_powerconsole = {
    "id": ["console", "large_console"],

    "name": "Power Console",

    "description": "Power is distributed using this. Every room has a 'START' and 'STOP' button"
                   "\nto control its power. All 'START' buttons are green besides where"
                   "\nthe generator for Hangar #2 is. Starting the generator may be my"
                   "\nonly chance out of here!"
}

object_warpcore = {
    "id": ["warpcore", "warp_core"],

    "name": "Warp Core",

    "description": "It's the warp core for the ship,"
                   "\nI could probably scan it for more information",

    "description_scan": "It doesn't seem to be operational, it's miss aligned."
}

object_weaponcontrol = {
    "id": ["weaponcontrol"],

    "name": "Weapon Controls",

    "description": "These are the main controls for the weapons,"
                   "\none of these must control the tractor beam",
}

object_bridgecontrols = {
    "id": ["bridgecontrols", "bridge_controls"],

    "name": "Bridge Controls",

    "description": "These look like the consoles that control this entire ship",
}

object_window = {
    "id": ["window"],

    "name": "A window",

    "description": "What an amazing view!",
}

object_lifecontrols = {
    "id": ["lifecontrols", "life_controls"],

    "name": "Life Support Controls",

    "description": "These are the controls for life support better not mess with them",
}
