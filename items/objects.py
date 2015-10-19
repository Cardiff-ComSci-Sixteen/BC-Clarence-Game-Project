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

    "description": "This fighter is odd in it's design, as it appears its wings open to form an 'x' shape.\n"
    "I could probably scan this to see if it works",

    "description_scan": "This fighter appears to be functional I could use it to escape"
}

object_damagedfighters = {
    "id": ["damagedfighters"],

    "description": "These fighters have seen better days"
}

object_oddfighters = {
    "id": ["oddfighters"],

    "description": "These fighters are shaped like a 'H' for some reason maybe I could scan them to see if they work.",

    "description_scan": "None of them seem to be functional"
}

object_emptyvodka = {
    "id": ["emptyvodka"],

    "description": "This bottle of vodka is empty, I wonder why."
}

object_bunks = {
    "id": ["bunks"],

    "description": "These don't look very comfortable"
}

object_mainreactor = {
    "id": ["mainreactor"],

    "description": "This large reactor powers this ship, I could probably scan it.",

    "description_scan": "It is a nuclear reactor, better not get to close."
}