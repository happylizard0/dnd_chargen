"""
D&D Character Persistence - File I/O and Serialization

This module handles loading and saving D&D character data to and from JSON files.
It manages the "characters" directory and provides utilities for serializing
Character objects to disk and reconstructing them.

The module uses Python's built-in dataclasses.asdict() for converting the Character
dataclass to a JSON-serializable dictionary, and reconstructs Character objects
from loaded JSON using the dataclass constructor (**dict unpacking).

Key features:
- Automatic character directory creation and management
- JSON serialization with human-readable formatting
- Safe filename generation from character names
- Error handling with user-friendly messages
"""

import os
import json
from dataclasses import asdict
from typing import List, Optional

from engine.models import Character


# ========== DIRECTORY MANAGEMENT ==========

CHARACTER_DIR = "characters"
"""The directory where all character JSON files are stored."""


def ensure_character_dir():
    """
    Create the character directory if it doesn't already exist.
    
    This function should be called before any file operations to ensure
    the directory is ready.
    """
    if not os.path.exists(CHARACTER_DIR):
        os.makedirs(CHARACTER_DIR)


def list_characters() -> List[str]:
    """
    Get a list of all saved character filenames in the characters directory.
    
    Returns:
        List of filenames (e.g., ["aragorn_lvl10.json", "gandalf_lvl20.json"])
        Returns empty list if no characters are saved
    """
    ensure_character_dir()
    return [f for f in os.listdir(CHARACTER_DIR) if f.endswith(".json")]


# ========== FILE I/O OPERATIONS ==========

def save_character(char: Character):
    """
    Save a Character object to a JSON file.
    
    The filename is generated from the character's name and level:
    - Character name is converted to lowercase and spaces become underscores
    - File format: "{name_lowercase}_lvl{level}.json"
    
    The JSON file is saved with 4-space indentation for human readability.
    
    Args:
        char: The Character object to save
    
    Side effects:
        - Creates the character directory if needed
        - Creates or overwrites a JSON file in the characters directory
        - Prints success or error message to console
    
    Example:
        A character named "Aragorn" at level 10 saves to: aragorn_lvl10.json
    """
    ensure_character_dir()
    
    # Generate safe filename: lowercase name with spaces replaced by underscores
    safe_name = char.name.replace(" ", "_").lower()
    filename = f"{safe_name}_lvl{char.level}.json"
    path = os.path.join(CHARACTER_DIR, filename)
    
    try:
        with open(path, "w", encoding="utf-8") as f:
            # Convert the Character dataclass to a dictionary (recursively handles nested objects)
            # JSON dump uses indent=4 for human-readable formatting
            json.dump(asdict(char), f, indent=4)
        print(f"\n[SUCCESS] Character saved to: {path}")
    except Exception as e:
        print(f"\n[ERROR] Could not save character: {e}")


def load_character_from_file(filename: str) -> Optional[Character]:
    """
    Load a character from a JSON file and reconstruct the Character object.
    
    The function handles both full paths and just filenames:
    - If given just a filename, it looks in the characters/ directory
    - If given a full path, it uses that path directly
    
    After loading the JSON, the dictionary is unpacked into the Character
    constructor using the **dict syntax, which reconstructs the dataclass.
    
    Args:
        filename: The filename (e.g., "aragorn_lvl10.json") or full path
    
    Returns:
        Character object if successful, None if loading fails
    
    Side effects:
        - Prints error message to console if loading fails
    """
    # Handle both relative filenames and absolute paths
    if not filename.startswith(CHARACTER_DIR):
        path = os.path.join(CHARACTER_DIR, filename)
    else:
        path = filename

    try:
        with open(path, "r", encoding="utf-8") as f:
            # Load JSON dictionary from file
            data = json.load(f)
            # Unpack the dictionary as constructor arguments to reconstruct the Character object
            # This works because the JSON keys match the Character dataclass field names
            return Character(**data)
    except Exception as e:
        print(f"\n[ERROR] Could not load character: {e}")
        return None