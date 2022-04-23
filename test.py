from bubble_sort import bubble_sort
from bogo_sort import bogo_sort, bogo_sort_recurrsive

from random import randint


def test_sort(sorting_method, tests, length):
    """
    Creates all the necessary data to simulate the program without user input.

    Parameters
    ----------
    tests : int
        The number of times the bubble sort will run

    Returns 
    -------
    None
    """

    for test in range(tests):
        list = []

        for index in range(length):
            list.append(randint(1, 10000))

        print(f"test {test + 1}")
        print(f"unordered list: {list}")
        print(f"ordered list: {sorting_method(list)}")


def get_input():
    """
    1. Takes in user input for how long the list will be.
    2. Takes in numbers and adds them to the num_list

    Note that because this method isn't currently being used because \n
    the test_sort() method does the same thing.

    Returns
    -------
    num_list
        The list of numbers
    """
    length = int(input("Amount of Numbers: "))
    num_list = []

    for num in range(length):
        num_list += [int(input())]

    return num_list

print("Bubble Sort Tests:")
test_sort(bubble_sort, 100, 100)

print("\nBogo Sort Tests:")
test_sort(bogo_sort_recurrsive, 1, 5)