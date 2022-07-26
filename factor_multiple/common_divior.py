#공약수 구하는 기계

def find_common_divior_machine(input_num_1, input_num_2):

    common_divior_list = []

    num_1 = input_num_1
    num_2 = input_num_2

    if num_1 > num_2:
        smaller_number = num_2
    else:
        smaller_number = num_1
    
    if smaller_number == 0:
        return 0

    for na_nul_su in range(smaller_number):
        if num_1 % smaller_number == 0 and num_2 % smaller_number == 0:
            common_divior_list.append(smaller_number)
            smaller_number -= 1
        else:
            smaller_number -= 1

    return common_divior_list[0]

if __name__ == "__main__":
    print(find_common_divior_machine(0, 48))
    