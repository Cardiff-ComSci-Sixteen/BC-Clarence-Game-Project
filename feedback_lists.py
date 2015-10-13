from collections import OrderedDict

# List of possible commands that could be used
commands_expanded = {"playername": ["playername, name, changename"]}

commands = OrderedDict([("go", "moves the player"),
                        ("inspect", "inspect the details of an element"), ("inventory", "see what you are carrying"),
                        ("exits", "shows all available exits"),
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