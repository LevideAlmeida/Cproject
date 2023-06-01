"""
code to validate CPF

"""

# Calculation of the tenth digit of the CPF
# import sys

CPF = input("Insert CPF: ")

# if_cpf_is_sequential = CPF == CPF[0] * len(CPF)
# if if_cpf_is_sequential:
# print("CPF invalidated by repetition!!!")
# sys.exit(1)

first_nine_digits = CPF[0:9]
regressive_multiplier: int = 10
sum_tenth_digit: int = 0

for digit in first_nine_digits:
    sum_tenth_digit += int(digit) * regressive_multiplier
    regressive_multiplier -= 1

tenth_digit = (sum_tenth_digit * 10) % 11
tenth_digit = tenth_digit if tenth_digit <= 9 else 0

# Calculation of the last digit of the CPF

first_ten_digits = first_nine_digits + str(tenth_digit)
regressive_multiplier: int = 11
sum_last_digit: int = 0

for digit in first_ten_digits:
    sum_last_digit += int(digit) * regressive_multiplier
    regressive_multiplier -= 1

last_digit = (sum_last_digit * 10) % 11
last_digit = last_digit if last_digit <= 9 else 0

cpf_generated_by__program = f'{first_nine_digits}{tenth_digit}{last_digit}'

if CPF == cpf_generated_by__program:
    print(f'{CPF} its valid')

else:
    print("CPF invalid!!!")
