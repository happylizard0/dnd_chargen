"""
D&D 5e Rules Engine - Mechanical Calculations

This module implements core D&D 5e mechanics and formulas. It provides functions
for dice rolling, ability score conversions, proficiency calculations, and
spellcasting-related computations.

All calculations follow official D&D 5e rules from the Player's Handbook (PHB).
This module is independent of character management and focuses purely on rules logic.

Key areas:
- Dice rolling (d6, 4d6 drop lowest, etc.)
- Ability modifiers (converting ability scores to modifiers)
- Proficiency bonuses (level-based scaling)
- Spellcasting DC and attack bonuses
- Hit point calculations
- Spell slot progressions (loaded from constants)
"""

import random
from typing import List, Tuple
from data.constants import SPELL_SLOT_PROGRESSIONS


# ========== DICE ROLLING FUNCTIONS ==========

def roll_dice(n: int, sides: int) -> List[int]:
    """
    Roll n dice with the given number of sides.
    
    Args:
        n: Number of dice to roll
        sides: Number of sides on each die (e.g., 6 for d6, 20 for d20)
    
    Returns:
        List of integers representing the result of each die roll
    
    Example:
        roll_dice(4, 6) might return [3, 5, 2, 6]
    """
    return [random.randint(1, sides) for _ in range(n)]


def roll_4d6_drop_lowest() -> Tuple[int, List[int]]:
    """
    Roll 4d6 and drop the lowest die, returning both the total and the rolls.
    This is the standard method for generating ability scores in D&D 5e.
    
    Returns:
        Tuple of (total, list_of_rolls)
        - total: Sum of the three highest rolls
        - list_of_rolls: The original four rolls (for reference)
    
    Example:
        Rolls [3, 5, 2, 6] -> returns (14, [3, 5, 2, 6]) (keeping 3, 5, 6)
    """
    rolls = roll_dice(4, 6)
    sorted_rolls = sorted(rolls)
    # Drop the lowest (index 0) and sum the remaining three
    return sum(sorted_rolls[1:]), rolls


# ========== ABILITY SCORE CONVERSIONS ==========

def ability_mod(score: int) -> int:
    """
    Convert an ability score to its modifier.
    
    D&D 5e formula: (score - 10) // 2
    
    Examples:
        score=10 -> modifier=0
        score=16 -> modifier=+3
        score=8 -> modifier=-1
    
    Args:
        score: The ability score (typically 3-20)
    
    Returns:
        The modifier to add/subtract from d20 rolls
    """
    return (score - 10) // 2


def calc_mods(abilities: dict) -> dict:
    """
    Calculate all ability modifiers at once from ability scores.
    Helper function that applies ability_mod() to every ability in the dictionary.
    
    Args:
        abilities: Dictionary of {ability_name: score}
                   e.g., {"STR": 15, "DEX": 12, ...}
    
    Returns:
        Dictionary of {ability_name: modifier}
                   e.g., {"STR": +2, "DEX": +1, ...}
    """
    return {k: ability_mod(v) for k, v in abilities.items()}


# ========== PROFICIENCY & BONUSES ==========

def proficiency_bonus(level: int) -> int:
    """
    Calculate proficiency bonus based on character level.
    Proficiency increases every 4 levels.
    
    D&D 5e progression:
    - Levels 1-4: +2
    - Levels 5-8: +3
    - Levels 9-12: +4
    - Levels 13-16: +5
    - Levels 17-20: +6
    
    Args:
        level: Character level (1-20)
    
    Returns:
        Proficiency bonus to apply to rolls
    """
    if level >= 17:
        return 6
    if level >= 13:
        return 5
    if level >= 9:
        return 4
    if level >= 5:
        return 3
    return 2


def spell_save_dc(spellcasting_mod: int, proficiency: int) -> int:
    """
    Calculate the Difficulty Class (DC) for creatures to resist spells cast by this character.
    
    D&D 5e formula: 8 + proficiency_bonus + spellcasting_ability_modifier
    
    When a creature casts a spell that forces a target to make a saving throw,
    the target must roll a d20 and add their relevant ability modifier.
    If the result is less than this DC, the spell's effect applies.
    
    Args:
        spellcasting_mod: The modifier from the spellcasting ability (INT, WIS, CHA, etc.)
        proficiency: The character's proficiency bonus (from proficiency_bonus function)
    
    Returns:
        The spell save DC (typically 12-18)
    
    Example:
        A 5th-level wizard with INT+3 and proficiency+3:
        DC = 8 + 3 + 3 = 14
    """
    return 8 + proficiency + spellcasting_mod


def spell_attack_bonus(spellcasting_mod: int, proficiency: int) -> int:
    """
    Calculate the bonus for melee spell attacks (e.g., Eldritch Blast, Shocking Grasp).
    
    D&D 5e formula: proficiency_bonus + spellcasting_ability_modifier
    
    This bonus is added to the d20 roll when the character makes a spell attack.
    
    Args:
        spellcasting_mod: The modifier from the spellcasting ability
        proficiency: The character's proficiency bonus
    
    Returns:
        The spell attack bonus (typically +3 to +10)
    
    Example:
        A 3rd-level warlock with CHA+2 and proficiency+2:
        Attack bonus = 2 + 2 = +4
    """
    return proficiency + spellcasting_mod


