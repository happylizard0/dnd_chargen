import unittest

from engine.builder import build_character, apply_level_up


class TestSpellcasting(unittest.TestCase):
    def test_paladin_spell_start(self):
        p = build_character('SirTest', 1, 'Human', '', 'Paladin', 'Soldier', 'Lawful Good')
        # Level 1 paladin should not have spellcasting yet
        self.assertFalse(p.spellcasting_ability)
        self.assertEqual(p.spell_slots, {})

        p2 = apply_level_up(p, 2)
        # At level 2 paladin gains spellcasting
        self.assertTrue(p2.spellcasting_ability)
        self.assertIn(1, p2.spell_slots)
        # DC computed properly
        sc_mod = p2.ability_mods.get(p2.spellcasting_ability, 0)
        expected_dc = 8 + p2.proficiency + sc_mod
        self.assertEqual(p2.spell_save_dc, expected_dc)

    def test_wizard_spellbook_and_slots(self):
        w = build_character('Mage', 1, 'Human', '', 'Wizard', 'Acolyte', 'Neutral Good')
        # Wizards should start with a spellbook and 1st-level slots
        self.assertTrue(w.spellbook)
        self.assertEqual(w.spell_slots.get(1), 2)

        w3 = apply_level_up(w, 3)
        # Level 3 should increase slots to include 2nd-level
        self.assertIn(2, w3.spell_slots)
        self.assertEqual(w3.spell_slots.get(1), 4)
        self.assertEqual(w3.spell_slots.get(2), 2)

    def test_wizard_high_level_slots(self):
        w = build_character('Archmage', 1, 'Human', '', 'Wizard', 'Acolyte', 'Neutral Good')
        w17 = apply_level_up(w, 17)
        # PHB-accurate: 17th-level full casters have one 9th-level slot
        self.assertIn(9, w17.spell_slots)
        self.assertEqual(w17.spell_slots.get(9), 1)
        # 1st-level slots remain at 4
        self.assertEqual(w17.spell_slots.get(1), 4)

    def test_noncaster_level_up(self):
        f = build_character('F', 1, 'Human', '', 'Fighter', 'Soldier', 'Lawful Good')
        f2 = apply_level_up(f, 5)
        # Fighter should remain a non-spellcaster
        self.assertFalse(f2.spellcasting_ability)
        self.assertEqual(f2.spell_slots, {})


if __name__ == '__main__':
    unittest.main()
