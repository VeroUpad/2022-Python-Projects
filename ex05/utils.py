"""EX05 - List and Utils - More List Utils."""
__author__ = "730489785"


def only_evens(many_nums: list[int]) -> list[int]:
    """Given a list of integers, return the even integers."""
    indx_track: int = 0
    result = []
    while indx_track < len(many_nums):
        if many_nums[indx_track] % 2 == 0:
            result.append(many_nums[indx_track])
            indx_track += 1 
        else:
            indx_track += 1
    return result


def concat(first_set: list[int], second_set: list[int]) -> list[int]:
    """Given two lists, return a single list with all values from both lists."""
    whole_set = []
    track_indx: int = 0

    while track_indx < len(first_set):
        whole_set.append(first_set[track_indx])
        track_indx += 1 
   
    track_indx: int = 0
    while track_indx < len(second_set):
        whole_set.append(second_set[track_indx])
        track_indx += 1
    return whole_set


def sub(num_set: list[int], start_indx: int, end_indx: int) -> list[int]:
    """Given list, start index, and end index, return values of list between start and end index."""
    result_set = []
    indx_track: int = start_indx
    if start_indx < 0:
        indx_track: int = 0
    
    stop_read: int = 0
    if end_indx > len(num_set):
        stop_read = len(num_set)
    else:
        stop_read = end_indx

    while indx_track < stop_read:
        result_set.append(num_set[indx_track]) 
        indx_track += 1
    return result_set
