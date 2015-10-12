from collections import OrderedDict

# List of possible commands that could be used
commands = OrderedDict([("east", "move EAST"), ("west", "move WEST"), ("north", "move NORTH"), ("south", "move SOUTH"),
                        ("inspect", "inspect the details of an element"), ("exits", "shows all available exits"),
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