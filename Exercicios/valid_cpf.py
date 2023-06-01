"""
code to validate CPF
"""


def valid_cpf(_cpf: str) -> bool:
    """
    function that validates a cpf
    """

    if_cpf_is_sequential = _cpf == _cpf[0] * len(_cpf)
    if if_cpf_is_sequential:
        print("CPF invalidated by repetition!!!")
        return False

    # Calculation of the tenth digit of the CPF
    first_nine_digits = _cpf[0:9]
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

    if _cpf == cpf_generated_by__program:
        return True

    return False


if __name__ == '__main__':
    cpf = input("Insert CPF: ")
    cpf_is_valid: bool = valid_cpf(cpf)

    if cpf_is_valid:
        print(f'{cpf} its valid')
    else:
        print("CPF invalid!!!")
