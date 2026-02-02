# data/spells/mid_level.py
"""Level 3, 4 and 5 spells."""

MID_LEVEL = {
    # Level 3
    "Counterspell": {
        "level": 3,
        "school": "Abjuration",
        "description": "When you see a creature casting a spell, attempt to interrupt it; automatic success if the spell is of lower level than your casting slot, otherwise make an ability check.",
        "range": "60 feet",
        "components": "S"
    },
    "Dispel Magic": {
        "level": 3,
        "school": "Abjuration",
        "description": "Choose one creature, object, or magical effect; attempt to end spells on it. Automatically ends spells of its level or lower, higher spells require a dispel check.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Fireball": {
        "level": 3,
        "school": "Evocation",
        "description": "A bright streak erupts into a 20-foot-radius sphere; creatures must make a DEX save or take 8d6 fire (half on success); scales with higher slots.",
        "range": "150 feet",
        "components": "V, S, M"
    },
    "Fly": {
        "level": 3,
        "school": "Transmutation",
        "description": "Target gains a flying speed of 60 feet for up to 10 minutes (concentration).",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Haste": {
        "level": 3,
        "school": "Transmutation",
        "description": "Targets' speed is doubled, they gain +2 AC, have advantage on DEX saves, and take an extra action each turn; ends if concentration broken.",
        "range": "30 feet",
        "components": "V, S, M"
    },
    "Revivify": {
        "level": 3,
        "school": "Necromancy",
        "description": "Touch a creature that died within the last minute and return it to life with 1 HP; requires expensive material component.",
        "range": "Touch",
        "components": "V, S, M"
    },

    # Level 4
    "Banishment": {
        "level": 4,
        "school": "Abjuration",
        "description": "Attempt to send a creature to another plane; the target makes a CHA save or is banished for the duration, longer if it fails repeatedly.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Blight": {
        "level": 4,
        "school": "Necromancy",
        "description": "Necromantic energy drains moisture, dealing 8d8 necrotic to one creature (CON save for half) or damages plants more severely.",
        "range": "30 feet",
        "components": "V, S"
    },
    "Dimension Door": {
        "level": 4,
        "school": "Conjuration",
        "description": "Teleport you and up to one willing creature within 500 feet to a destination you specify that you can visualize or describe.",
        "range": "500 feet",
        "components": "V"
    },
    "Greater Invisibility": {
        "level": 4,
        "school": "Illusion",
        "description": "A creature you touch becomes invisible even if it attacks or casts spells for the duration (concentration).",
        "range": "Touch",
        "components": "V, S"
    },
    "Polymorph": {
        "level": 4,
        "school": "Transmutation",
        "description": "Transform a creature into a new form (beast) with temporary HP; if the target drops to 0 HP in new form, it returns to original form.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Wall of Fire": {
        "level": 4,
        "school": "Evocation",
        "description": "Create a wall of fire that damages creatures near or passing through it for 5d8 fire (save for half) depending on side chosen.",
        "range": "120 feet",
        "components": "V, S, M"
    },

    # Level 5
    "Cloudkill": {
        "level": 5,
        "school": "Conjuration",
        "description": "A 20-foot-radius cloud of poisonous vapor deals 5d8 poison damage (CON save for half) and moves away from you each round.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Cone of Cold": {
        "level": 5,
        "school": "Evocation",
        "description": "A 60-foot cone of cold deals 8d8 cold damage (CON save for half).",
        "range": "Self (60ft cone)",
        "components": "V, S, M"
    },
    "Greater Restoration": {
        "level": 5,
        "school": "Abjuration",
        "description": "End one effect reducing a target's ability score, charmed or petrified condition, or reduce exhaustion by one level, depending on the effect removed.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Hold Monster": {
        "level": 5,
        "school": "Enchantment",
        "description": "Like Hold Person but targets any creature type; targets fail WIS save and are paralyzed for the duration on failure.",
        "range": "90 feet",
        "components": "V, S, M"
    },
    "Raise Dead": {
        "level": 5,
        "school": "Necromancy",
        "description": "Return a dead creature that has been dead no longer than 10 days to life with 1 HP, with long-term penalties to some abilities until healed.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Scrying": {
        "level": 5,
        "school": "Divination",
        "description": "See and hear a particular creature at any distance if it fails a WIS save (or automatically if you have a connection); concentration and expensive components.",
        "range": "Self",
        "components": "V, S, M"
    }
}
