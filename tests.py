import unittest
import io
from unittest import mock

from lib import PalindromeFinder, JSONFileKeyReader


class IsPalindromeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.palindrome_finder = PalindromeFinder(None)

    def test_empty_string(self):
        self.assertTrue(self.palindrome_finder._is_palindrome(""))

    def test_one_letter_string(self):
        self.assertTrue(self.palindrome_finder._is_palindrome("a"))

    def test_two_letter_palindrome(self):
        self.assertTrue(self.palindrome_finder._is_palindrome("bb"))

    def test_three_letter_string(self):
        self.assertTrue(self.palindrome_finder._is_palindrome("gig"))

    def test_odd_length_string(self):
        self.assertTrue(self.palindrome_finder._is_palindrome("civic"))
        
    def test_even_length_string(self):
        self.assertTrue(self.palindrome_finder._is_palindrome("noon"))

    def test_not_palindome_short(self):
        self.assertFalse(self.palindrome_finder._is_palindrome("any"))

    def test_not_palindome_long(self):
        self.assertFalse(self.palindrome_finder._is_palindrome("whatever"))

    def test_several_strings(self):
        self.assertTrue(self.palindrome_finder._is_palindrome("racecar"))
        self.assertTrue(self.palindrome_finder._is_palindrome("kayak"))
        self.assertTrue(self.palindrome_finder._is_palindrome("reviver"))
        self.assertTrue(self.palindrome_finder._is_palindrome("madam"))


class GetPalindromeJSONKeyFileTestCase(unittest.TestCase):

    def process_file(self, test_input):
        memory_file = io.StringIO(initial_value=test_input)
        palindrom_filder = PalindromeFinder(JSONFileKeyReader(memory_file))
        with mock.patch('lib.open', create=True) as mock_open:
            mock_open.return_value = memory_file
            palindromes = palindrom_filder.get_palindromes()
        return palindromes

    def test_get_palindrome(self):
        test_input = '{"foo":"bar"}\n{"key":"racecar"}\n{"key":"not a palindrome","word":"sentence"}'
        palindromes = self.process_file(test_input)        
        self.assertEqual(len(palindromes), 1)
        self.assertEqual(palindromes[0], 'racecar')

    def test_empty_lines(self):
        test_input = '\n\n{"foo":"bar"}\n\n\n{"key":"racecar"}\n{"key":"not a palindrome","word":"sentence"}'
        palindromes = self.process_file(test_input)        
        self.assertEqual(len(palindromes), 1)
        self.assertEqual(palindromes[0], 'racecar')

    def test_not_json_lines(self):
        test_input = 'asdfasdasd\n{"foo":"bar"}sdfgsdfg\nsdfgsdfgsdf\n2345434\n{"key":"racecar"}\n{"key":"not a palindrome","word":"sentence"}'
        palindromes = self.process_file(test_input)        
        self.assertEqual(len(palindromes), 1)
        self.assertEqual(palindromes[0], 'racecar')

    def test_several_matches(self):
        test_input = '{"foo":"bar"}\nasasdasd\n{"key":"racecar"}\n{"key":"not a palindrome","word":"sentence"}\n\nccsdas\n{"data": "some word", "key":"civic","word":"sentence"}'
        palindromes = self.process_file(test_input)        
        self.assertEqual(len(palindromes), 2)
        self.assertEqual(palindromes[0], 'racecar')
        self.assertEqual(palindromes[1], 'civic')


if __name__ == '__main__':
    unittest.main()