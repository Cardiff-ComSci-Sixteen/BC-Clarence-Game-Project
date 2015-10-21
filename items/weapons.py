from lists.feedback_lists import *

weapon_powersword = {
    "id": ["power_sword", "power"],

    "class": 1,

    "weight": 20,

    "name": "Power Sword",

    "description":
    "This sword is powered, it should be able to slice enemies up",

    "attributes": {"damage": 12},

    "feedback": weapon_power_sword_attack
}

weapon_laspistol = {
    "id": ["laspistol"],

    "class": 1,

    "weight": 15,

    "name": "Laspistol",

    "description":
    "This pistol fires a concentrated beam of light,"
    "\nhowever due to its size it is not very powerful",

    "attributes": {"damage": 15},

    "feedback": weapon_laspistol_attack
}

weapon_swordgun = {
    "id": ["swordgun", "sword_gun"],

    "class": 1,

    "weight": 25,

    "name": "a sword-gun",

    "description":
    "Its a sword with a small gun attached to it",

    "attributes": {"damage": 7},

    "feedback": weapon_swordgun_attack
}

weapon_pulse = {
    "id": ["pulserifle", "pulse_rifle"],

    "class": 1,

    "weight": 20,

    "name": "M41A Pulse Rifle",

    "description":
    "The M41A Pulse Rifle is a pulse-action, air-cooled, automatic assault"
    "\nrifle chambered for 10×24mm case-less ammunition.",

    "attributes": {"damage": 26},

    "feedback": weapon_pulse_attack
}

weapon_energysword = {
    "id": ["energysword", "energy_sword"],

    "class": 1,

    "weight": 15,

    "name": "The Energy Sword",

    "description":
    "The Energy Sword consists of a curved hilt, housing an energy storage"
    "\nmodule and a device for projecting the plasma which forms the blade.",

    "attributes": {"damage": 22},

    "feedback": weapon_energysword_attack
}

weapon_sonicemitter = {
    "id": ["sonicemitter", "sonic_emitter"],

    "class": 1,

    "weight": 20,

    "name": "Sonic Emitter",

    "description":
    "The Sonic Emitter chassis is composed of a gray metallic tube,"
    "\noutfitted with four vacuum tubes, a housing for a small energy cell,"
    "\na conical muzzle and a rear-mounted oscilloscope, all attached to a pistol grip.",

    "attributes": {"damage": 50},

    "feedback": weapon_sonicemitter_attack
}

weapon_phaser = {
    "id": ["phaser"],

    "class": 1,

    "weight": 10,

    "name": "Phaser",

    "description":
    "Its a particle-beam weapon that is small enough to fit in the user's palm.",

    "attributes": {"damage": 20},

    "feedback": weapon_phaser_attack
}

weapon_saber = {
    "id": ["lightsaber", "light_saber", "saber"],

    "class": 1,

    "weight": 10,

    "name": "Lightsaber",

    "description":
    "The weapon consists of a blade of pure plasma being emitted from"
    "\nthe hilt and suspended in a force containment field."
    "\nThe field that contains the immense heat of the plasma"
    "\nprotects the wielder whilst allowing the blade to keep its shape.",

    "attributes": {"damage": 40},

    "feedback": weapon_saber_attack
}

weapon_blaster = {
    "id": ["blaster_pistol", "blasterpistol", "dl-44", "dl-44_blaster_pistol"],

    "class": 1,

    "weight": 10,

    "name": "The DL-44 Blaster Pistol",

    "description":
    "The DL-44 was a powerful, highly modifiable and accurate blaster pistol."
    "\nIt packs a heavy punch compared to other pistols without losing accuracy",

    "attributes": {"damage": 30},

    "feedback": weapon_blaster_attack
}
