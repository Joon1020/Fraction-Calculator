import tkinter as tk
from tkinter import ttk
from addtion import addition
from subtraction import subtracting_fraction
from division import division
from multiplication import multiplication

app = tk.Tk()
# app.resizable(False, False)
app.title('분수의 사칙연산')

tabControl = ttk.Notebook(app)

addition_tab = ttk.Frame(tabControl)
subtraction_tab = ttk.Frame(tabControl)
multiplication_tab = ttk.Frame(tabControl)
division_tab = ttk.Frame(tabControl)

tab_var_text = [[addition_tab, '덧셈'], [subtraction_tab, '뺄셈'], [multiplication_tab, '곱셈'], [division_tab, '나눗셈']]

for var_text in tab_var_text:
    tabControl.add(var_text[0], text=var_text[1])
tabControl.pack(expand=1, fill='both')

addition_frame = ttk.LabelFrame(addition_tab, text='분수의 덧셈', height=1, width=50)
subtraction_frame = ttk.LabelFrame(subtraction_tab, text='분수의 뺄셈')
multiplication_frame = ttk.LabelFrame(multiplication_tab, text='분수의 곱셈')
division_frame = ttk.LabelFrame(division_tab, text='분수의 나눗셈')

frame_list = [addition_frame, subtraction_frame, multiplication_frame, division_frame]

for frame in frame_list:
    frame.grid(column=0, row=0, padx=4, pady=4)

# 자연수, 분모, 분자 클래스
class input_fraction_whole_number(tk.IntVar): # 자연수
    def __init__(self, entry_master, row_pos, column_pos=0):
        super().__init__()
        fraction_number = ttk.Entry(entry_master, width=7, textvariable=self)
        fraction_number.grid(row=row_pos,column=column_pos)

class input_fraction_denominator(tk.IntVar): # 분모
    def __init__(self, entry_master, row_pos, column_pos=0):
        super().__init__()
        fraction_number = ttk.Entry(entry_master, width=7, textvariable=self)
        fraction_number.grid(row=row_pos,column=column_pos)
    between_denominator_numerator_line = ttk.Label()
    
class input_fraction_numerator(tk.IntVar): # 분자
    def __init__(self, entry_master, row_pos, column_pos=0):
        super().__init__()
        fraction_number = ttk.Entry(entry_master, width=7, textvariable=self)
        fraction_number.grid(row=row_pos,column=column_pos)

class fraction():
    def __init__(self, fraction_master, column_pos):
        self.fraction_whole_number = input_fraction_whole_number(fraction_master,1, column_pos=column_pos)
        self.fraction_denominator = input_fraction_denominator(fraction_master, 2, column_pos=column_pos+1)
        self.fraction_line = ttk.Label(fraction_master, text='--------------')
        self.fraction_line.grid(column=column_pos+1, row=1)
        self.fraction_numerator = input_fraction_numerator(fraction_master, 0, column_pos=column_pos+1)



class two_fraction_and_math_symbols_with_function():

    def __init__(self, arithmetic_operation_math_symbol, fraction_master, function):
        self.result_label = ttk.Label()


        self.first_fraction = fraction(fraction_master, 1)

        math_symbol = ttk.Label(fraction_master, text=arithmetic_operation_math_symbol)
        math_symbol.grid(column=6, row=1)

        self.second_fraction = fraction(fraction_master, 7)


        def arithmetic_operation_function():
            # global result_label
            first_whole_number = self.first_fraction.fraction_whole_number.get()
            second_whole_number = self.second_fraction.fraction_whole_number.get()
            first_fraction_denominator = self.first_fraction.fraction_denominator.get()
            second_fraction_denominator = self.second_fraction.fraction_denominator.get()
            first_fraction_numerator = self.first_fraction.fraction_numerator.get()
            second_fraction_numerator = self.second_fraction.fraction_numerator.get()

            self.result_label.destroy()
            self.result = function(first_whole_number, first_fraction_numerator, first_fraction_denominator, second_whole_number, second_fraction_numerator, second_fraction_denominator)
            self.result_label = ttk.Label(fraction_master, text=self.result)
            self.result_label.grid(column=15, row=1)

        result_button = ttk.Button(fraction_master, width=3, text='=', command=arithmetic_operation_function)
        result_button.grid(column=10, row=1)

fraction_addition = two_fraction_and_math_symbols_with_function(' + ', addition_frame, addition)
fraction_subtraction = two_fraction_and_math_symbols_with_function(' - ', subtraction_frame, subtracting_fraction)
fraction_multiplication = two_fraction_and_math_symbols_with_function(' × ', multiplication_frame, multiplication)
fraction_divior = two_fraction_and_math_symbols_with_function(' ÷ ', division_frame, division)

app.mainloop()