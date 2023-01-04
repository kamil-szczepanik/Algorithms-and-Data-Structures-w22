from ast import List
from naive_search import naive_search
from kmp_search import kmp_search
from kr_search import kr_search
import unittest


class TestFindNaive(unittest.TestCase):
  
    @staticmethod
    def find(substring: str, text: str):
        return naive_search(substring, text)


    def test_empty_substring(self):
        assert self.find("", "abcdef") == []

    def test_empty_text(self):
        assert self.find("abc", "") == []

    def test_empty_both(self):
        assert self.find("", "") == []

    def test_same_length_match(self):
        assert self.find("zozol", "zozol") == [0]

    def test_same_length_no_match(self):
        assert self.find("chomik dżungarski", "sklep zoologiczny") == []

    def test_substring_longer(self):
        assert self.find("chomik dżungarski", "kwiaciarnia") == []

    def test_no_match(self):
        assert self.find("xyz", "abcdef") == []

    def test_single_match_start(self):
        assert self.find("ab", "abcdef") == [0]

    def test_single_match_middle(self):
        assert self.find("cde", "abcdef") == [2]

    def test_single_match_end(self):
        assert self.find("ef", "abcdef") == [4]

    def test_multiple_matches(self):
        assert self.find("cd", "aaabcdefgcdhij") == [4, 9]

    def test_i_before_e(self):
        assert self.find(
            "ei",
            "Except when your foreign neighbour Keith receives eight counterfeit beige sleighs from feisty caffeinated weight lifters. Weird."
        ) == [20, 26, 36, 44, 50, 64, 69, 76, 88, 98, 107, 123]

    def test_overlapping(self):
        assert self.find("abcabc", "abcabcabc") == [0, 3]

    def test_backtracking(self):
        assert self.find("ABCDABD", "A ABCD ABCDABCDABD")

class TestFindKMP(TestFindNaive):
    @staticmethod
    def find(substring: str, text: str):
        return kmp_search(substring, text)


class TestFindKR(TestFindNaive):
    @staticmethod
    def find(substring: str, text: str):
        return kr_search(substring, text, 901)

