# data/constants.py
"""
This module contains constant data structures for D&D 5e character generation.
"""
ALIGNMENT_DESC = {
    "Lawful Good": "Act as a person of honor and compassion, following a strict code to do the right thing.",
    "Neutral Good": "Do the best a good person can do, helping others according to their needs without concern for rules.",
    "Chaotic Good": "Act as your conscience directs, with little regard for what others expect. A 'Robin Hood' archetype.",
    "Lawful Neutral": "Act as law, tradition, or a personal code directs you. Order is more important than moral bias.",
    "True Neutral": "Prefer to stay out of moral debates and follow the pragmatic middle ground.",
    "Chaotic Neutral": "Follow your whims. You are an individualist first and foremost.",
    "Lawful Evil": "Take what you want within the limits of a code of tradition, loyalty, or order.",
    "Neutral Evil": "Doing whatever you can get away with. Pure pragmatism and self-interest.",
    "Chaotic Evil": "Act with arbitrary violence, spurred by greed, hatred, or a simple lust for destruction."
}
RACES = {
    "Human": {"ability_mods": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}},
    "Elf": {
        "ability_mods": {"DEX": 2},
        "subraces": {
            "High Elf": {"ability_mods": {"INT": 1}, "features": ["Cantrip (INT)"], "speed": 30},
            "Wood Elf": {"ability_mods": {"WIS": 1}, "features": ["Fleet of Foot"], "speed": 35},
            "Drow": {"ability_mods": {"CHA": 1}, "features": ["Superior Darkvision"], "speed": 30},
        },
        "speed": 30,
        "features": ["Darkvision"],
    },
    "Dwarf": {
        "ability_mods": {"CON": 2},
        "subraces": {
            "Hill Dwarf": {"ability_mods": {"WIS": 1}, "features": ["Dwarven Toughness"]},
            "Mountain Dwarf": {"ability_mods": {"STR": 2}, "features": ["Armor Training"]},
        },
        "speed": 25,
        "features": ["Darkvision", "Dwarven Resilience"],
    },
    "Halfling": {
        "ability_mods": {"DEX": 2},
        "subraces": {
            "Lightfoot": {"ability_mods": {"CHA": 1}},
            "Stout": {"ability_mods": {"CON": 1}},
        },
        "speed": 25,
        "features": ["Lucky"],
    },
    "Half-Elf": {
        "ability_mods": {"CHA": 2},
        "free_ability_points": 2,
        "speed": 30,
        "features": ["Darkvision", "Fey Ancestry"],
    },
    "Half-Orc": {
        "ability_mods": {"STR": 2, "CON": 1},
        "speed": 30,
        "features": ["Relentless Endurance", "Savage Attacks"],
    },
    "Tiefling": {
        "ability_mods": {"CHA": 2, "INT": 1},
        "speed": 30,
        "features": ["Darkvision", "Infernal Legacy"],
    },
    "Gnome": {
        "ability_mods": {"INT": 2},
        "subraces": {
            "Forest Gnome": {"ability_mods": {"DEX": 1}},
            "Rock Gnome": {"ability_mods": {"CON": 1}},
        },
        "speed": 25,
        "features": ["Gnome Cunning"],
    },
}

CLASSES = {
    "Fighter": {
        "hit_die": 10,
        "skill_choices": 2,
        "proficiencies": {
            "saving_throws": ["STR", "CON"],
            "skills": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
        },
        "spellcaster": False,
        "armor": ["All armor", "Shields"],
        "weapons": ["Simple", "Martial"],
        "features": ["Second Wind", "Fighting Style"],
        "equipment": ["Chain Mail", "Longsword", "Shield"],
    },
    "Wizard": {
        "hit_die": 6,
        "skill_choices": 2,
        "proficiencies": {
            "saving_throws": ["INT", "WIS"],
            "skills": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
        },
        "spellcaster": True,
        "spellcasting_ability": "INT",
        "cantrips_known": 3,
        "spells_known": None,
        "spell_slots_by_level": {1: 2},
        "features": ["Arcane Recovery", "Spellcasting"],
        "equipment": ["Spellbook", "Quarterstaff"],
    },
    "Cleric": {
        "hit_die": 8,
        "skill_choices": 2,
        "proficiencies": {
            "saving_throws": ["WIS", "CHA"],
            "skills": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        },
        "spellcaster": True,
        "spellcasting_ability": "WIS",
        "cantrips_known": 3,
        "spells_known": None,
        "features": ["Divine Domain", "Spellcasting"],
        "equipment": ["Mace", "Scale Mail", "Shield", "Holy Symbol"],
    },
    "Rogue": {
        "hit_die": 8,
        "skill_choices": 4,
        "proficiencies": {
            "saving_throws": ["DEX", "INT"],
            "skills": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
        },
        "spellcaster": False,
        "features": ["Sneak Attack", "Thieves' Cant"],
        "equipment": ["Leather Armor", "Shortsword", "Daggers (2)", "Thieves' Tools"],
    },
    "Paladin": {
        "hit_die": 10,
        "skill_choices": 2,
        "proficiencies": {
            "saving_throws": ["WIS", "CHA"],
            "skills": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
        },
        "spellcaster": True,
        "spellcasting_ability": "CHA",
        "spellcasting_start_level": 2,
        "cantrips_known": 0,
        "spells_known": None,
        "features": ["Divine Sense", "Lay on Hands"],
        "equipment": ["Chain Mail", "Warhammer", "Shield", "Holy Symbol"],
    },
    "Bard": {
        "hit_die": 8,
        "skill_choices": 3,
        "proficiencies": {
            "saving_throws": ["DEX", "CHA"],
            "skills": ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"],
        },
        "spellcaster": True,
        "spellcasting_ability": "CHA",
        "cantrips_known": 2,
        "spells_known": 4,
        "features": ["Bardic Inspiration", "Spellcasting"],
        "equipment": ["Leather Armor", "Lute", "Dagger"],
    },
    "Ranger": {
        "hit_die": 10,
        "skill_choices": 3,
        "proficiencies": {
            "saving_throws": ["STR", "DEX"],
            "skills": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
        },
        "spellcaster": True,
        "spellcasting_ability": "WIS",
        "spellcasting_start_level": 2,
        "cantrips_known": 0,
        "spells_known": None,
        "features": ["Favored Enemy", "Natural Explorer"],
        "equipment": ["Scale Mail", "Shortswords (2)", "Longbow"],
    },
}

