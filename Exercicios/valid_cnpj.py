"""
code to validate CNPJ
"""


def multiply_cnpj_twelve_digits(cnpj: str) -> int:
    sum = 0
    sum += int(cnpj[0]) * 5
    sum += int(cnpj[1]) * 4
    sum += int(cnpj[2]) * 3
    sum += int(cnpj[3]) * 2
    sum += int(cnpj[4]) * 9
    sum += int(cnpj[5]) * 8
    sum += int(cnpj[6]) * 7
    sum += int(cnpj[7]) * 6
    sum += int(cnpj[8]) * 5
    sum += int(cnpj[9]) * 4
    sum += int(cnpj[10]) * 3
    sum += int(cnpj[11]) * 2

    return sum


def multiply_cnpj_thirteen_digits(cnpj: str, thirteen_digit: str) -> int:
    sum = 0
    sum += int(cnpj[0]) * 6
    sum += int(cnpj[1]) * 5
    sum += int(cnpj[2]) * 4
    sum += int(cnpj[3]) * 3
    sum += int(cnpj[4]) * 2
    sum += int(cnpj[5]) * 9
    sum += int(cnpj[6]) * 8
    sum += int(cnpj[7]) * 7
    sum += int(cnpj[8]) * 6
    sum += int(cnpj[9]) * 5
    sum += int(cnpj[10]) * 4
    sum += int(cnpj[11]) * 3
    sum += int(thirteen_digit) * 2

    return sum


def is_cnpj_valido(cnpj: str) -> bool:
    """
    code to validate CPF
    """

    if_cpf_is_sequential = cnpj == cnpj[0] * len(cnpj)
    if if_cpf_is_sequential:
        print("CNPJ invalidated by repetition!!!")
        return False

    # Calculation of the tenth digit of the CPF
    first_twelve_digits = cnpj[0:12]
    sum_twelve_digit: int = 0

    sum_twelve_digit = multiply_cnpj_twelve_digits(cnpj)

    thirteen_digit = sum_twelve_digit % 11
    thirteen_digit = '0' if thirteen_digit in [0, 1] else \
        str(11 - thirteen_digit)

    # Calculation of the last digit of the CPF

    sum_thirteen_digit: int = 0

    sum_thirteen_digit = multiply_cnpj_thirteen_digits(cnpj, thirteen_digit)

    last_digit = sum_thirteen_digit % 11
    last_digit = '0' if last_digit in [0, 1] else \
        str(11 - last_digit)

    final_digits = thirteen_digit + last_digit

    cpf_generated_by_program = f'{first_twelve_digits}{final_digits}'
    print(cpf_generated_by_program)
    if cnpj == cpf_generated_by_program:
        return True

    return False


if __name__ == "__main__":
    print("CNPJs inválidos")
    print(is_cnpj_valido("0"))
    print(is_cnpj_valido("123456789012345"))
    print(is_cnpj_valido("5" * 14))
    print(is_cnpj_valido("90306453000103"))
    print(is_cnpj_valido("90306453000130"))

    print("CNPJs válidos")
    print(is_cnpj_valido("90306453000133"))
    print(is_cnpj_valido("82671952000100"))
    print(is_cnpj_valido("31049514000165"))
    print(is_cnpj_valido("77437514000133"))
    print(is_cnpj_valido("00059549000151"))
