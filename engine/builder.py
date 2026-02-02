"""
D&D Character Builder - Character Creation and Leveling

This module contains all logic for creating new characters and advancing existing ones.
It orchestrates the various subsystems (rules, spellcasting, biographies) to produce
a complete, playable character.

Key responsibilities:
- Generate ability scores using various methods (4d6, standard array, point buy)
- Apply racial and subrace ability bonuses
- Derive secondary statistics (modifiers, proficiency, hit points, skills)
- Initialize spellcasting (cantrips, known/prepared spells, spell slots)
- Handle character leveling with feature acquisition and stat progression
- Generate character backstories
- Present alignment selection UI

The build_character() function is the primary entry point for creating new characters,
while apply_level_up() handles advancing existing characters to a new level.
"""

import random
from data.constants import RACES, CLASSES, BACKGROUNDS, SKILL_TO_ABILITY
from data.spells import CANTRIP_POOLS, SPELLS_BY_LEVEL
from engine.rules import (
    roll_4d6_drop_lowest, proficiency_bonus,
    calculate_hp, calc_mods, spell_save_dc, spell_attack_bonus, prepareable_spells_count,
    compute_spell_slots_for_class_level
)
from engine.models import Character
from engine.biographer import generate_backstory


# ========== SPELLCASTING INITIALIZATION ==========

def _initialize_spellcasting(char: Character, class_data: dict, level: int):
    """
    Initialize or update all spellcasting-related fields for a character.

    This function is idempotent: if the character already has cantrips or a spellbook,
    they won't be replaced. Instead, prepared spells are adjusted based on the new level.

    The function respects the class's spellcasting_start_level setting. For example,
    Paladins and Rangers don't gain spells until level 2, so this function returns
    early if the character hasn't reached that level yet.

    Process:
    1. Check if character has reached the class's spellcasting start level
    2. Set spellcasting ability and calculate spell DC/attack bonus
    3. Assign cantrips (if not already assigned)
    4. Handle class-specific spell assignment:
       - Wizards: Initialize spellbook with 6 level-1 spells
       - Known-spell casters (Bard, Sorcerer): Assign random known spells
       - Prepared casters (Cleric, Druid, etc.): Assign prepared spells based on level + mod
    5. Calculate and assign spell slots based on class/level progression

    Args:
        char: The Character object to update
        class_data: Class data dictionary from CLASSES (contains spellcaster info)
        level: The character's current level (used for prepared spell count)

    Side effects:
        - Modifies the character's spellcasting-related fields in-place
        - Does not overwrite cantrips or spellbook if already set
    """
    # Check if character has reached the minimum level for this class to have spells
    start_level = class_data.get("spellcasting_start_level", 1)
    if level < start_level:
        return

    # ===== SPELL ABILITY & DC/BONUS =====
    sc_ability = class_data.get("spellcasting_ability")
    char.spellcasting_ability = sc_ability or ""
    # Use an explicit string key to satisfy static type checks (spellcasting_ability may be Optional)
    sc_key = char.spellcasting_ability or ""
    sc_mod = char.ability_mods.get(sc_key, 0)
    char.spell_save_dc = spell_save_dc(sc_mod, char.proficiency)
    char.spell_attack_bonus = spell_attack_bonus(sc_mod, char.proficiency)

    # ===== CANTRIPS =====
    cantrips_known = class_data.get("cantrips_known", 0)
    if cantrips_known > 0 and not char.cantrips:
        # Get the list of possible cantrips for this class and randomly select
        pool = CANTRIP_POOLS.get(char.char_class, [])
        if pool:
            char.cantrips = random.sample(pool, min(cantrips_known, len(pool)))

    # ===== KNOWN / PREPARED / SPELLBOOK SPELLS =====
    # Currently uses level-1 spell pool (future: expand to multiple levels)
    spells_known_num = class_data.get("spells_known")
    class_pool = SPELLS_BY_LEVEL.get(char.char_class, {}).get(1, [])

    if char.char_class == "Wizard":
        # Wizards have a spellbook they populate with written spells
        start_count = min(6, len(class_pool))
        if not char.spellbook:
            char.spellbook = random.sample(class_pool, start_count) if class_pool else []
    elif spells_known_num is not None and spells_known_num > 0:
        # Known-spell casters (Bard, Sorcerer) have a fixed list of known spells
        if not char.known_spells:
            char.known_spells = random.sample(class_pool, min(spells_known_num, len(class_pool))) if class_pool else []
    else:
        # Prepared casters (Cleric, Druid, Paladin, Ranger) can prepare a limited number
        # Rule: prepared spells = level + spellcasting modifier (minimum 1)
        num_prep = prepareable_spells_count(level, sc_mod)
        if class_pool and num_prep > 0:
            if not char.prepared_spells:
                # Initial assignment if not yet set
                char.prepared_spells = random.sample(class_pool, min(num_prep, len(class_pool)))
            else:
                # Adjust existing prepared list if level-up changes the count
                if num_prep > len(char.prepared_spells):
                    # Add more spells if we gained levels and can now prepare more
                    extras = [s for s in class_pool if s not in char.prepared_spells]
                    if extras:
                        add = min(num_prep - len(char.prepared_spells), len(extras))
                        char.prepared_spells.extend(random.sample(extras, add))
                elif num_prep < len(char.prepared_spells):
                    # Remove spells if we somehow have too many prepared (shouldn't happen in normal play)
                    char.prepared_spells = random.sample(char.prepared_spells, num_prep)

    # ===== SPELL SLOTS =====
    # Use the rules helper to look up PHB-accurate spell slot progression
    char.spell_slots = compute_spell_slots_for_class_level(char.char_class, level)


