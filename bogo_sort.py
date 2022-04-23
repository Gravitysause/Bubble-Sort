#########################
## Bogo Sort Algorithm ##
#########################

from sort_functions import in_order
from random import randint


def bogo_sort(num_list):
    run = 0
    while not in_order(num_list):
        run += 1

        for number in range(len(num_list)):
            num = num_list.pop(number)
            num_list.insert(randint(0, len(num_list)), num)
            
        print(num_list)

    return num_list

def bogo_sort_recurrsive(num_list):
    if in_order(num_list):
        return num_list

    for number in range(len(num_list)):
        num = num_list.pop(number)
        num_list.insert(randint(0, len(num_list)), num)

    return bogo_sort_recurrsive(num_list)
