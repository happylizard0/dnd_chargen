"""
D&D Character Model - Core Data Structure

This module defines the Character dataclass, which serves as the central data
model for representing a D&D 5e player character. All character information
(abilities, skills, spells, equipment, etc.) is stored in instances of this class.

The Character model combines:
- Basic attributes: name, level, race, class, alignment
- Mechanical attributes: abilities, mods, hit points, proficiency
- Proficiency tracking: saving throws, skills, equipment
- Spellcasting system: cantrips, known/prepared spells, spell slots, save DC

This dataclass uses Python's @dataclass decorator for automatic __init__, 
__repr__, and __eq__ methods, making it easy to work with and serialize.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Character:
    """
    Represents a single D&D 5e player character with all relevant statistics
    and equipment needed for gameplay.
    
    Attributes:
        Core Identity:
        - name: Character's name
        - level: Current character level (1-20)
        - race: Character's race (e.g., "Elf", "Dwarf")
        - subrace: Subrace if applicable (e.g., "Wood Elf"), empty string otherwise
        - char_class: Character's class (e.g., "Wizard", "Cleric")
        - background: Character's background (affects skills and personality)
        - alignment: Moral/ethical alignment (e.g., "Lawful Good")
        
        Ability Scores & Modifiers:
        - abilities: Dictionary {STR, DEX, CON, INT, WIS, CHA} -> score (3-20)
        - ability_mods: Derived modifiers from ability scores
        - proficiency: Proficiency bonus based on level (ranges from +2 to +6)
        
        Combat & Health:
        - hit_points: Current HP (calculated from hit die, CON, and level)
        - saving_throws: List of abilities character is proficient in (e.g., ["WIS", "STR"])
        - skills: Dictionary {skill_name -> is_proficient}
        - equipment: List of carried items and gear
        
        Spellcasting (if applicable):
        - cantrips: List of known cantrips (0-level spells)
        - known_spells: Spells the character has learned (for Wizard, Bard, Sorcerer)
        - prepared_spells: Spells chosen for today (for Cleric, Druid, Paladin, Ranger)
        - spellbook: Spells a Wizard has scribed into their book
        - spell_slots: Dictionary {spell_level -> remaining_slots} for casting spells
        - spellcasting_ability: Primary ability for spell casting (e.g., "INT")
        - spell_save_dc: Difficulty class for creatures to resist spells
        - spell_attack_bonus: Bonus for spell attack rolls
        
        Flavor & Story:
        - features: Class features and special abilities granted by level/subclass
        - backstory: Character's personal history and motivations
        - rolls: Stores original ability score rolls (for reference/verification)
    """
    
    # ========== CORE IDENTITY ==========
    name: str
    level: int
    race: str
    subrace: str
    char_class: str
    background: str
    alignment: str
    
    # ========== ABILITY SCORES & MODIFIERS ==========
    abilities: Dict[str, int]  # {STR, DEX, CON, INT, WIS, CHA}
    rolls: Dict[str, List[int]]  # Stores original d6 rolls for reference
    ability_mods: Dict[str, int]  # Derived from abilities
    
    # ========== COMBAT & PROFICIENCY ==========
    hit_points: int
    proficiency: int
    saving_throws: List[str]
    skills: Dict[str, bool]
    equipment: List[str]
    
    # ========== SPELLCASTING FIELDS ==========
    # Legacy field kept for backward compatibility (not actively used)
    spells: Dict[str, List[str]] = field(default_factory=dict)
    
    # Modern spellcasting structure
    cantrips: List[str] = field(default_factory=list)  # 0-level spells
    known_spells: List[str] = field(default_factory=list)  # For Wizard/Bard/Sorcerer
    prepared_spells: List[str] = field(default_factory=list)  # For Cleric/Druid/Paladin/Ranger
    spellbook: List[str] = field(default_factory=list)  # Wizard's spellbook only
    spell_slots: Dict[int, int] = field(default_factory=dict)  # {level -> count}
    spellcasting_ability: Optional[str] = ""  # "INT", "WIS", "CHA", etc.
    spell_save_dc: int = 0  # Difficulty class for spell saves
    spell_attack_bonus: int = 0  # Bonus to spell attack rolls
    
    # ========== FEATURES & STORY ==========
    features: List[str] = field(default_factory=list)  # Class features
    backstory: str = ""  # Character's personal history