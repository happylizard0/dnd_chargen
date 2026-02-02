# data/spells/low_level.py
"""Level 1 and 2 spells."""

LOW_LEVEL = {
    # Level 1
    "Bless": {
        "level": 1,
        "school": "Enchantment",
        "description": "Up to three creatures of your choice gain a d4 to attack rolls and saving throws for the duration (concentration).",
        "range": "30 feet",
        "components": "V, S, M"
    },
    "Burning Hands": {
        "level": 1,
        "school": "Evocation",
        "description": "A 15-foot cone of flames; each creature in cone must make a DEX save or take 3d6 fire (half on success).",
        "range": "Self (15ft cone)",
        "components": "V, S"
    },
    "Cure Wounds": {
        "level": 1,
        "school": "Evocation",
        "description": "A creature you touch regains hit points equal to 1d8 + spellcasting modifier (healing increases when cast at higher levels).",
        "range": "Touch",
        "components": "V, S"
    },
    "Detect Magic": {
        "level": 1,
        "school": "Divination",
        "description": "For up to 10 minutes, you sense the presence of magic within 30 feet and can see an aura around magic if concentration maintained.",
        "range": "Self",
        "components": "V, S"
    },
    "Guiding Bolt": {
        "level": 1,
        "school": "Evocation",
        "description": "Make a ranged spell attack; on hit deals 4d6 radiant and grants advantage on the next attack against the target.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Magic Missile": {
        "level": 1,
        "school": "Evocation",
        "description": "Create three glowing darts that automatically hit and each deals 1d4+1 force damage (scales with higher slots).",
        "range": "120 feet",
        "components": "V, S"
    },
    "Shield": {
        "level": 1,
        "school": "Abjuration",
        "description": "An invisible barrier grants +5 bonus to AC until start of your next turn and negates Magic Missile hits for that turn.",
        "range": "Self",
        "components": "V, S"
    },
    "Sleep": {
        "level": 1,
        "school": "Enchantment",
        "description": "Puts creatures into magical slumber totaling hit points worth of creatures, starting with lowest HP; no effect on undead or creatures immune to being charmed.",
        "range": "90 feet",
        "components": "V, S, M"
    },

    # Level 2
    "Darkness": {
        "level": 2,
        "school": "Evocation",
        "description": "Create a 15-foot-radius sphere of magical darkness that even darkvision can't see through; can be centered on an object.",
        "range": "60 feet",
        "components": "V, M"
    },
    "Hold Person": {
        "level": 2,
        "school": "Enchantment",
        "description": "Choose a humanoid to make a WIS save; on failure it is paralyzed for the duration with repeat saves at end of each turn.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Invisibility": {
        "level": 2,
        "school": "Illusion",
        "description": "A willing creature becomes invisible until the spell ends or until it attacks or casts a spell; lasts up to 1 hour.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Lesser Restoration": {
        "level": 2,
        "school": "Abjuration",
        "description": "Cure one disease or condition (blinded, deafened, paralyzed, poisoned) affecting a creature you touch.",
        "range": "Touch",
        "components": "V, S"
    },
    "Misty Step": {
        "level": 2,
        "school": "Conjuration",
        "description": "Briefly teleport up to 30 feet to an unoccupied space you can see as a bonus action.",
        "range": "Self",
        "components": "V"
    },
    "Shatter": {
        "level": 2,
        "school": "Evocation",
        "description": "A sudden loud ringing deals 3d8 thunder damage (con save for half) to creatures in a 10-foot-radius and damages objects.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Spiritual Weapon": {
        "level": 2,
        "school": "Evocation",
        "description": "Create a floating spectral weapon that makes a melee spell attack as a bonus action for 1 minute, dealing 1d8+spellcasting modifier force damage.",
        "range": "60 feet",
        "components": "V, S"
    }
}