# ========== ALIGNMENT SYSTEM ==========

ALIGNMENT_DESC = {
    """
    Dictionary mapping alignment names to short descriptions.
    These are presented to the user during character creation to help them
    choose an alignment that fits their vision.
    """
    "Lawful Good": "Act as a person of honor and compassion, following a strict code to do the right thing.",
    "Neutral Good": "Do the best a good person can do, helping others without concern for rules.",
    "Chaotic Good": "Act as your conscience directs, with little regard for what others expect.",
    "Lawful Neutral": "Act as law, tradition, or a personal code directs you. Order is paramount.",
    "True Neutral": "Prefer to stay out of moral debates and follow the pragmatic middle ground.",
    "Chaotic Neutral": "Follow your whims. You are an individualist first and foremost.",
    "Lawful Evil": "Take what you want within the limits of a code of tradition or order.",
    "Neutral Evil": "Doing whatever you can get away with. Pure self-interest.",
    "Chaotic Evil": "Act with arbitrary violence, spurred by greed, hatred, or lust for destruction."
}


def suggest_alignment(race: str, char_class: str) -> str:
    """
    Suggest a "default" alignment based on the character's race and class.

    This uses classic D&D tropes and stereotypes to propose an alignment
    that fits the character's archetype. The user can override this suggestion
    when choosing their actual alignment.

    Class-based suggestions (override race):
    - Paladin -> Lawful Good (oath-bound)
    - Monk -> Lawful Neutral (discipline)
    - Druid -> True Neutral (nature balance)
    - Rogue, Bard, Warlock -> Chaotic Neutral (individualistic)
    - Barbarian -> Chaotic Good (freedom-loving)

    Race-based suggestions:
    - Dwarf, Dragonborn -> Lawful Good
    - Elf, Tiefling, Halfling -> Chaotic Good
    - Others -> Neutral Good (default fallback)

    Args:
        race: The character's race
        char_class: The character's class

    Returns:
        A string alignment (e.g., "Lawful Good")
    """
    # Class suggestions take precedence
    if char_class == "Paladin":
        return "Lawful Good"
    if char_class == "Monk":
        return "Lawful Neutral"
    if char_class == "Druid":
        return "True Neutral"
    if char_class in ["Rogue", "Bard", "Warlock"]:
        return "Chaotic Neutral"
    if char_class == "Barbarian":
        return "Chaotic Good"

    # Race suggestions
    if race in ["Dwarf", "Dragonborn"]:
        return "Lawful Good"
    if race in ["Elf", "Tiefling", "Halfling"]:
        return "Chaotic Good"

    # Default for any other combination
    return "Neutral Good"


def get_user_alignment(race: str, char_class: str) -> str:
    """
    Present an interactive menu for the user to select their character's alignment.

    This function displays all 9 alignments with their descriptions, highlights
    the suggested alignment, and allows the user to override with their choice.
    Pressing Enter without a choice selects the suggestion.

    Args:
        race: The character's race (used for suggestion)
        char_class: The character's class (used for suggestion)

    Returns:
        The selected alignment string (e.g., "Lawful Evil")
    """
    # Calculate the suggested alignment based on race and class
    suggested = suggest_alignment(race, char_class)

    print(f"\n--- ALIGNMENT SELECTION ---")
    print(f"Based on your path as a {race} {char_class}, you are naturally drawn to: {suggested}\n")

    # Display all alignment options
    options = list(ALIGNMENT_DESC.keys())
    for idx, align in enumerate(options, 1):
        desc = ALIGNMENT_DESC[align]
        # Mark the suggested alignment with an arrow
        prefix = "-> " if align == suggested else "   "
        print(f"{prefix}{idx}. {align:15} | {desc}")

    # Prompt user for choice
    while True:
        choice = input(f"\nChoose alignment (1-9) or press Enter for [{suggested}]: ").strip()

        if choice == "":
            # Empty input selects the suggestion
            return suggested
        if choice.isdigit() and 1 <= int(choice) <= 9:
            # Valid numeric choice
            return options[int(choice) - 1]
        # Invalid input, reprompt
        print("Invalid choice. Please pick a number between 1 and 9.")


