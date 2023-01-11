"""EX07 - Dictionary Functions."""
__author__ = "730489785"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings, invert it and return."""
    result: dict[str, str] = {}
    for key in given:
        if given[key] in result:
            raise KeyError("Input value- strings must be unique for output key- strings")
        result[given[key]] = key
    return result


def favorite_color(all_colors: dict[str, str]) -> str:
    """Given list of colors, return most common color."""
    quantity_track: dict[str, int] = {}
    most_common_color: str = ""
    num_track: int = 0 

    for key in all_colors:
        if all_colors[key] in quantity_track:
            quantity_track[all_colors[key]] += 1
        else:
            quantity_track[all_colors[key]] = 1
            
    for value in quantity_track:
        if quantity_track[value] > num_track:
            num_track = quantity_track[value]
            most_common_color = value

    return most_common_color 


def count(input_vals: list[str]) -> dict[str, int]:
    """Given list of strings, return dictionary containg the count of each item."""
    result_dictionary: dict[str, int] = {}
    for item in input_vals:
        if item in result_dictionary:
            result_dictionary[item] += 1
        else: 
            result_dictionary[item] = 1
    return result_dictionary
