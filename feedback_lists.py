from collections import OrderedDict

# List of possible commands that could be used
commands_expanded = {"playername": ["playername, name, changename"]}

commands = OrderedDict([
    ("drop", "drop an item from your inventory"),
    ("exits", "show all available exits"),
    ("go", "enter a new room"),
    ("help", "show a list of available commands ('help detailed' for more info)"),
    ("inventory", "see what you are carrying"),
    ("load", ""),
    ("playername", "change your name"),
    ("quit", "quits the game"),
    ("save", ""),
    ("scan", "analyze an element in a room or an item"),
    ("stats", "view valuable information about your character"),
    ("take", "pick up an item to your inventory")])

commands_detailed = OrderedDict([
    ("drop", "drop an item from your inventory,"
             "\n       alternatively, you can use 'drop everything'"
             "\n       to let go of all items in your inventory"),
    ("exits", "shows all available exits that are in"
              "\n        the room you are currently in"),
    ("go", "go to a new room"),
    ("help", "shows a list of available commands"),
    ("inventory", "you can see a list of all the items"
                  "\n            that you are currently carrying in your inventory"),
    ("load", ""),
    ("playername", "use this if you don't like your name and want to change it"),
    ("quit", "quits the game"),
    ("save", ""),
    ("scan", "analyze an element in a room or an item"
             "\n       you can SCAN your inventory or room"
             "\n       to get information about what is inside"
             "\n       by typing 'scan inventory' (alternative of INVENTORY)"
             "\n       or 'scan room' to get name, description and room contents"
             "\n       alternatively you can use 'inspect', 'analyze' and 'look'"),
    ("stats", "view information about your character such as"
              "\n        how many items you are carrying, their weight, health, etc."),
    ("take", "pick up an item and add it to your inventory")])

commands_aliases = ["inspect", "look", "analyze"]

# Feedback for invalid input
command_unknown = ["Am I drunk? Let me try that again - I KNOW I can do it!",
                   "I do not know how to do that.",
                   "What is the point of doing this?",
                   "I cannot accomplish that without breaking a bone.",
                   "What will mom say if I did that?",
                   "I do not want to be chased by space FBI."
                   ]

go_deny = ["Going there is not an option.",
           "I cannot go there.",
           "What's in it for me by going there?",
           "This location is unfamiliar to me."]

take_deny = ["This looks scary, I do not want it.",
             "I will not take this.",
             "I do not like this object.",
             "Taking this is not an option.",
             "What would be the point of that?"]

drop_deny = ["I wish I had it in the first place.",
             "I'd love to, but nah.",
             "See, this could work... Well, it didn't, I do not have this item.",
             "Someone give it to me so I can drop it!",
             "Take first, drop second. I'm still on stage 1!"]