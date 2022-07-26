# 곱셈
from factor_multiple import common_multiple
from factor_multiple import common_divior

def multiplication(whole_number_1, numerator_1, denominator_1, whole_nubmer_2, numerator_2, denominator_2):
   try:
      if denominator_1 == 0 or denominator_2 == 0: # 분모가 0일때 에러  
         raise ValueError('분모가 0입니다.')
      whole_number1_numerator = whole_number_1 * denominator_1 # 대분수 => 가분수
      numerator_1 = numerator_1 + whole_number1_numerator

      whole_number2_numerator = whole_nubmer_2 * denominator_2 # 대분수 => 가분수
      numerator_2 = numerator_2 + whole_number2_numerator


      last_numerator = numerator_1 * numerator_2 # 곱셈
      common_denominator = denominator_1 * denominator_2

      if last_numerator == 0 or common_denominator == 0:
         return """

         0"""

      last_whole_number = last_numerator // common_denominator # 가분수 => 대분수
      last_numerator = last_numerator % common_denominator

      if last_numerator == 0:
         return f"""
               
         {last_whole_number}
               """


      last_numerator_common_denominator_greatest_common_divisior = common_divior.find_common_divior_machine(last_numerator, common_denominator) # 약분
      last_numerator = last_numerator // last_numerator_common_denominator_greatest_common_divisior
      common_denominator = common_denominator // last_numerator_common_denominator_greatest_common_divisior

      return f"""
               {last_numerator}
         {last_whole_number} ----
               {common_denominator}"""
   except Exception as e:
      return f'예외가 발생했습니다. {e}'
if __name__ == "__main__":
   a = multiplication(12, 12, 12, 12, 12, 12)
   print(a)