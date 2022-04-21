###########################
## Bubble Sort Algorythm ##
###########################

from sort_functions import swap, in_order


def bubble_sort(num_list):
    """
    Loops through all assets of the list and sorts them using a bubble sorting alogithm.

    Parameters
    ----------
    num_list : list
        The list of numbers that will be sorted

    Returns
    -------
    num_list
        num_list but it's been sorted
    """

    sorted = False

    while not sorted:
        for num in range(0, len(num_list) - 1, 1):
            x_val, y_val = num_list[num], num_list[num + 1]

            if x_val >= y_val:
                swap(num_list, num, num + 1)

        sorted = in_order(num_list)

    return num_list
    


