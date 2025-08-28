from string_library import *
import unittest

class TestStrings(unittest.TestCase):
    def test_remove_whitespace(self):
        self.assertEqual(normalize_whitespace('  something about this  '), 'something about this')

    def test_remove_large_spaces(self):
        self.assertEqual(normalize_whitespace('My  spacebar   is  broken'), 'My spacebar is broken')

    def test_remove_whitespace_empty(self):
        self.assertEqual(normalize_whitespace(' '), '')
        self.assertEqual(normalize_whitespace(''), '')

    def test_palindrome(self):
        self.assertEqual(is_palindrome('bob'), True)
        self.assertEqual(is_palindrome('sally'), False)

    def test_single_letter_palindrome(self):
        self.assertEqual(is_palindrome('a'), True)

    def test_palindrome_empty(self):
        self.assertEqual(is_palindrome(''), True)
        self.assertEqual(is_palindrome(' '), True)

    def test_word_count(self):
        self.assertEqual(word_count('This should have 5 words'), 5)

    def test_word_count_single_word(self):
        self.assertEqual(word_count('bob'), 1)

    def test_word_count_empty(self):
        self.assertEqual(word_count(' '), 0)
        self.assertEqual(word_count(''), 0)

    def test_frequent_word(self):
        self.assertEqual(most_frequent_word('bob should be the most frequent word bob'), 'bob')

    def test_frequent_equal_occurances(self):
        self.assertEqual(most_frequent_word('all words occur once'), 'all')
        self.assertEqual(most_frequent_word('bob bob bob sally sally sally'), 'bob')

    def test_empty_frequency(self):
        self.assertEqual(most_frequent_word(' '), None)
        self.assertEqual(most_frequent_word(''), None)

    def test_same_word_string(self):
        self.assertEqual(most_frequent_word('bob bob bob bob bob'), 'bob')

    def test_truncate(self):
        self.assertEqual(truncate('this is too big', 4), 't...')
        self.assertEqual(truncate('this is too big', 7), 'this...')

    def test_truncate_empty(self):
        self.assertEqual(truncate("", 0), "")
        self.assertEqual(truncate("", 1), "")

    def test_truncate_small(self):
        self.assertEqual(truncate("bob", 2), "..")

    def test_truncate_equal(self):
        self.assertEqual(truncate('bob', 3), 'bob')

    def test_truncate_larger(self):
        self.assertEqual(truncate('bob', 4), 'bob')
    
    def test_unique(self):
        self.assertEqual(unique_words('A piper has a pipe'), ['A', 'a', 'has', 'pipe', 'piper'])
    
    def test_all_unique(self):
        self.assertEqual(unique_words("I do not have this"), ['I', 'do', 'have', 'not', 'this'])
    
    def test_none_unique(self):
        self.assertEqual(unique_words('L L L L L L L'), ['L'])

    def test_empty_unique(self):
        self.assertEqual(unique_words(''), [])
        self.assertEqual(unique_words(' '), [])
    
    def test_reverse(self):
        self.assertEqual(reverse_words("this has been reversed"), "reversed been has this")

    def test_reverse_one_word(self):
        self.assertEqual(reverse_words('bob'), 'bob')
    
    def test_reverse_empty(self):
        self.assertEqual(reverse_words(''), '')
        self.assertEqual(reverse_words(' '), '')
    
    def test_contains_digit(self):
        self.assertEqual(contains_digit('This string contains a 9'), True)
        self.assertEqual(contains_digit('nobody expects the num6er inquisition'), True)
    
    def test_contains_only_digits(self):
        self.assertEqual(contains_digit("912341"), True)

    def test_contains_digits_empty(self):
        self.assertEqual(contains_digit(""), False)
        self.assertEqual(contains_digit(" "), False)
    
    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("I... have.. too... many... punctuations..."), "I have too many punctuations")
    
    def test_remove_punctuation_puncstring(self):
        self.assertEqual(remove_punctuation('.........'), '')
        self.assertEqual(remove_punctuation(',,,,,,,,,,,'), '')
    
    def test_remove_punctuation_emptyString(self):
        self.assertEqual(remove_punctuation(''), '')
        self.assertEqual(remove_punctuation(' '), ' ')

if __name__ == "__main__":
    unittest.main()