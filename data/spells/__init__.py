from .cantrips import CANTRIPS as CANTRIP_SPELLS, CANTRIP_POOLS
from .low_level import LOW_LEVEL
from .mid_level import MID_LEVEL
from .high_level import HIGH_LEVEL

# Backwards-compatible export names expected by the rest of the project
CANTRIPS = CANTRIP_SPELLS

ALL_SPELLS = {
    **CANTRIP_SPELLS,
    **LOW_LEVEL,
    **MID_LEVEL,
    **HIGH_LEVEL
}

# A small compatibility map for starting-level class pools (kept from legacy layout)
SPELLS_BY_LEVEL = {
    "Wizard": {
        1: ["Magic Missile", "Mage Armor", "Shield", "Detect Magic", "Sleep", "Identify", "Burning Hands"],
    },
    "Cleric": {
        1: ["Cure Wounds", "Bless", "Shield of Faith", "Guiding Bolt", "Detect Magic"],
    },
    "Bard": {
        1: ["Healing Word", "Dissonant Whispers", "Charm Person", "Faerie Fire"],
    },
    "Paladin": {
        1: ["Divine Favor", "Shield of Faith", "Bless"],
    },
    "Ranger": {
        1: ["Hunter's Mark", "Cure Wounds", "Detect Magic"],
    },
}