# ========== ABILITY SCORE GENERATION ==========

def generate_abilities(method: str = "4d6") -> dict:
    """
    Generate ability scores using the specified method.

    Three standard D&D 5e methods are supported:

    1. **4d6 (Standard)**:
       Roll 4d6 six times, drop the lowest from each, assign as desired.
       Implementation: Auto-assigns in STR, DEX, CON, INT, WIS, CHA order.
       Typical range: scores between 8-16

    2. **Standard Array**:
       Use the official PHB array: [15, 14, 13, 12, 10, 8]
       Implementation: Shuffles array randomly, then assigns.
       Always the same total but good for fairness.

    3. **Point Buy** (fallback):
       Default to 10 for all abilities (point buy not fully implemented).

    Args:
        method: One of "4d6", "standard", or other (defaults to all 10s)

    Returns:
        Dictionary {ability_name: score} for STR, DEX, CON, INT, WIS, CHA
    """
    stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    if method == "4d6":
        # Roll 4d6 drop lowest for each ability
        return {s: roll_4d6_drop_lowest()[0] for s in stats}
    elif method == "standard":
        # Use PHB standard array, shuffled randomly
        vals = [15, 14, 13, 12, 10, 8]
        random.shuffle(vals)
        return dict(zip(stats, vals))
    else:
        # Fallback: all 10s (neutral baseline)
        return {s: 10 for s in stats}


# ========== CHARACTER CREATION ==========

def build_character(name: str, level: int, race: str, subrace: str, char_class: str,
                    background: str, alignment: str, method: str = "4d6") -> Character:
    """
    Create a complete D&D character from scratch.

    This is the main character creation function. It orchestrates all subsystems
    (ability generation, racial bonuses, skill selection, spellcasting, backstory)
    to produce a fully initialized Character object.

    Process:
    1. Generate or assign base ability scores
    2. Apply racial and subrace ability bonuses
    3. Calculate derived statistics (mods, HP, proficiency)
    4. Assign skills based on class and background
    5. Gather equipment from class and background
    6. Create the Character dataclass instance
    7. Generate a unique backstory
    8. Initialize spellcasting (if the class is a spellcaster)

    Args:
        name: Character's name (used for identification and file saves)
        level: Starting level (typically 1, can be higher for mid-level campaigns)
        race: Character's race (must be a key in RACES from constants)
        subrace: Subrace if applicable (e.g., "Wood Elf"), empty string otherwise
        char_class: Character's class (must be a key in CLASSES from constants)
        background: Character's background (must be a key in BACKGROUNDS)
        alignment: Character's alignment (e.g., "Lawful Good")
        method: Ability score generation method ("4d6", "standard", or other)

    Returns:
        A fully initialized Character object ready for gameplay

    Raises:
        KeyError: If race, class, or background are not defined in constants
    """
    # ===== STEP 1: ABILITY SCORES =====
    abilities = generate_abilities(method)

    # ===== STEP 2: RACIAL BONUSES =====
    # Apply base race bonuses
    race_data = RACES.get(race, {})
    for stat, bonus in race_data.get("ability_mods", {}).items():
        abilities[stat] += bonus

    # Apply subrace bonuses (if subrace is selected)
    if subrace:
        sub_data = race_data.get("subraces", {}).get(subrace, {})
        for stat, bonus in sub_data.get("ability_mods", {}).items():
            abilities[stat] += bonus

    # ===== STEP 3: DERIVED STATISTICS =====
    # Convert ability scores to modifiers
    mods = calc_mods(abilities)

    # Look up class data
    class_data = CLASSES[char_class]
    hit_die = class_data["hit_die"]

    # Calculate HP (uses hit die, CON mod, and level)
    hp = calculate_hp(hit_die, mods["CON"], level)

    # Calculate proficiency bonus
    prof = proficiency_bonus(level)

    # ===== STEP 4: SKILLS =====
    # Start with all skills unproficient
    skills = {s: False for s in SKILL_TO_ABILITY.keys()}

    # Get the class's available skills and pick random ones
    class_skill_list = class_data.get("proficiencies", {}).get("skills", [])
    num_class_choices = 4 if char_class == "Rogue" else (3 if char_class == "Bard" else 2)
    selected_class_skills = random.sample(class_skill_list, min(len(class_skill_list), num_class_choices))
    for s in selected_class_skills:
        skills[s] = True

    # Add background skills
    bg_skills = BACKGROUNDS.get(background, {}).get("skills", [])
    for s in bg_skills:
        skills[s] = True

    # ===== STEP 5: EQUIPMENT & CHARACTER OBJECT CREATION =====
    # Create the Character object with all fields initialized
    char = Character(
        name=name,
        level=level,
        race=race,
        subrace=subrace or "",
        char_class=char_class,
        background=background,
        alignment=alignment,
        abilities=abilities,
        rolls={},
        ability_mods=mods,
        hit_points=hp,
        proficiency=prof,
        saving_throws=class_data.get("proficiencies", {}).get("saving_throws", []),
        skills=skills,
        equipment=class_data.get("equipment", []) + BACKGROUNDS[background].get("equipment", []),
        spells={},
        cantrips=[],
        known_spells=[],
        prepared_spells=[],
        spellbook=[],
        spell_slots={},
        spellcasting_ability="",
        spell_save_dc=0,
        spell_attack_bonus=0,
        features=class_data.get("features", []),
        backstory=""
    )

    # ===== STEP 6: BACKSTORY =====
    # Generate a unique backstory using the biographer module
    char.backstory = generate_backstory(char)

    # ===== STEP 7: SPELLCASTING =====
    # Initialize spellcasting if this class is a spellcaster and has reached spellcasting start level
    start_level = class_data.get("spellcasting_start_level", 1)
    if class_data.get("spellcaster") and level >= start_level:
        _initialize_spellcasting(char, class_data, level)

    return char


