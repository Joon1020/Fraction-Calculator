# 약수 구하는 기계

def find_divior_marchine(input_number):
    divisor_list = []

    num = input_number
    divior = num

    for i in range(num):
        if num % divior == 0:
            divisor_list.append(divior)
            divior -= 1
        else:
            divior -= 1

    return divisor_list
    