SKILL_TO_ABILITY = {
    "Acrobatics": "DEX",
    "Animal Handling": "WIS",
    "Arcana": "INT",
    "Athletics": "STR",
    "Deception": "CHA",
    "History": "INT",
    "Insight": "WIS",
    "Intimidation": "CHA",
    "Investigation": "INT",
    "Medicine": "WIS",
    "Nature": "INT",
    "Perception": "WIS",
    "Performance": "CHA",
    "Persuasion": "CHA",
    "Religion": "INT",
    "Sleight of Hand": "DEX",
    "Stealth": "DEX",
    "Survival": "WIS",
}

BACKGROUNDS = {
    "Soldier": {"skills": ["Athletics", "Intimidation"], "equipment": ["Insignia", "Trophy", "Common clothes", "10 gp"]},
    "Acolyte": {"skills": ["Insight", "Religion"], "equipment": ["Holy symbol", "Prayer book", "Common clothes", "15 gp"]},
    "Criminal": {"skills": ["Deception", "Stealth"], "equipment": ["Crowbar", "Dark clothes", "15 gp"]},
    "Folk Hero": {"skills": ["Animal Handling", "Survival"], "equipment": ["Artisan tool", "Common clothes", "10 gp"]},
    "Noble": {"skills": ["History", "Persuasion"], "equipment": ["Fine clothes", "Signet ring", "25 gp"]},
    "Commoner": {"skills": [], "equipment": ["Common clothes", "5 gp"]},
}

CLASS_PRIORITIES = {
    "Fighter": ["STR", "CON", "DEX"],
    "Rogue": ["DEX", "INT", "CON"],
    "Wizard": ["INT", "CON", "DEX"],
    "Cleric": ["WIS", "CON", "STR"],
    "Paladin": ["CHA", "STR", "CON"],
    "Bard": ["CHA", "DEX", "CON"],
    "Ranger": ["DEX", "WIS", "CON"],
}

# Spell slot progression per class (PHB tables, levels 1-20)
SPELL_SLOT_PROGRESSIONS = {
    # Full casters (Wizard, Cleric, Bard, Druid, Sorcerer) — slots for levels 1..20
    "Wizard": {
        1: {1: 2},
        2: {1: 3},
        3: {1: 4, 2: 2},
        4: {1: 4, 2: 3},
        5: {1: 4, 2: 3, 3: 2},
        6: {1: 4, 2: 3, 3: 3},
        7: {1: 4, 2: 3, 3: 3, 4: 1},
        8: {1: 4, 2: 3, 3: 3, 4: 2},
        9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    },
    "Cleric": {},
    "Bard": {},
}
# Reuse the same full-caster progression for other full caster classes
for _cls in ("Cleric", "Bard"):
    SPELL_SLOT_PROGRESSIONS[_cls] = {lvl: slots.copy() for lvl, slots in SPELL_SLOT_PROGRESSIONS["Wizard"].items()}

# Half-caster progression (Paladin & Ranger) — PHB table levels 1..20
SPELL_SLOT_PROGRESSIONS["Paladin"] = {
    1: {},
    2: {1: 2},
    3: {1: 3},
    4: {1: 3},
    5: {1: 4, 2: 2},
    6: {1: 4, 2: 2},
    7: {1: 4, 2: 3},
    8: {1: 4, 2: 3},
    9: {1: 4, 2: 3, 3: 2},
    10: {1: 4, 2: 3, 3: 2},
    11: {1: 4, 2: 3, 3: 3},
    12: {1: 4, 2: 3, 3: 3},
    13: {1: 4, 2: 3, 3: 3, 4: 1},
    14: {1: 4, 2: 3, 3: 3, 4: 1},
    15: {1: 4, 2: 3, 3: 3, 4: 2},
    16: {1: 4, 2: 3, 3: 3, 4: 2},
    17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
    18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
    19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
    20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
}
SPELL_SLOT_PROGRESSIONS["Ranger"] = {lvl: slots.copy() for lvl, slots in SPELL_SLOT_PROGRESSIONS["Paladin"].items()}


# Placeholder stub for spell data logic (kept for compatibility)
SPELLCASTERS = {
    "Wizard": {1: [2]},
    "Cleric": {1: [2]},
    "Bard": {1: [2]},
    "Paladin": {1: [0]}, # Paladins start spells at level 2
    "Ranger": {1: [0]},
}