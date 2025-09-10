# test_homework_W10_m.py

import pytest
from s6811450123 import *

@pytest.mark.parametrize("text, expected", [
    ("Hello World", {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}),
    ("Programming", {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}),
    ("aaa bbb c", {'a': 3, 'b': 3, 'c': 1}),
    ("", {})
])
def test_count_character_frequency(text, expected):
    assert count_character_frequency(text) == expected

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3, 4], [3, 4, 5, 6], [3, 4]),
    ([1, 2, 3], [4, 5, 6], []),
    ([], [1, 2, 3], []),
    ([1, 2, 2, 3], [2, 3, 3, 4], [2, 3])
])
def test_find_common_elements(list1, list2, expected):
    assert find_common_elements(list1, list2) == expected

@pytest.mark.parametrize("name, expected", [
    ("john doe", "John Doe"),
    ("ANNA SMITH", "Anna Smith"),
    ("pEtEr jOnEs", "Peter Jones"),
    ("single", "Single")
])
def test_format_name(name, expected):
    assert format_name(name) == expected

@pytest.mark.parametrize("n, expected", [
    (8, [0, 1, 1, 2, 3, 5, 8, 13]),
    (1, [0]),
    (2, [0, 1]),
    (0, [])
])
def test_fibonacci_sequence(n, expected):
    assert fibonacci_sequence(n) == expected

@pytest.mark.parametrize("number, expected", [
    (11, True),
    (10, False),
    (2, True),
    (1, False)
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected

@pytest.mark.parametrize("data, expected", [
    ([{'price': 10, 'quantity': 3}, {'price': 5, 'quantity': 10}], 80.0),
    ([{'price': 2.5, 'quantity': 2}, {'price': 10, 'quantity': 1}], 15.0),
    ([{'price': 100, 'quantity': 1}], 100.0),
    ([], 0.0)
])
def test_calculate_total_sales(data, expected):
    assert calculate_total_sales(data) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("The quick brown fox jumps", "jumps"),
    ("one two three", "three"),
    ("short word", "short"),
    ("", "")
])
def test_find_longest_word(sentence, expected):
    assert find_longest_word(sentence) == expected

@pytest.mark.parametrize("d, expected", [
    ({'a': 1, 'b': 2}, {1: 'a', 2: 'b'}),
    ({'apple': 'fruit', 'dog': 'animal'}, {'fruit': 'apple', 'animal': 'dog'}),
    ({'x': 100}, {100: 'x'}),
    ({}, {})
])
def test_invert_dictionary(d, expected):
    assert invert_dictionary(d) == expected

@pytest.mark.parametrize("text, shift, expected", [
    ("abc", 3, "def"),
    ("xyz", 3, "abc"), # Test wrapping
    ("Hello World", 5, "Mjqqt Btwqi"), # Test case and spaces
    ("test", 0, "test") # Test zero shift
])
def test_caesar_cipher_encrypt(text, shift, expected):
    assert caesar_cipher_encrypt(text, shift) == expected

@pytest.mark.parametrize("numbers, expected", [
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]), # Test reverse-sorted
    ([1, 1, 2, 1, 3], [1, 1, 1, 2, 3]), # Test with duplicates
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])  # Test already-sorted
])
def test_bubble_sort(numbers, expected):
    assert bubble_sort(numbers) == expected