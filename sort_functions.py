def in_order(num_list):
    """
    Returns True if list of ints are in least to greatest order.
    Ex1
    ---
    >>> num_list = [0, 1, 5, 6, 8]
    >>> in_order(num_list)
    True
    Ex2
    ---
    >>> num_list = [0, 6, 3, 4]
    >>> in_order(num_list)
    False
    Parameters
    ----------
    num_list : list
        The list of numbers that will be checked
    Returns
    -------
    True 
        num_list is in order from least to greatest
    False
        num_list isn't in order from least to greatest
    """

    for num in range(len(num_list) - 1):
        if num_list[num] > num_list[num + 1]:
            return False

    return True


def swap(num_list, index1, index2):
    """
    Swaps the position of index1 with index2 inside a list. \n
    Note that this method only works if the values are one index apart \n
    (Which is all you need for bubble sort)

    Ex1
    ---
    >>> num_list = [1, 2]
    >>> swap(num_list, 0, 1)
    num_list = [2, 1]

    Parameters
    ----------
    num_list : list
        The list that contains the two numbers
        that will be swapped

    index1 : any
        One of the values that will be swapped

    index2 : any 
        The other value that will be swapped

    Returns
    -------
    None

    """

    value1 = num_list[index1]
    num_list.pop(num_list.index(value1))

    num_list.insert(index2, value1)