# 배수 구하는 기계

def find_multiple_machine(input_num, num_tb_dis):
    multiple_list = []

    num = input_num
    num_to_be_displayed = num_tb_dis

    for i in range(num_to_be_displayed):
        multiple_list.append(num * num_to_be_displayed)
        num_to_be_displayed -= 1

    return multiple_list