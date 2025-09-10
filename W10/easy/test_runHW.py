# test_s68114501234_W10.py

import pytest
from W10.easy import s68114501234


def test_baht_to_yuan():
    assert s68114501234.baht_to_yuan(100) == 20.0
    assert s68114501234.baht_to_yuan(0) == 0.0

def test_calculate_rectangle_area():
    assert s68114501234.calculate_rectangle_area(10, 5) == 50
    assert s68114501234.calculate_rectangle_area(2.5, 4) == 10.0

def test_calculate_circle_area():
    assert s68114501234.calculate_circle_area(10) == pytest.approx(314.15926535)
    assert s68114501234.calculate_circle_area(0) == 0.0

def test_celsius_to_fahrenheit():
    assert s68114501234.celsius_to_fahrenheit(30) == 86.0
    assert s68114501234.celsius_to_fahrenheit(0) == 32.0

@pytest.mark.parametrize("number, expected", [(10, True), (7, False), (0, True), (-2, True)])
def test_is_even(number, expected):
    assert s68114501234.is_even(number) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 10, 10), (10, 5, 10), (-1, -5, -1), (5, 5, 5)])
def test_find_max(a, b, expected):
    assert s68114501234.find_max(a, b) == expected

@pytest.mark.parametrize("text, expected", [("hello", "olleh"), ("", ""), ("level", "level")])
def test_reverse_string(text, expected):
    assert s68114501234.reverse_string(text) == expected

@pytest.mark.parametrize("text, expected", [("Hello World", 3), ("Rhythm", 0), ("AEIOUaeiou", 10)])
def test_count_vowels(text, expected):
    assert s68114501234.count_vowels(text) == expected

def test_calculate_simple_interest():
    assert s68114501234.calculate_simple_interest(1000, 5, 2) == 100.0

@pytest.mark.parametrize("text, expected", [("level", True), ("python", False), ("A man a plan a canal Panama", True)])
def test_is_palindrome(text, expected):
    assert s68114501234.is_palindrome(text) == expected

def test_sum_list():
    assert s68114501234.sum_list([1, 2, 3, 4, 5]) == 15
    assert s68114501234.sum_list([]) == 0

def test_average_list():
    assert s68114501234.average_list([10, 20, 30, 40, 50]) == 30.0
    assert s68114501234.average_list([]) == 0.0

@pytest.mark.parametrize("n, expected", [(5, 120), (0, 1), (1, 1), (7, 5040)])
def test_factorial(n, expected):
    assert s68114501234.factorial(n) == expected

@pytest.mark.parametrize("year, expected", [(2024, True), (2023, False), (2000, True), (1900, False)])
def test_is_leap_year(year, expected):
    assert s68114501234.is_leap_year(year) == expected

def test_combine_strings():
    assert s68114501234.combine_strings("Good", " Morning") == "Good Morning"
    assert s68114501234.combine_strings("", "test") == "test"

@pytest.mark.parametrize("score, expected", [(100, 'A'), (80, 'A'), (79, 'B'), (70, 'B'), (65, 'C'), (50, 'D'), (49, 'F'), (0, 'F')])
def test_get_grade(score, expected):
    assert s68114501234.get_grade(score) == expected

def test_find_min_in_list():
    assert s68114501234.find_min_in_list([5, 3, 9, 1, 7]) == 1
    assert s68114501234.find_min_in_list([-1, -5, 0]) == -5
    assert s68114501234.find_min_in_list([]) is None

def test_count_char():
    assert s68114501234.count_char("programming", "m") == 2
    assert s68114501234.count_char("mississippi", "s") == 4

def test_remove_duplicates():
    assert s68114501234.remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert s68114501234.remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert s68114501234.remove_duplicates([]) == []

@pytest.mark.parametrize("number, expected", [(15, "FizzBuzz"), (6, "Fizz"), (10, "Buzz"), (7, "7")])
def test_fizz_buzz(number, expected):
    assert s68114501234.fizz_buzz(number) == expected