"""
D&D Character Generator - Command Line Interface (CLI)

This module provides all user-facing CLI interactions for the D&D character
generator. It handles menus, prompts, character creation workflow, and display
formatting.

Key responsibilities:
- Main menu and navigation flow
- Character creation wizard (prompts for race, class, alignment, etc.)
- Character display and inspection
- Character leveling workflow
- File selection and management UI

The module uses simple text-based menus with numeric choices and handles
validation to keep the UX predictable and error-tolerant.
"""

import os
from typing import List, Optional

from data.constants import RACES, CLASSES, BACKGROUNDS, SKILL_TO_ABILITY
from data.persist import list_characters, load_character_from_file, save_character
from engine.builder import build_character, apply_level_up, get_user_alignment
from engine.models import Character


# ========== APPLICATION BANNER ==========

_BANNER_SHOWN = False
"""Global flag to ensure the banner is only printed once per session."""

BANNER = r"""
   _  _____  ____   ____  _     ____     _  __    _    ____    _    _     
 | |/ / _ \| __ ) / __ \| |   |  _ \   | |/ /   / \  | __ )  / \  | |    
 | ' / | | |  _ \| |  | | |   | | | |  | ' /   / _ \ |  _ \ / _ \ | |    
 | . \ |_| | |_) | |__| | |___| |_| |  | . \  / ___ \| |_) / ___ \| |___ 
 |_|\_\___/|____/ \____/|_____|____/   |_|\_\/_/   \_\____/_/   \_\_____|
                                                                         
        >>--- D&D CHARACTER GENERATOR : BUILD. LEVEL. ADVENTURE ---<<

        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⢸⡇⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠿⠛⡥⢀⡠⠆⠀⢸⡇⠀⠰⠠⠤⢌⠛⠿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⡿⢋⣁⣀⣀⣁⣀⣀⣀⣀⣸⣇⣀⣀⣀⣀⣉⣀⣀⣈⡙⢿⣿⣿⣿⣿
        ⣿⣿⣿⡟⠛⠋⠉⠉⠉⠉⠉⠉⠉⢩⡿⢿⡍⠉⠉⠉⠉⠉⠉⠉⠉⠛⢻⣿⣿⣿
        ⣿⣿⣿⣿⡀⠀⠀⣠⡴⠦⠀⠀⣠⡟⠁⠈⢻⡄⠀⢠⡀⢼⠓⣆⠀⢀⣿⣿⣿⣿
        ⣿⣿⣿⠘⣧⠀⠀⣏⣹⠀⠀⣰⠟⠀⠀⠀⠀⠻⣆⠉⢳⡈⠧⡼⠀⣼⠃⣿⣿⣿
        ⣿⣿⣿⣦⢹⡆⠀⠉⠁⠀⣰⢃⡴⢶⡄⢠⡶⣤⠘⣆⠈⠃⠀⠀⢰⡏⡐⣿⣿⣿
        ⣿⣿⣿⡿⠰⢿⡄⠀⠀⣴⠃⠀⣠⠼⠃⢿⠀⣸⠃⠘⣦⠀⠀⢠⡿⠂⣋⣿⣿⣿
        ⣿⣿⣿⠀⠸⠈⢷⣀⡾⠃⠀⠈⠛⠛⠃⠈⠛⠁⠀⠀⠘⢷⣀⡾⠁⠀⠀⣿⣿⣿
        ⣿⣿⣿⣤⣤⡴⠾⢿⡷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢾⡿⠷⠦⣤⣤⣿⣿⣿
        ⣿⣿⣿⣿⣷⣤⡒⡈⠻⣦⡀⠀⠤⣶⠀⣴⣒⡒⠀⢀⣴⡟⣁⣔⣤⣾⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⣦⡀⠛⠀⠲⠤⢋⣴⠟⣉⣼⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣄⠀⠀⣠⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""


def print_banner():
    """
    Print the ASCII art banner to the console.
    Used only on the first main menu display to welcome the user.
    """
    print(BANNER)


# ========== MAIN MENU ==========

def main_menu() -> str:
    """
    Display the main menu and return the user's choice.
    
    This function displays the main menu once per session (with the banner),
    then shows menu options and prompts the user to select from numbered options.
    
    Returns:
        One of: "new", "load", "view", "exit"
        ("exit" causes main.py to terminate the application)
    """
    global _BANNER_SHOWN
    # Show the banner only once, on first menu display
    if not _BANNER_SHOWN:
        print_banner()
        _BANNER_SHOWN = True

    while True:
        print("\n==== D&D Character Generator ====")
        print("1. Create New Character")
        print("2. Load & Level Up Character")
        print("3. View Character")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        # Route to appropriate function based on choice
        if choice == "1":
            return "new"
        elif choice == "2":
            return "load"
        elif choice == "3":
            return "view"
        elif choice == "4":
            return "exit"
        else:
            print("Invalid option. Please enter 1-4.")


# ========== UTILITY PROMPTS ==========

def prompt_choice_number(prompt: str, options: List[str]) -> str:
    """
    Display a numbered list of options and prompt the user to select one.
    
    This is the standard method for all multi-choice prompts in the CLI.
    It validates input and re-prompts on invalid selection.
    
    Args:
        prompt: The question or instruction to display above the options
        options: List of option strings to present to the user
    
    Returns:
        The selected option string from the list
    
    Example:
        result = prompt_choice_number("Choose a class", ["Wizard", "Cleric", "Rogue"])
        # User selects "2", returns "Cleric"
    """
    print(f"\n{prompt}:")
    # Display each option with a number (1-indexed for user friendliness)
    for idx, opt in enumerate(options, 1):
        print(f"  {idx}. {opt}")

    # Prompt loop with validation
    while True:
        try:
            choice = int(input("Enter number: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            # User entered non-numeric input
            pass
        # Invalid choice, re-prompt
        print(f"Please enter a number between 1 and {len(options)}.")


def pick_subrace_if_any(race: str) -> str:
    """
    Prompt the user to select a subrace if the chosen race has subraces.
    
    Some races in D&D 5e have subraces (e.g., Wood Elf, High Elf for Elf).
    This function checks if the race has subraces and prompts if needed.
    
    Args:
        race: The race name (must be a key in RACES from constants)
    
    Returns:
        Subrace name if selected, empty string if race has no subraces
    """
    # Look up the race's subraces list
    subraces = RACES.get(race, {}).get("subraces", [])
    if subraces:
        # Race has subraces; prompt user to select
        return prompt_choice_number(f"Select {race} subrace", list(subraces.keys()))
    # No subraces for this race
    return ""


# ========== CHARACTER DISPLAY ==========

def print_character(char: Character):
    """
    Display a character's full information in a formatted, readable layout.
    
    This function displays all character statistics in a structured format:
    - Header: name, level, race, class, alignment
    - Abilities: raw scores and modifiers
    - Health and proficiency
    - Skills: only proficient skills are shown (with calculated bonus)
    - Backstory: character's personal history
    - Spellcasting: if applicable (ability, DC, cantrips, known/prepared/spellbook, slots)
    
    Args:
        char: The Character object to display
    """
    # ===== HEADER =====
    print("\n" + "="*30)
    print(f"NAME: {char.name} | LEVEL: {char.level}")
    print(f"RACE: {char.race} {char.subrace} | CLASS: {char.char_class}")
    print(f"ALIGNMENT: {getattr(char, 'alignment', 'True Neutral')}")
    print("="*30)

    # ===== ABILITY SCORES =====
    print("\nABILITIES:")
    for k, v in char.abilities.items():
        mod = char.ability_mods[k]
        print(f"  {k}: {v:2} ({mod:+d})")  # Format modifier with sign

    # ===== COMBAT STATS =====
    print(f"\nHP: {char.hit_points} | PROF: +{char.proficiency}")

    # ===== SKILLS =====
    print("\nSKILLS (Proficient):")
    for s, val in sorted(char.skills.items()):
        if val:  # Only display proficient skills
            # Calculate skill bonus: ability mod + proficiency bonus
            ability = SKILL_TO_ABILITY[s]
            bonus = char.ability_mods[ability] + char.proficiency
            print(f"  {s}: +{bonus}")

    # ===== BACKSTORY =====
    if char.backstory:
        print(f"\nBACKSTORY:\n{char.backstory}")

    # ===== SPELLCASTING (if applicable) =====
    if getattr(char, 'spellcasting_ability', None):
        print("\nSPELLCASTING:")
        print(f"  Ability: {char.spellcasting_ability}")
        print(f"  Save DC: {char.spell_save_dc}")
        print(f"  Attack Bonus: +{char.spell_attack_bonus}")

        # Display cantrips
        if char.cantrips:
            print("  Cantrips:")
            for c in char.cantrips:
                print(f"    - {c}")

        # Display known spells (for known-spell casters like Bard)
        if char.known_spells:
            print("  Known Spells:")
            for s in char.known_spells:
                print(f"    - {s}")

        # Display prepared spells (for prepared casters like Cleric)
        if char.prepared_spells:
            print("  Prepared Spells:")
            for s in char.prepared_spells:
                print(f"    - {s}")

        # Display spellbook (Wizards only)
        if char.spellbook:
            print("  Spellbook:")
            for s in char.spellbook:
                print(f"    - {s}")

        # Display spell slots
        if char.spell_slots:
            print("  Spell Slots:")
            for level, count in sorted(char.spell_slots.items()):
                print(f"    Level {level}: {count}")


# ========== CHARACTER CREATION WORKFLOW ==========

def cli_new_character():
    """
    Interactive character creation workflow.
    
    This function guides the user through creating a new character by
    prompting for:
    1. Character name
    2. Race and subrace
    3. Class
    4. Background
    5. Ability score generation method (4d6, standard array, etc.)
    6. Alignment (with suggestions)
    
    After collecting input, it calls build_character() to create the character,
    displays the result, and saves it to a JSON file.
    """
    # Prompt for each piece of information in sequence
    name = input("\nCharacter Name: ").strip() or "Nameless"
    race = prompt_choice_number("Select Race", list(RACES.keys()))
    sub = pick_subrace_if_any(race)
    cls = prompt_choice_number("Select Class", list(CLASSES.keys()))
    bg = prompt_choice_number("Select Background", list(BACKGROUNDS.keys()))
    alignment = get_user_alignment(race, cls)  # Interactive alignment UI
    method = prompt_choice_number("Ability Method", ["4d6", "standard", "point_buy"])

    # Build the character with the collected information
    char = build_character(name, 1, race, sub, cls, bg, alignment, method)

    # Display the newly created character
    print_character(char)

    # Save the character to file
    save_character(char)


# ========== CHARACTER MANAGEMENT WORKFLOWS ==========

def cli_load_and_level():
    """
    Load an existing character and level it up.
    
    This function:
    1. Lists all saved characters and prompts user to select one
    2. Loads the selected character from JSON
    3. Prompts for the target level
    4. Applies all level-ups from current level to target level
    5. Displays the updated character
    6. Saves the updated character
    """
    # Get list of saved character files
    files = list_characters()
    if not files:
        print("No characters found.")
        return

    # Prompt user to select which character to load
    selected_file = prompt_choice_number("Select file to load", files)
    char = load_character_from_file(os.path.join("characters", selected_file))

    if char:
        print(f"\nLoaded {char.name}, Level {char.level}")
        try:
            # Prompt for target level
            target = int(input(f"Level up to: ").strip())
            if target > char.level:
                # Apply level-ups incrementally
                char = apply_level_up(char, target)
                # Display the updated character
                print_character(char)
                # Save the updated character
                save_character(char)
            else:
                print(f"Target level must be higher than current level {char.level}.")
        except ValueError:
            print("Invalid level. Please enter a number.")


def cli_view_character():
    """
    Load and display a saved character without making any changes.
    
    This function:
    1. Lists all saved characters and prompts user to select one
    2. Loads the selected character from JSON
    3. Displays it using print_character()
    4. Waits for user confirmation before returning to menu
    """
    # Get list of saved character files
    files = list_characters()
    if not files:
        print("No characters found.")
        return

    # Prompt user to select which character to view
    selected_file = prompt_choice_number("Select character to view", files)
    char = load_character_from_file(os.path.join("characters", selected_file))

    if char:
        # Display the character
        print_character(char)
        # Wait for user confirmation before returning to menu
        input("\nPress Enter to return to menu...")