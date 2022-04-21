#########################
## Bogo Sort Algorithm ##
#########################

from sort_functions import in_order
from random import randint


def bogo_sort(num_list):
    while not in_order(num_list):
        for number in range(len(num_list)):
            num = num_list.pop(number)
            num_list.insert(randint(0, len(num_list)), num)

        print(num_list)

    return num_list
