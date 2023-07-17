""" 
Essa aqui é uma calculadora básica, não faz muita coisa
mas as contas básicas ela ja ta conta, como:
Adição, subtração, Divisão e multiplicação
"""

while True:
    number_1 = input('Type a one number: ')
    number_2 = input('Type another number: ')
    operator = input('Type a operator [ +, /, *, -]: ')

    is_valid = None

    try:
        number_1_int = int(number_1)
        number_2_int = int(number_2)
        is_valid = True
    except Exception as err:
        # print(err)
        is_valid = None
        # print(f'Não foi possivel executar a operação entre {number_1} e {number_2}')
        print('Um ou ambos dos números são invalidos, tente novamente')
        continue

    operator_allowed = '+-/*'

    if operator not in operator_allowed:
        print(f'Digite um operador válido. Esses são os permitidos: {operator_allowed}')
        continue

    if len(operator) > 1:
        print('Digite somente um operador') 
        continue

    if operator == '+':
        result_add = number_1_int + number_2_int
        print(f'O resultado da sua conta é: {result_add}')
    elif operator == '-':
        result_sub = number_1_int - number_2_int
        print(f'O resultado da sua conta é: {result_sub}')
    elif operator == '/':
        result_div = number_1_int / number_2_int
        print(f'O resultado da sua conta é: {result_div}')
    elif operator == '*':
        result_multi = number_1_int * number_2_int
        print(f'O resultado da sua conta é: {result_multi}')
    else:
        print('Não era para chegar aqui, rs')

    exit = input('Deseja sair? [S] Sim | [N] Não ').lower().startswith('s')
    if exit is True:
        break
    if exit is False:
        continue