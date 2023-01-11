"""EX05 - List and Utils - Tests for the utils Function."""
__author__ = "730489785"

from utils import only_evens, sub, concat


def test_only_evens_return_whole_num() -> None:
    """Ensure return values result in a whole- number when divided by 2."""
    assert only_evens([3, 5, 16, 4, 28, 32, 33]) == [16, 4, 28, 32]


def test_only_evens_return_empty_list() -> None:
    """Ensure inputing an empty list returns an empty list."""
    assert only_evens([]) == [] 


def test_only_evens_all_odds() -> None:
    """Ensure inputing a list of only even ints returns an empty list."""
    assert only_evens([3, 5, 7, 9, 11]) == []    


def test_concat_return_empty_list() -> None:
    """Given two empty lists, return an empty list."""
    assert concat([], []) == []


def test_concat_two_full_lists() -> None:
    """Test that given two lists, return one combined list."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_one_full_list() -> None:
    """Test that given two lists, one empty, one with three ints, return one combined list."""
    assert concat([], [4, 5, 6]) == [4, 5, 6]


def test_sub_full_list_a() -> None:
    """Test that given a list, return numbers between inputted bounds."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 7) == [4, 5, 6, 7]


def test_sub_full_list_b() -> None:
    """Test that given a list, return numbers between the inputted bounds."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 7) == [5, 6, 7]


def test_sub_full_no_list() -> None:
    """Test that given empty list and bounds return empty list."""
    assert sub([], 4, 7) == []