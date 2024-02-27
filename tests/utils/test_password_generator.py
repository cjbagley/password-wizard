from unittest import TestCase

from password_wizard.utils.password_generator import PasswordGenerator


class TestPasswordGenerator(TestCase):
    def test_set_length(self) -> None:
        generator = PasswordGenerator()
        self.assertEqual(len(generator.generate()), 18)
        generator.set_length(10)
        self.assertEqual(len(generator.generate()), 10)

    def test_set_special_characters(self) -> None:
        generator = PasswordGenerator()
        self.assertIn("_", generator._special_chr_list)
        self.assertNotIn("a", generator._special_chr_list)
        generator.set_special_characters("!#-")
        self.assertIn("!", generator._special_chr_list)
        self.assertNotIn("_", generator._special_chr_list)

    def test_use_special_characters(self) -> None:
        """As 'secrets' module does not use seeds, this
        posses potential issues with testing the use of
        special characters, as it is possible to generate a
        'correct' random password that just happens to not have
        any. To that end, attempt the generation multiple times
        to determine if special characters used or not.
        """
        generator = PasswordGenerator()
        special_chars = set(generator._special_chr_list)

        """ Test special characters are being used
        Generate password until either special char found, or
        max attempts exceeded. Really unlikely that it will hit
        near the attempt max unless no special chars are being used
        """
        found_special_char = False
        attemps_left = 30
        while attemps_left != 0:
            if special_chars.intersection(generator.generate()):
                found_special_char = True
                break
            attemps_left -= 1

        self.assertTrue(found_special_char)

        """ Testing no special characters functionality
        Try x times, all of which should not have any
        special characters in.
        """
        generator.set_use_special_characters(False)
        attemps_left = 30
        while attemps_left != 0:
            self.assertFalse(special_chars.intersection(generator.generate()))
            attemps_left -= 1
