""" 
# Programa da loja do Seu Tanaka.

n_shirts = int(input('Quantas camisas ele vai comprar? '))
value_shirts = float(input('Qual o valor das camisas? '))

value_final = n_shirts * value_shirts

if n_shirts <= 5:
    value_final = value_final * (1 - 3/100)
elif n_shirts <= 10:
    value_final = value_final * (1 - 5/100)
else: 
     value_final = value_final * (1 - 7/100)

print(f'O valor final das camisas foi: {value_final:.1f}')
"""


# print("""
      
#     ************************************************
#             CÁLCULO DE GRANDEZAS ELÉTRICAS
#     ************************************************
#     1. Tensão (em Volt)
#     2. Resistência (em Ohm)
#     3. Corrente (em Ampére)
#     ************************************************
      
#  """)

# input_calc = int(input("Qual grandeza deseja calcular? [1 - 2 - 3] "))

# if input_calc == 1:
#     print(" ")
#     r = int(input("Qual é a resistencia? "))
#     i = int(input("Qual é a corrente? "))
#     result_u = r * i
#     print(f"A tensão é: U={result_u}")
# elif input_calc == 2:
#     print(" ")
#     u = int(input("Qual é a tensão? "))
#     r = int(input("Qual é a resistencia? "))
#     result_i = u / r
#     print(f'A corrente é: i={result_i}')
# elif input_calc == 3:
#     print(" ")
#     i = int(input("Qual é a corrente? "))
#     u = int(input("Qual é a tensão? "))
#     result_r = i / u
#     print(f'A corrente é: i={result_r}')
# else:
#     print("Número invalido.")


""" 
# Ordenação ( Maior ao menor )

person_1 = float(input("Digite a estatura da primeira pessoa: ")) 
person_2 = float(input("Digite a estatura da segunda pessoa: "))
person_3 = float(input("Digite a estatura da terceira pessoa: "))

mais_baixo = None
mais_alto = None
mediano = None

if person_1 > person_2 and person_1 > person_3:
    mais_alto = person_1
    if person_2 > person_3:
        mediano = person_2
        mais_baixo = person_3
    else:
        mediano = person_3
        mais_baixo = person_2
elif person_2 > person_1 and person_2 > person_3:
    mais_alto = f"Pessoa 2 com: {person_2} de altura"
    if person_1 > person_3:
        mediano = f"Pessoa 1 com: {person_1} de altura"
        mais_baixo = f'Pessoa 3 com: {person_3} de altura'
    else:
        mediano = f'Pessoa 3 com: {person_3} de altura'
        mais_baixo = f'Pessoa 1 com: {person_1} de altura'
else: 
    mais_alto = person_3
    if person_1 > person_2:
        mediano = f"Pessoa 1 com: {person_1} de altura"
        mais_baixo = f'Pessoa 2 com: {person_2} de altura'
    else:
        mediano = f'Pessoa 2 com: {person_2} de altura'
        mais_baixo = f'Pessoa 1 com: {person_1} de altura'

print(f"O mais baixo é: {mais_baixo}, mais alto: {mais_alto} e o mediano: {mediano}")
"""
"""
# Exercicio Proposto #1

print("Exercicio Proposto #1")

number = int(input("Digite um número inteiro e positivo: "))

number_verify = number % 2 == 0

if number_verify:
    number_square_root = pow(number, 2)
    print(f'O seu número {number} é par, e esse é o quadrado dele: {number_square_root}')
else:
    number_cube_root = pow(number, 3)
    print(f'O seu número {number} é ímpar, e esse é o cubo dele: {number_cube_root}')
"""
""" # Exercicio Proposto #2

print("Exercicio Proposto #2 \n")

number_1 = int(input("Digte o primeiro número: "))
number_2 = int(input("Digite o segundo número: "))
print("\n")

print(f"{'*' * 18} {'O que deseja fazer?'} {'*' * 18}")
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")
print(f'{"*" * 48}')
input_op = int(input("Escolha uma opção: "))

if input_op == 1:
    media_pond = (number_1 * 2) + (number_2 * 3) / 5
    print(f'A média ponderada dos números é: {media_pond}')
elif input_op == 2:
    print(f"Quadrado da soma dos 2 números é: {pow(number_1 + number_2, 2)}")
elif input_op == 3:
    if number_1 > number_2:
        cubo_1 = pow(number_2, 3)
        print(f'O cubo do menor número é: {cubo_1}')
    else:
        cubo_2 = pow(number_1, 3)
        print(f'O cubo do menor número é: {cubo_2}')
else:
    print("Número inválido.") """

