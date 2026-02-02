# data/spells/high_level.py
"""Levels 6-9 spells."""

HIGH_LEVEL = {
    # Level 6
    "Arcane Gate": {
        "level": 6,
        "school": "Conjuration",
        "description": "Create linked teleportation portals that creatures can step through to travel between two portals.",
        "range": "500 feet",
        "components": "V, S"
    },
    "Chain Lightning": {
        "level": 6,
        "school": "Evocation",
        "description": "A bolt of lightning deals 10d8 lightning damage to a primary target (DEX save for half) and arcs to additional targets for 3d8 each.",
        "range": "150 feet",
        "components": "V, S, M"
    },
    "Circle of Death": {
        "level": 6,
        "school": "Necromancy",
        "description": "A 60-foot-radius sphere of necrotic energy deals 8d6 necrotic damage (CON save for half).",
        "range": "150 feet",
        "components": "V, S, M"
    },
    "Disintegrate": {
        "level": 6,
        "school": "Transmutation",
        "description": "A thin green ray deals 10d6+40 force damage (DEX save for half); reduces creature to dust if it drops to 0 from this damage.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Eyebite": {
        "level": 6,
        "school": "Necromancy",
        "description": "For the duration, you can target one creature per turn to be afflicted with sleep, panic (frightened), or sickened; those effects last until end of your next turn.",
        "range": "Self",
        "components": "V, S"
    },
    "Find the Path": {
        "level": 6,
        "school": "Divination",
        "description": "Displays a short, straight path to a specific known location; lasts concentration and provides guidance even if obstructed.",
        "range": "Self",
        "components": "V, S, M"
    },
    "Harm": {
        "level": 6,
        "school": "Necromancy",
        "description": "A creature you choose within range takes 14d6 necrotic damage (CON save for half) or optional effects versus undead.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Heal": {
        "level": 6,
        "school": "Evocation",
        "description": "A creature regains 70 hit points and is freed from blindness, deafness, and any diseases affecting it.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Heroes' Feast": {
        "level": 6,
        "school": "Conjuration",
        "description": "Create a magnificent feast that cures diseases, gives immunity to poison and fear, and grants temporary HP and a bonus to saves.",
        "range": "30 feet",
        "components": "V, S, M"
    },
    "Mass Suggestion": {
        "level": 6,
        "school": "Enchantment",
        "description": "Suggest a course of activity (max 12 words) to up to twelve creatures that fail a WIS save; they follow it for up to 24 hours.",
        "range": "60 feet",
        "components": "V, M"
    },
    "Sunbeam": {
        "level": 6,
        "school": "Evocation",
        "description": "A beam of brilliant light deals 6d8 radiant and blinds creatures on failed CON save; can be used repeatedly for the duration.",
        "range": "Self (60ft line)",
        "components": "V, S, M"
    },
    "True Seeing": {
        "level": 6,
        "school": "Divination",
        "description": "Touch a creature or object and grants truesight out to 120 feet for the duration, allowing see through illusions and invisibility.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Word of Recall": {
        "level": 6,
        "school": "Conjuration",
        "description": "Teleport you and up to five willing creatures to a previously designated sanctuary point, requiring a short rest to recharge.",
        "range": "5 feet",
        "components": "V"
    },

    # Level 7
    "Conjure Celestial": {
        "level": 7,
        "school": "Conjuration",
        "description": "Summon a celestial of challenge rating appropriate to the slot to fight for you for the duration.",
        "range": "90 feet",
        "components": "V, S"
    },
    "Delayed Blast Fireball": {
        "level": 7,
        "school": "Evocation",
        "description": "Create a bead that detonates into a large fireball dealing 12d6 fire after a delay; can grow in power each round it is maintained.",
        "range": "150 feet",
        "components": "V, S, M"
    },
    "Divine Word": {
        "level": 7,
        "school": "Evocation",
        "description": "Speak a word of power to banish or stun creatures with low hit points within range, causing varying effects based on their HP.",
        "range": "30 feet",
        "components": "V"
    },
    "Etherealness": {
        "level": 7,
        "school": "Transmutation",
        "description": "You and willing companions step into the Ethereal Plane for the duration, allowing movement through the Material plane but not affecting it.",
        "range": "Self",
        "components": "V, S"
    },
    "Finger of Death": {
        "level": 7,
        "school": "Necromancy",
        "description": "A creature takes 7d8 + 30 necrotic damage on a hit (CON save for half); humanoids killed by this may become zombies under your control.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Fire Storm": {
        "level": 7,
        "school": "Evocation",
        "description": "Choose up to ten 10-foot cubes where sheets of roaring flame appear dealing 7d10 fire (DEX save for half) to creatures in the area.",
        "range": "150 feet",
        "components": "V, S"
    },
    "Forcecage": {
        "level": 7,
        "school": "Evocation",
        "description": "Create an immobile, invisible prison that traps creatures; they cannot teleport or pass through physical barriers to escape.",
        "range": "100 feet",
        "components": "V, S, M"
    },
    "Magnificent Mansion": {
        "level": 7,
        "school": "Conjuration",
        "description": "Create an extradimensional dwelling with food and servants that can be entered via a shimmering doorway.",
        "range": "30 feet",
        "components": "V, S, M"
    },
    "Mirage Arcane": {
        "level": 7,
        "school": "Illusion",
        "description": "Transform terrain to appear as another type and hide structures for up to 10 days, fooling observers unless they interact closely.",
        "range": "Sight",
        "components": "V, S"
    },
    "Plane Shift": {
        "level": 7,
        "school": "Conjuration",
        "description": "Transport up to eight creatures to a different plane (or banish a creature that fails a CHA save to another plane).",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Prismatic Spray": {
        "level": 7,
        "school": "Evocation",
        "description": "A multi-colored beam strikes multiple creatures, each color inflicting different damage/effects (no save for some, save for others).",
        "range": "Self (60ft cone)",
        "components": "V, S"
    },
    "Project Image": {
        "level": 7,
        "school": "Illusion",
        "description": "Create an illusory duplicate of yourself that you can see and hear through; spells you cast originate from the image.",
        "range": "500 miles",
        "components": "V, S, M"
    },
    "Regenerate": {
        "level": 7,
        "school": "Transmutation",
        "description": "Instantly regain 4d8+15 HP and regrow lost body parts over time; restores limb or organ lost.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Resurrection": {
        "level": 7,
        "school": "Necromancy",
        "description": "Restore life to a creature dead for no more than a century, restoring full hit points and removing many effects, with a costly component.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Reverse Gravity": {
        "level": 7,
        "school": "Transmutation",
        "description": "Reverse gravity in a 100-foot radius so creatures and objects fall upward until the spell ends.",
        "range": "100 feet",
        "components": "V, S, M"
    },
    "Symbol": {
        "level": 7,
        "school": "Abjuration",
        "description": "Inscribe a magical glyph that triggers debilitating effects when activated by a creature, such as pain or paralysis.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Teleport": {
        "level": 7,
        "school": "Conjuration",
        "description": "Instantly transport you and up to eight willing creatures to a destination you specify, with a chance of mishap if you are imprecise.",
        "range": "10 feet",
        "components": "V"
    },

    # Level 8
    "Antimagic Field": {
        "level": 8,
        "school": "Abjuration",
        "description": "Create an invisible sphere within which magic cannot function; spells and magical effects are suppressed while inside.",
        "range": "Self (10-foot radius)",
        "components": "V, S, M"
    },
    "Antipathy/Sympathy": {
        "level": 8,
        "school": "Enchantment",
        "description": "Make a creature or object attract or repel creatures of certain types, potentially dominating movement over a vast area.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Clone": {
        "level": 8,
        "school": "Necromancy",
        "description": "Grow a duplicate body as a safeguard; if you die, your soul can transfer into the clone under certain conditions.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Control Weather": {
        "level": 8,
        "school": "Transmutation",
        "description": "Control weather patterns in a 5-mile radius, changing conditions gradually over time while concentrating.",
        "range": "Self (5-mile radius)",
        "components": "V, S, M"
    },
    "Demiplane": {
        "level": 8,
        "school": "Conjuration",
        "description": "Create a shadowy door to a demiplane you can access for storage or privacy for the duration.",
        "range": "60 feet",
        "components": "S"
    },
    "Dominate Monster": {
        "level": 8,
        "school": "Enchantment",
        "description": "Attempt to control a creature's actions; target must fail a WIS save or be charmed and obey you for duration.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Earthquake": {
        "level": 8,
        "school": "Evocation",
        "description": "Create a localized earthquake that damages and topples structures and creatures in a large area, with ongoing hazards.",
        "range": "500 feet",
        "components": "V, S, M"
    },
    "Feeblemind": {
        "level": 8,
        "school": "Enchantment",
        "description": "Deal severe psychic damage that reduces a target's INT and CHA to 1 and prevents them from casting spells or understanding language.",
        "range": "150 feet",
        "components": "V, S, M"
    },
    "Glibness": {
        "level": 8,
        "school": "Enchantment",
        "description": "You gain an uncanny ability to lie flawlessly; for the duration you can replace any CHA check with a minimum roll.",
        "range": "Self",
        "components": "V"
    },
    "Holy Aura": {
        "level": 8,
        "school": "Abjuration",
        "description": "Bestow a protective aura on allies that grants advantage on saves and resistance to spells and fright, and advantage on attacks against fiends/undead.",
        "range": "Self",
        "components": "V, S, M"
    },
    "Incendiary Cloud": {
        "level": 8,
        "school": "Conjuration",
        "description": "Create a cloud that deals 6d8 fire damage and spreads each round, burning creatures in its area (DEX save for half).",
        "range": "150 feet",
        "components": "V, S"
    },
    "Maze": {
        "level": 8,
        "school": "Conjuration",
        "description": "Banished creature must escape an extradimensional maze with an INT check to end the effect each round.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Mind Blank": {
        "level": 8,
        "school": "Abjuration",
        "description": "Bestows immunity to psychic damage and to divination and mind-reading; grants protection for 24 hours.",
        "range": "Touch",
        "components": "V, S"
    },
    "Power Word Stun": {
        "level": 8,
        "school": "Enchantment",
        "description": "Speak a single word that stuns a creature with 150 HP or fewer without a save.",
        "range": "60 feet",
        "components": "V"
    },
    "Sunburst": {
        "level": 8,
        "school": "Evocation",
        "description": "Create a brilliant sunlight explosion that deals 12d6 radiant damage (CON save for half) and can blind undead and fiends.",
        "range": "150 feet",
        "components": "V, S, M"
    },
    "Telepathy": {
        "level": 8,
        "school": "Evocation",
        "description": "Establish telepathic contact with a creature and send/receive messages over any distance if they are willing or fail a save.",
        "range": "Unlimited",
        "components": "V, S, M"
    },
    "Tsunami": {
        "level": 8,
        "school": "Conjuration",
        "description": "Create a massive wall of water that crashes down, knocking creatures prone and dealing bludgeoning damage in its area.",
        "range": "Sight",
        "components": "V, S"
    },

    # Level 9
    "Astral Projection": {
        "level": 9,
        "school": "Necromancy",
        "description": "Project your astral form to the Astral Plane along with up to eight willing creatures, leaving bodies behind in suspended animation.",
        "range": "10 feet",
        "components": "V, S, M"
    },
    "Foresight": {
        "level": 9,
        "school": "Divination",
        "description": "Bestow a limited preternatural awareness on a willing creature, granting advantage on almost everything and imposing disadvantage on attackers for 8 hours.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Gate": {
        "level": 9,
        "school": "Conjuration",
        "description": "Open a portal linking to another plane that can summon a specific creature or serve as a passage between planes.",
        "range": "60 feet",
        "components": "V, S, M"
    },
    "Imprisonment": {
        "level": 9,
        "school": "Abjuration",
        "description": "Banish a creature into a magical prison by binding its body or mind with a long-duration, variably effecting imprisonment form.",
        "range": "30 feet",
        "components": "V, S, M"
    },
    "Mass Heal": {
        "level": 9,
        "school": "Abjuration",
        "description": "Heal multiple creatures within range, distributing significant HP and ending many debilitating conditions.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Meteor Swarm": {
        "level": 9,
        "school": "Evocation",
        "description": "Call down four enormous meteors that each explode for 20d6 fire and 20d6 bludgeoning in large areas (DEX save for half).",
        "range": "1 mile",
        "components": "V, S"
    },
    "Power Word Kill": {
        "level": 9,
        "school": "Enchantment",
        "description": "Say a word that kills a creature with 100 hit points or fewer instantly, with no saving throw.",
        "range": "60 feet",
        "components": "V"
    },
    "Prismatic Wall": {
        "level": 9,
        "school": "Abjuration",
        "description": "Create a wall of multicolored light; each layer inflicts different effects/damage and is difficult to pass through or dispel.",
        "range": "60 feet",
        "components": "V, S"
    },
    "Shapechange": {
        "level": 9,
        "school": "Transmutation",
        "description": "Transform into any creature whose challenge rating is equal to your level or lower, gaining its statistics and abilities.",
        "range": "Self",
        "components": "V, S, M"
    },
    "Storm of Vengeance": {
        "level": 9,
        "school": "Conjuration",
        "description": "Summon a massive storm dealing acid, lightning, and thunder damage over several rounds with ongoing debilitating effects.",
        "range": "Sight",
        "components": "V, S"
    },
    "Time Stop": {
        "level": 9,
        "school": "Transmutation",
        "description": "Briefly stop time for everyone but you, allowing multiple turns to act while others are frozen until the spell ends or you affect another creature.",
        "range": "Self",
        "components": "V"
    },
    "True Polymorph": {
        "level": 9,
        "school": "Transmutation",
        "description": "Transform a creature or object into another creature or object permanently if concentration is maintained for the full duration.",
        "range": "30 feet",
        "components": "V, S, M"
    },
    "True Resurrection": {
        "level": 9,
        "school": "Necromancy",
        "description": "Restore life to a creature dead up to 200 years, restoring full HP and removing most effects at great material cost.",
        "range": "Touch",
        "components": "V, S, M"
    },
    "Weird": {
        "level": 9,
        "school": "Illusion",
        "description": "Create an illusory horror that frights and damages multiple creatures in an area if they fail a WIS save.",
        "range": "120 feet",
        "components": "V, S"
    },
    "Wish": {
        "level": 9,
        "school": "Conjuration",
        "description": "The most powerful spell: replicate many lower-level spells without components or bend reality at great risk; effects beyond the listed options are at DM discretion.",
        "range": "Self",
        "components": "V"
    }
}
