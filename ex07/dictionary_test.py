"""EX07 - Dictionary Functions Tests."""
__author__ = "730489785"

from dictionary import invert, favorite_color, count


def test_invert_letters() -> None: 
    """Given dictionary of letters- keys and letters- values, return inverse."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words() -> None: 
    """Given dictionary of word- keys and word- values, return inverse."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_wordsy() -> None: 
    """Given dictionary of word- keys and word- values, return inverse."""
    assert invert({'fruit': 'dog'}) == {'dog': 'fruit'}


def test_favorite_color_words() -> None: 
    """Given dictionary of names and colors return most popular color."""
    exp: str = "blue"
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == exp


def test_favorite_color_tie() -> None: 
    """Given dictionary of names and colors return most popular color."""
    exp: str = "yellow"
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Heidi": "yellow"}) == exp


def test_count_list_of_numbers() -> None:
    """Given list of numbers- strings, return dictionary with count of each number- string."""
    assert count(["1", "2", "3", "4", "4", "5", "6"]) == {"1": 1, "2": 1, "3": 1, "4": 2, "5": 1, "6": 1}


def test_count_list_of_names() -> None:
    """Given list of names, return dictionary with count of each names."""
    assert count(["Joe", "Abigail", "Joe", "Frank"]) == {'Joe': 2, 'Abigail': 1, 'Frank': 1}


def test_count_list_of_bools() -> None:
    """Given list of bools, return dictionary with count of each bool."""
    assert count(["True", "False", "True", "True"]) == {'True': 3, 'False': 1}