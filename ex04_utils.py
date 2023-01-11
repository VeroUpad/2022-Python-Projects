"""EX04 - List Utiility Functions."""
__author__ = "730489785"


def all(num_coll: list[int], sngl_num: int) -> bool:
    """Given list of int and single int, return bool of whether or the single int equals all int."""
    indx_track: int = 0
    assert len(num_coll) >= 1
    while indx_track < len(num_coll):
        if num_coll[indx_track] != sngl_num:
            return False
        else:
            indx_track += 1
    return True


def max(many_num: list[int]) -> int:
    """Given a list of integers, return largest value in list."""
    being_checked: int = 0
    running_thru: int = 1 

    if len(many_num) == 0:
        raise ValueError("max() arg is an empty List")

    while running_thru < len(many_num):
        if many_num[being_checked] > many_num[running_thru]:
            running_thru += 1
        else:
            being_checked = running_thru
            running_thru += 1
    return many_num[being_checked]


def is_equal(set_alpha: list[int], set_beta: list[int]) -> bool:
    """Given two lists of int values, compare if every value at every index is equal for both lists."""
    index_alpha: int = 0
    index_beta: int = 0
    while index_alpha < len(set_alpha) and index_beta < len(set_beta):
        if set_alpha[index_alpha] != set_beta[index_beta] or len(set_alpha) != len(set_beta):
            return False
        else: 
            index_alpha += 1
            index_beta += 1
    return True