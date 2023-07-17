""" 
Laços de repetição [ While, For ]
é usado estruturas conhecidas como iteração
"""

# Programa 30 - Imprimir 4k de saudações com While.

""" 
count = 1
while count <= 10:
  print(f'Olá {count}')
  count += 1
print("Fim do while") 
"""

#while <condição (ou um conjunto delas) for verdadeira>:
  #Instruções a serem executadas
  #Instruções a serem executadas após o encerramento do loop

# Programa 34 - Soma 10 números usando While

"""  
soma = 0
termo = 1
while termo <= 10:
  soma += termo
  termo += 1
print(soma)
"""

"""  
Função range()
Ele gera uma sequencia de números dentro de uma faixa.
A sequencia sempre vai começar por 0 | IMPORTANTE

range(<quantidade_de_números_a_serem_gerados>)
range(<início_da_faixa>, <fim_da_faixa>[,<step>])

"""

# print(list(range(3)))

"""  

 # Estrutura FOR
 for <variável> in range([maneira_1|maneira_2]):
    #Instruções a serem executadas
 #Instruções a serem executadas após o fim do loop

"""

""" 
# Programa 30 em for

for count in range(1, 11): # Vai começar no 1 e vai parar no 10
  print(f"Olá in for {count}")
print("Fim do for")

for count in range(1, 11, 2): # Vai começar no 1 e vai parar no 10, pulando de 2 em 2
  print(f"Olá in for {count}")
print("Fim do for")
"""

""" text = 'Joao'
iter = iter(text)

for i in text:
    print(i)
    
print(" ")

while True:
    try:
        print(next(iter))
    except StopIteration:
        break
"""
""" 
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    if i == 5:
        print('i é 5, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executara')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!') """

import os

palava_secreta = 'perfume'
letras_corretas = ''
n_tentaivas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    n_tentaivas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palava_secreta:
        letras_corretas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palava_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)


    if palavra_formada == palava_secreta:
        os.system('clear')
        print("Parabens, você acertou a palavra secreta! A palavra era: ", palava_secreta)
        print("Tentativas: ", n_tentaivas)
        letras_corretas = ''
        n_tentaivas = 0