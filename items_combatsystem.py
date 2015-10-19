from random import randint

def weapons(weapon_input):

	if weapon_input == "sword of azrath" or weapon_input == "sword":
		sword["Damage"] = randint(8,25)
		print("The name of this weapon is " + sword["Name"] + ".")
		print("The Damage of this weapon is " + str(sword["Damage"]) + " HP.")
		print("The Defence of this weapon is " + str(sword["Defence"]) + ".")

	if weapon_input == "the holy gun" or weapon_input ==  "gun":
		gun["Damage"] = randint(35,60)
		print("The name of this weapon is " + gun["Name"] + ".")
		print("The Damage of this weapon is " + str(gun["Damage"]) + " HP.")
		print("The Defence of this weapon is " + str(gun["Defence"]) + ".")

	if weapon_input == "glow stick of life" or weapon_input ==  "lightsaber" or weapon_input ==  "light saber":
		lightsaber["Damage"] = randint(40,65)
		print("The name of this weapon is " + lightsaber["Name"] + ".")
		print("The Damage of this weapon is " + str(lightsaber["Damage"]) + " HP.")
		print("The Defence of this weapon is " + str(lightsaber["Defence"]) + ".")

	if weapon_input == "the blaster rifle" or weapon_input ==  "blaser rifle" or weapon_input ==  "rifle":
		blaster["Damage"] = randint(25,50)
		print("The name of this weapon is " + blaser["Name"] + ".")
		print("The Damage of this weapon is " + str(blaster["Damage"]) + " HP.")
		print("The Defence of this weapon is " + str(blaster["Defence"]) + ".")

		

spoon =  {"Name": "Wooden Spoon", "Defence": 3}
sword = {"Name": "Sword of Azrath", "Defence": 5}
gun = {"Name": "The Holy Gun", "Defence": 1}
lightsaber = {"Name": "Glow Stick of Life", "Defence": 25}
blaster = {"Name": "The Blaster Rifle", "Defence": 3}