# ========== SPELL SLOT MANAGEMENT ==========

def prepareable_spells_count(level: int, spellcasting_mod: int) -> int:
    """
    Calculate how many spells a prepared caster (Cleric, Druid, Paladin, Ranger) can
    prepare for the day.
    
    D&D 5e rule: A prepared caster can prepare a number of spells equal to
    their character level plus their spellcasting ability modifier (minimum of 1).
    
    Args:
        level: Character level (1-20)
        spellcasting_mod: Modifier from the spellcasting ability
    
    Returns:
        Number of spells that can be prepared (minimum 0, but usually >0)
    
    Example:
        A 5th-level cleric with WIS+2:
        Can prepare 5 + 2 = 7 spells
    """
    return max(0, level + spellcasting_mod)


def has_spell_slot(spell_slots: dict, level: int) -> bool:
    """
    Check if a character has at least one available spell slot of a given level.
    
    Args:
        spell_slots: Dictionary {spell_level: remaining_count}
        level: The spell level to check (0-9)
    
    Returns:
        True if at least one slot is available, False otherwise
    
    Example:
        has_spell_slot({1: 2, 2: 1}, 2) -> True
        has_spell_slot({1: 0}, 1) -> False
    """
    return spell_slots.get(level, 0) > 0


def use_spell_slot(spell_slots: dict, level: int) -> bool:
    """
    Consume one spell slot of the given level if available.
    This function modifies the spell_slots dictionary in-place.
    
    Args:
        spell_slots: Dictionary {spell_level: remaining_count}
                     (modified by this function)
        level: The spell level to consume (0-9)
    
    Returns:
        True if a slot was successfully consumed, False if no slots available
    
    Example:
        slots = {1: 2, 2: 1}
        use_spell_slot(slots, 1) -> True, slots becomes {1: 1, 2: 1}
        use_spell_slot(slots, 3) -> False, slots unchanged
    """
    if has_spell_slot(spell_slots, level):
        spell_slots[level] -= 1
        return True
    return False


def compute_spell_slots_for_class_level(char_class: str, level: int) -> dict:
    """
    Look up and return the spell slots available to a character of a given class and level.
    
    This function queries the SPELL_SLOT_PROGRESSIONS table from constants.py,
    which contains PHB-accurate spell slot progressions for all caster classes.
    
    The progression table is structured as:
        {class: {level: {slot_level: count, ...}, ...}, ...}
    
    For a given character level, we find the highest configured progression level
    that doesn't exceed the character's actual level, then return that progression's
    slot dictionary.
    
    Args:
        char_class: The character's class (e.g., "Wizard", "Cleric")
        level: The character's current level (1-20)
    
    Returns:
        Dictionary of {spell_slot_level: count} showing available spell slots
        Returns empty dict if the class is not a spellcaster
    
    Example:
        A 5th-level Wizard should get: {1: 4, 2: 3, 3: 2}
        (4 first-level slots, 3 second-level, 2 third-level)
    """
    # Retrieve the progression table for this class (empty dict if class not in table)
    prog = SPELL_SLOT_PROGRESSIONS.get(char_class, {})
    if not prog:
        return {}
    
    # Find all progression levels that are <= the character's actual level
    applicable_levels = [l for l in prog.keys() if l <= level]
    if not applicable_levels:
        return {}
    
    # Use the highest applicable progression level
    best = max(applicable_levels)
    # Return a copy so modifications don't affect the original progression table
    return prog.get(best, {}).copy()


# ========== HIT POINT CALCULATIONS ==========

def calculate_hp(hit_die: int, con_mod: int, level: int) -> int:
    """
    Calculate a character's total hit points.
    
    D&D 5e HP calculation:
    - At level 1: hit_die + CON_modifier (minimum 1 HP)
    - At each level after: average_of_hit_die + CON_modifier (minimum 1 HP per level)
    
    Where average = (hit_die // 2) + 1
    For example, a d8 has average 5 (d8 ranges 1-8, so (8//2)+1=5)
    
    Args:
        hit_die: The class hit die (e.g., 8 for Wizard, 10 for Rogue, 12 for Barbarian)
        con_mod: The character's CON modifier (can be negative)
        level: The character's level (1-20)
    
    Returns:
        Total hit points (minimum 1, even if modifiers are heavily negative)
    
    Example:
        Wizard (d6) at level 5 with CON+1:
        Level 1: 6 + 1 = 7 HP
        Levels 2-5: 4 + 1 = 5 HP each (where 4 is average of d6)
        Total: 7 + (4 * 4) = 23 HP
    """
    # At level 1: roll + CON modifier
    hp = hit_die + con_mod
    
    # Calculate average roll (rounded down, then +1)
    avg = (hit_die // 2) + 1
    
    # For each level beyond 1: add average + CON modifier
    if level > 1:
        hp += (avg + con_mod) * (level - 1)
    
    # Ensure minimum 1 HP (even if heavily negative modifiers)
    return max(1, hp)