""" # Exercicio Proposto 4

login_user_1     = "procopio"
login_password_1 = "12345"

login_user_2     = "paiva"
login_password_2 = "54321"

user_input     = input("Digite seu usuário: ")
password_input = input("Digite sua senha: ") 

verify_1 = user_input == login_user_1 and password_input == login_password_1
verify_2 = user_input == login_user_2 and password_input == login_password_2

if verify_1 or verify_2:
    print("Seja bem vindo")
else:
    print("Usuário ou senha não conferem") """

""" # Exercicio Proposto #5

# Cargo             |       Porcentabem de aumento
programador_sistema = 0.3
analista_sistema    = 0.2
analista_db         = 0.15

print("************ Cargos ***********")
print("1. Programador de sistema")
print("2. Analista de sistema")
print("3. Analista de banco de dados")

cargo_user    = input("Qual é o seu cargo? ")
salario_atual = float(input("Digite seu salário atual: "))

# Verificações:

verify_programador_sistema = cargo_user == "1"  #"programador de sistema"
verify_analista_sitema     = cargo_user == "2"  #"analista de sistema"
verify_analista_db         = cargo_user == "3"  #"analista de banco de dados"

# Contas e if's

if verify_programador_sistema:
    conta_programador_sistema = salario_atual * programador_sistema + salario_atual
    print(f"O seu salário atual após o aumento é R$: {conta_programador_sistema}")
elif verify_analista_sitema:
    conta_analista_sitema = salario_atual * analista_sistema + salario_atual
    print(f"O seu salário atual após o aumento é R$: {conta_analista_sitema}")
elif verify_analista_db:
    conta_analista_db = salario_atual * analista_db + salario_atual
    print(f"O seu salário atual após o aumento é R$: {conta_analista_db}")
else:
    print(f"Não foi possivel encontrar um cargo com esse número digitado: {cargo_user}")
 """

""" 
# Exercicio Proposto #6

sobrenome_1 = "araujo"
sobrenome_2 = "pinheiro"
sobrenome_3 = "bonner"
sobrenome_4 = "vasconcelos"

input_name = input("Digite o SOBRENOME de um apresentador: ").lower()

verify_1_2 = input_name == sobrenome_1 or input_name == sobrenome_2
verify_3_4 = input_name == sobrenome_3 or input_name == sobrenome_4


if verify_1_2:
    print("Bom Dia Nação, apresentado por Zé PINHEIRO e por Ana Carla ARAÚJO")
elif verify_3_4:
    print("Jornal Brasileiro, apresentado por Bill BONNER e Carla VASCONCELOS")
else:
    print("Apresentador(a) desconhecido(a)") 
"""

""" 
# Exercicio proposto #9

valor_final     = float(input("Qual é o valor total da venda? "))

print("1. À vista ( Pix ou espécie )")
print("2. Cartão de Débito")
print("3. Cartão de credito ( Vencimento )")

forma_pagamento = int(input("Qual a forma de pagamento? "))

if forma_pagamento == 1:
    desconto_valor_1 = valor_final - ( valor_final * 0.15 ) 
    print(f"O desconto foi de 15%, e o valor final é: {desconto_valor_1}")
elif forma_pagamento == 2:
    desconto_valor_2 = valor_final - ( valor_final * 0.10 ) 
    print(f"O desconto foi de 10%, e o valor final é: {desconto_valor_2}")
elif forma_pagamento == 3:
    desconto_valor_3 = valor_final - ( valor_final * 0.05 ) 
    print(f"O desconto foi de 5%, e o valor final é: {desconto_valor_3}")
else:
    print(f"Não foi possivel encontrar essa forma de pagamento: {forma_pagamento}")
"""

""" 
# Exercicio Proposto #10

altura = float(input("Qual a sua altura? "))
peso = float(input("Qual é o seu peso? "))

calculo_imc = peso / altura ** 2 

if calculo_imc < 18.5:
    print(f"O seu imc atual é {calculo_imc:.2f}, e você está abaixo do peso")
elif calculo_imc > 18.5 and calculo_imc < 25:
    print(f"O seu imc atual é {calculo_imc:.2f}, e você está com peso normal")
elif calculo_imc > 25 and calculo_imc < 30:
    print(f'O seu imc atual é {calculo_imc:.2f}, e você está sobrepeso')
else:
    print(f"Cuidado! Seu imc atual é {calculo_imc:.2f} e você está com obesidade")
 """    