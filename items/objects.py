# for now each object will be called as object_<object> in the room["objects"] list.
# object "id" is how each object will be called when inspected or scanned - they cannot be taken
# description_scan works the same way as with items - check items.py for more
# state is currently not implemented with objects, only rooms and their descriptions/exits

object_ceiling = {
    "id": "ceiling",

    "description": "This is keeping the structure safe from the outside climate."
                   "\nI cannot imagine what would happen if it collapsed on me!",

    "description_scan": "This object is very unstable - it could prove harmful!",

    "state": 0
}