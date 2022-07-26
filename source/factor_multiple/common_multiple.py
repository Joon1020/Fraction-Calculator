# 공배수 구하는 기계

def find_common_multiple_marchine(i_num_1, i_num_2):
    the_least_common_multiple = 0

    num_1 = i_num_1
    num_2 = i_num_2
    num = num_1 * num_2

    num_2_multiple = []

    help_number = 1

    while num not in num_2_multiple:
        num_2_multiple.append(num_2 * help_number)
        help_number += 1

    help_number = 0
    num_1_multiple = num_1

    while num_1_multiple not in num_2_multiple:
        num_1_multiple = num_1 * help_number
        help_number += 1
    else:
        the_least_common_multiple = num_1_multiple

    return the_least_common_multiple