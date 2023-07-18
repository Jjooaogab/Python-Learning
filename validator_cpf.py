# Melhorar esse código no futuro!!

import re
import sys
cpf = re.sub(
    r'[^0-9]',
    '',
    '111.444.777-35'
)

cpf_formated_1 = cpf[:9]

counter_1 = 10

result_1 = 0
for i in cpf_formated_1:
    result_1 += int(i) * counter_1
    counter_1 -= 1

result_multiply_1 = result_1 * 10
result_rest_1 = result_multiply_1 % 11
digit_1 = result_rest_1 if result_rest_1 <= 9 else 0


cpf_formated_2 = cpf_formated_1 + str(digit_1)

counter_2 = 11

result_2 = 0
for i in cpf_formated_2:
    result_2 += int(i) * counter_2
    counter_2 -= 1

digit_2_rest = result_2 % 11

if digit_2_rest < 2:
    digit_2 = 0
elif digit_2_rest >= 2:
    digit_2 = 11 - digit_2_rest


cpf_verified_by_machine = f'{cpf_formated_1}{digit_1}{digit_2}'

if cpf == cpf_verified_by_machine:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')

