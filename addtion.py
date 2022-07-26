# 덧셈
from factor_multiple import common_multiple
from factor_multiple import common_divior

def addition(whole_number_1, numerator_1, denominator_1, whole_nubmer_2, numerator_2, denominator_2):
   try:
      # if numerator_1 > denominator_1 or numerator_2 > denominator_2:
      #    raise ValueError('분모와 분자가 같거나 분자가 분모보다 큽니다.')
      if denominator_1 == 0 or denominator_2 == 0: # 분모가 0일때 에러
         raise ValueError('분모가 0입니다.')

      whole_number1_numerator = whole_number_1 * denominator_1
      numerator_1 = numerator_1 + whole_number1_numerator

      whole_number2_numerator = whole_nubmer_2 * denominator_2
      numerator_2 = numerator_2 + whole_number2_numerator

      common_denominator = common_multiple.find_common_multiple_marchine(denominator_1, denominator_2)
      fraction_1_common_denominator_denominator_least_common_multiple = common_denominator // denominator_1
      fraction_2_common_denominator_denominator_least_common_multiple = common_denominator // denominator_2

      numerator_1 =fraction_1_common_denominator_denominator_least_common_multiple * numerator_1
      numerator_2 = fraction_2_common_denominator_denominator_least_common_multiple * numerator_2

      temporary_numerator = numerator_1 + numerator_2
      last_whole_number = temporary_numerator // common_denominator
      last_numerator = temporary_numerator % common_denominator
      if last_numerator == 0:
         return f"""            
                  {last_numerator}
            {last_whole_number} ----
                  {common_denominator}"""

      last_numerator_common_denominator_greatest_common_divisior = common_divior.find_common_divior_machine(last_numerator, common_denominator)
      last_numerator = last_numerator // last_numerator_common_denominator_greatest_common_divisior
      common_denominator = common_denominator // last_numerator_common_denominator_greatest_common_divisior

      if last_numerator == 0:
         return f"""
         {last_whole_number}
            """

      return f"               {last_numerator} \n         {last_whole_number} ----\n               {common_denominator}"

   except Exception as error_massage:
      return f"예외가 발생했습니다. {error_massage}"

if __name__ == "__main__":
   test = addition(12, 2, 4, 42, 1, 3)
   print(test)