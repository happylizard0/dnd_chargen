# data/spells/cantrips.py
"""Cantrip (level 0) spell definitions and class cantrip pools."""

CANTRIPS = {
    "Acid Splash": {
        "level": 0,
        "school": "Conjuration",
        "description": "Hurl a bubble of acid; target(s) fail DEX save take 1d6 acid (can target two within 5 ft of each other).",
        "range": "60 feet",
        "components": "V, S"
    },
    "Eldritch Blast": {
        "level": 0,
        "school": "Evocation",
        "description": "Make a ranged spell attack; on hit deals 1d10 force damage (scales with level).",
        "range": "120 feet",
        "components": "V, S"
    },
    "Fire Bolt": {
        "level": 0,
        "school": "Evocation",
        "description": "Make a ranged spell attack; on hit deals 1d10 fire damage (scales with level); ignites flammable objects.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Guidance": {
        "level": 0,
        "school": "Divination",
        "description": "Touch a willing creature; once before spell ends they can add d4 to one ability check.",
        "range": "Touch",
        "components": "V, S"
    },
    "Light": {
        "level": 0,
        "school": "Evocation",
        "description": "Touch an object; it sheds bright light 20 ft and dim light for additional 20 ft for duration.",
        "range": "Touch",
        "components": "V, M"
    },
    "Mage Hand": {
        "level": 0,
        "school": "Conjuration",
        "description": "Create a spectral hand to manipulate objects, open/stow items, and interact within 30 ft.",
        "range": "30 feet",
        "components": "V, S"
    },
    "Minor Illusion": {
        "level": 0,
        "school": "Illusion",
        "description": "Create a sound or an image that lasts; investigation can reveal the illusion with a successful check.",
        "range": "30 feet",
        "components": "S, M"
    },
    "Prestidigitation": {
        "level": 0,
        "school": "Transmutation",
        "description": "Perform minor magical tricks (cleaning, flavoring, light effects) that last up to 1 hour.",
        "range": "10 feet",
        "components": "V, S"
    },
    "Sacred Flame": {
        "level": 0,
        "school": "Evocation",
        "description": "Target makes DEX save or takes 1d8 radiant damage; cover gives no benefit to save.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Vicious Mockery": {
        "level": 0,
        "school": "Enchantment",
        "description": "Target that can hear you makes WIS save or takes 1d4 psychic and has disadvantage on next attack.",
        "range": "60 feet",
        "components": "V"
    },

    # Additional cantrips referenced in class pools (not present previously in ALL_SPELLS)
    "Chill Touch": {
        "level": 0,
        "school": "Necromancy",
        "description": "Make a ranged spell attack (or ranged spell effect) dealing 1d8 necrotic; prevents healing on target until next turn.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Dancing Lights": {
        "level": 0,
        "school": "Evocation",
        "description": "Create up to four torch-sized lights that hover and shed dim light; can combine into a humanoid form.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Mending": {
        "level": 0,
        "school": "Transmutation",
        "description": "Repair a single break or tear in an object or mend a small hole in cloth/wood/metal.",
        "range": "Touch",
        "components": "V, S"
    },
    "Message": {
        "level": 0,
        "school": "Transmutation",
        "description": "Whisper a short message to a creature within 120 feet that only it can hear and reply.",
        "range": "120 feet",
        "components": "V, S, M"
    },
    "Poison Spray": {
        "level": 0,
        "school": "Conjuration",
        "description": "Target makes CON save or takes 1d12 poison damage at range 10 feet.",
        "range": "10 feet",
        "components": "V, S"
    },
    "Ray of Frost": {
        "level": 0,
        "school": "Evocation",
        "description": "Make a ranged spell attack dealing 1d8 cold and reduce target's speed by 10 feet until next turn.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Shocking Grasp": {
        "level": 0,
        "school": "Evocation",
        "description": "Make a melee spell attack dealing 1d8 lightning and prevents target from taking reactions until its next turn.",
        "range": "Touch",
        "components": "V, S"
    },
    "True Strike": {
        "level": 0,
        "school": "Divination",
        "description": "Gain insight to gain advantage on your first attack roll against target on next turn.",
        "range": "30 feet",
        "components": "S"
    },
    "Druidcraft": {
        "level": 0,
        "school": "Transmutation",
        "description": "Perform small nature-related effects (instant weather, flower growth, etc.).",
        "range": "30 feet",
        "components": "V, S"
    },
    "Produce Flame": {
        "level": 0,
        "school": "Conjuration",
        "description": "Create a flame in your hand shedding light; throw to make ranged spell attack dealing 1d8 fire.",
        "range": "30 feet",
        "components": "V, S"
    },
    "Shillelagh": {
        "level": 0,
        "school": "Transmutation",
        "description": "Touch club or quarterstaff, it deals d8 damage and uses your spellcasting ability for attack/damage.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Friends": {
        "level": 0,
        "school": "Enchantment",
        "description": "Gain advantage on Charisma checks directed at one creature for the duration; creature may be hostile afterward.",
        "range": "Self",
        "components": "S"
    },
    "Spare the Dying": {
        "level": 0,
        "school": "Necromancy",
        "description": "Stabilize a creature at 0 HP without needing to make a medicine check.",
        "range": "Touch",
        "components": "V, S"
    },
    "Thaumaturgy": {
        "level": 0,
        "school": "Transmutation",
        "description": "Manifest minor supernatural effects like booming voice, tremor, altering sounds or lights.",
        "range": "30 feet",
        "components": "V"
    }
}

# Class cantrip pools (kept for compatibility with builder)
CANTRIP_POOLS = {
    "Wizard": [
        "Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light",
        "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray",
        "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"
    ],
    "Cleric": [
        "Guidance", "Light", "Mending", "Resistance", "Sacred Flame",
        "Spare the Dying", "Thaumaturgy"
    ],
    "Druid": [
        "Druidcraft", "Guidance", "Mending", "Poison Spray",
        "Produce Flame", "Resistance", "Shillelagh"
    ],
    "Bard": [
        "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending",
        "Message", "Minor Illusion", "Prestidigitation", "True Strike", "Vicious Mockery"
    ],
    "Sorcerer": [
        "Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light",
        "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray",
        "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"
    ],
    "Warlock": [
        "Chill Touch", "Eldritch Blast", "Friends", "Mage Hand",
        "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"
    ],
    "Paladin": [],
    "Ranger": [],
}
