# 뺄셈
from factor_multiple import common_multiple
from factor_multiple import common_divior

def subtracting_fraction(whole_number_1, numerator_1, denominator_1, whole_nubmer_2, numerator_2, denominator_2):
   try:
      # if numerator_1 >= denominator_1 or numerator_2 >= denominator_2:
      #    raise ValueError('분모와 분자가 같거나 분자가 분모보다 큽니다.')
      if denominator_1 == 0 or denominator_2 == 0: # 분모가 0일때 에러
         raise ValueError('분모가 0입니다.')

      whole_number1_numerator = whole_number_1 * denominator_1
      numerator_1 = numerator_1 + whole_number1_numerator

      whole_number2_numerator = whole_nubmer_2 * denominator_2
      numerator_2 = numerator_2 + whole_number2_numerator

      common_denominator = common_multiple.find_common_multiple_marchine(denominator_1, denominator_2) # 공통분모
      
      fraction_1_common_denominator_denominator_least_common_multiple = common_denominator // denominator_1 # 공통분모로 분수를 만들때 분자에 곱해줄 수
      fraction_2_common_denominator_denominator_least_common_multiple = common_denominator // denominator_2

      common_denominator_numerator_1 = fraction_1_common_denominator_denominator_least_common_multiple * numerator_1 # 분자 분모에 맞추기
      common_denominator_numerator_2 = fraction_2_common_denominator_denominator_least_common_multiple * numerator_2

      if common_denominator_numerator_1 < common_denominator_numerator_2:
         raise IndexError('오른쪽 분수가 왼쪽의 분수보다 더 큽니다. ')

      temporary_numerator = common_denominator_numerator_1 - common_denominator_numerator_2 # 뺄셈
      if temporary_numerator == 0:
         return """

      0"""

      last_whole_number = temporary_numerator // common_denominator  # 가분수에서 대분수로 변환
      last_numerator = temporary_numerator % common_denominator

      if last_numerator == 0:
         return f"""

         {last_whole_number}
            """
      last_numerator_common_denominator_greatest_common_divisior = common_divior.find_common_divior_machine(temporary_numerator, common_denominator) # 약분
      temporary_numerator = last_numerator_common_denominator_greatest_common_divisior // temporary_numerator 
      last_numerator = last_numerator // last_numerator_common_denominator_greatest_common_divisior
      common_denominator = common_denominator // last_numerator_common_denominator_greatest_common_divisior


      return f"""
               {last_numerator}
         {last_whole_number} ----
               {common_denominator}"""

   except Exception as e:
      return f'예외가 발생했습니다. {e}'

if __name__ == "__main__":
   test = subtracting_fraction(1,5,9,0,2,3)
   print(test)