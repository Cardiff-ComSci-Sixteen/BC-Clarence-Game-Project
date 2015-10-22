from collections import OrderedDict

# List of possible commands that could be used
commands_expanded = {"playername": ["playername, name, changename"]}

commands = OrderedDict([
    ("drop", "drop an item from your inventory"),
    ("exits", "show all available exits"),
    ("go", "enter a new room"),
    ("help", "show a list of available commands ('help detailed' for more info)"),
    ("inspect", "inspect the details of an object"),
    ("inventory", "see what you are carrying"),
    ("objectives", "shows your current list of objectives"),
    ("playername", "change your name"),
    ("quit", "quits the game"),
    ("save", "save your current progress"),
    ("scan", "analyze an object for more information"),
    ("stats", "view valuable information about your character"),
    ("take", "pick up an item to your inventory")])

commands_detailed = OrderedDict([
    ("drop", "drop an item from your inventory,"
             "\n            alternatively, you can use 'drop everything'"
             "\n            to let go of all items in your inventory"),
    ("exits", "shows all available exits that are in"
              "\n            the room you are currently in"),
    ("go", "go to a new room"),
    ("help", "shows a list of available commands"),
    ("inspect", "you can inspect a room, item object in room or your inventory"
                "\n            to get basic information about what the item/object is"
                "\n            as well as what the inventory/room's contents are"
                "\n            type 'inspect room' to view room information again or"
                "\n            'inspect room items' to see items in the room you can take."),
    ("inventory", "you can see a list of all the items"
                  "\n            that you are currently carrying in your inventory"),
    ("objectives", "shows your current list of objectives"),
    ("playername", "use this if you don't like your name and want to change it"),
    ("quit", "quits the game"),
    ("save", "saves your progress to saves\ with the name you have types"),
    ("scan", "use your SCANNER to further analyze an object in the room/inventory"
             "\nto get more information about it, if there is any"),
    ("stats", "view information about your character such as"
              "\n            how many items you are carrying, their weight, health, etc."),
    ("take", "pick up an item and add it to your inventory")])

commands_aliases = ["look", "analyze"]

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
           "Destination unknown!",
           "This location is unfamiliar to me."]

go_back_deny = ["I can no longer go back.",
                "Something is impeding with my way back!",
                "What if I told you: I CANNOT GO BACK!"]

take_deny = ["This looks scary, I do not want it.",
             "I will not take this.",
             "I do not like this object.",
             "Taking this is not an option.",
             "What would be the point of that?"]

drop_deny = ["I wish I had it in the first place.",
             "I'd love to, but nah.",
             "See, this could work... Well, it didn't, I do not have this item.",
             "Someone give it to me so I can drop it!",
             "What's in it for me by going there?",
             "Take first, drop second. I'm still on stage 1!"]

scanner_deny = ["The scanner does not show anything.",
                "There is nothing special about this.",
                "It says 'no new information found'."]

weapon_power_sword_attack = ["You swing your sword with fierce force in for a successful strike!",
                             "You charge at the enemy, swinging your Power Sword at them!",
                             "You spin 360 degrees with your Power Sword, striking the enemy!"]

weapon_laspistol_attack = ["You aim at the enemy and pull the trigger.",
                           "You pull out your Laspistol straight from the pocket and shoot at the enemy.",
                           "Using your Laspistol you attempt a 360 no-scope."]

weapon_swordgun_attack = ["You point the small gun at the enemy and shoot.",
                          "You move the blade in front of you and charge towards your enemy.",
                          "You make a weird combo by using both the blade and the"
                          "\ngun against your enemy"]

weapon_pulse_attack = ["You crouch and take a deep breath, sending a bolt at your enemy.",
                       "You make a 360 no-scope with the rifle.",
                       "You load some ammunition in the rifle and shoot multiple times."]

weapon_energysword_attack = ["You focus your mind on the plasma blade and charge at the enemy.",
                             "You swing your sword in a rapid fashion.",
                             "You leap and attempt to stab your opponent's back."]

weapon_sonicemitter_attack = ["You tune the oscilloscope to a sine and blast bass at your opponent.",
                              "You cut all high frequencies and amplify the sound, forming a sonic boom.",
                              "Setting the Sonic Emitter to HIGH and covering your ears you shoot at the opponent."]

weapon_phaser_attack = ["You accumulate energy and send a blast of particles at the enemy.",
                        "With the Phaser you fire a neon-blue beam of proton particles.\n",
                        "The Phaser glows red as you release its payload onto your enemy."]

weapon_saber_attack = ["With the beam protruded you charge at your opponent, slicing at sight.",
                       "You charge Jackie-Chan style at your enemy, swinging the Lightsaber.",
                       "You Throw the Lightsaber at your enemy, returning it using the force."]

weapon_blaster_attack = ["You aim and shoot with your Blaster Pistol at your enemy.",
                         "You charge the Blaster's power and then unload its force at your enemy.",
                         "With the Blaster Pistol in your hand you shoot ferociously."]

encounter_fill = [" and he does not look a happy bunny!",
                  " and he wants you to pay for your tuition fees!",
                  ". They want to steal your underwear!",
                  " and they are ready to fight!",
                  " and you have no option but to fight them!",
                  ". Now is the time to prove yourself!"]