from collections import OrderedDict

# List of possible commands that could be used
commands_expanded = {"playername": ["playername, name, changename"]}

commands = OrderedDict([("go", "moves the player"),
                        ("inspect", "inspect the details of an element"), ("inventory", "see what you are carrying"),
                        ("exits", "shows all available exits"), ("take", "pick up an item to your inventory"),
                        ("drop", "drop an item from your inventory"),
                        ("help", "shows a list of available commands"), ("save", ""), ("load", ""), ("quit", "quits the game"),
                        ("playername", "change player's name")])

# Feedback for invalid input
command_unknown = ["Am I drunk? Let me try that again.",
                   "I do not know how to do that.",
                   "What is the point of doing this?",
                   "I cannot accomplish that without breaking a bone.",
                   "What will mom say if I did that?",
                   "I do not want to be chased by the FBI."
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