# ========== CHARACTER LEVELING ==========

def apply_level_up(char: Character, new_level: int) -> Character:
    """
    Advance a character to a new level, updating all relevant statistics.

    This function handles the complete level-up process:
    1. Grant level-specific features (class features, ASIs)
    2. Update proficiency bonus
    3. Recalculate hit points
    4. Update spellcasting (DC, bonus, slots, prepared spells)

    The function processes each intermediate level (e.g., 5->7 processes level 6, then 7)
    to ensure no features are skipped.

    Args:
        char: The Character object to level up
        new_level: The target level (must be higher than current)

    Returns:
        The updated Character object (same object, modified in-place)
    """
    old_level = char.level
    class_data = CLASSES[char.char_class]

    # ===== STEP 1: PROCESS EACH INTERMEDIATE LEVEL FOR FEATURES =====
    for lvl in range(old_level + 1, new_level + 1):
        # Look up features granted at this level
        features_by_level = class_data.get('features_by_level', {})
        if lvl in features_by_level:
            for feature in features_by_level[lvl]:
                if feature not in char.features:
                    char.features.append(feature)
                    print(f"Gained feature: {feature}")

    # ===== STEP 2: UPDATE CORE STATISTICS =====
    char.level = new_level
    char.ability_mods = calc_mods(char.abilities)
    char.proficiency = proficiency_bonus(new_level)

    # ===== STEP 3: UPDATE HIT POINTS =====
    hit_die = class_data["hit_die"]
    avg_gain = (hit_die // 2) + 1
    # Recalculate from scratch: base + average per level + CON mod per level
    char.hit_points = hit_die + (avg_gain * (new_level - 1)) + (char.ability_mods["CON"] * new_level)

    # ===== STEP 4: UPDATE SPELLCASTING =====
    if class_data.get('spellcaster'):
        start_level = class_data.get('spellcasting_start_level', 1)
        if char.level >= start_level:
            # Ensure spellcasting ability is known
            if not getattr(char, 'spellcasting_ability', ''):
                char.spellcasting_ability = class_data.get('spellcasting_ability', '') or ''

            # Recalculate spell DC and attack bonus (proficiency may have changed)
            sc_key = char.spellcasting_ability or class_data.get('spellcasting_ability', '') or ""
            sc_mod = 0
            if isinstance(char.ability_mods, dict):
                sc_mod = char.ability_mods.get(sc_key, 0)

            char.spell_save_dc = spell_save_dc(sc_mod, char.proficiency)
            char.spell_attack_bonus = spell_attack_bonus(sc_mod, char.proficiency)

            # Update spell slots and prepared spells (may change at certain levels)
            _initialize_spellcasting(char, class_data, char.level)

    return char