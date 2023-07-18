# a_1 = ['A', 'B', 12, True, 'Hello', 1.23123123, 3.14]

# indices = 0
# for __a_1__ in a_1:
#     indices += 1
#     print(indices, __a_1__)

# # Outro método:
# print("-" * 26)

# index = range(len(a_1))

# for i in index:
#     print(i, a_1[i])

# nomes = [ 'Maria', 'Helena', 'Luiz' ]
# n_enumarate = enumerate(nomes)

# for i in n_enumarate:
#     print(i)

buy = []

while True:
    
    print("O que você deseja fazer? ")
    input_actions = int(input("[1] Inserir | [2] Apagar | [3] Listar | [4] Sair "))

    if input_actions == 1:
        insert_item = input("O que você deixa inserir? ")
        buy.append(insert_item)
        # print(buy) # Debug
        print("O item", insert_item, "foi colocado a sua lista")
        continue
    elif input_actions == 2:
        size_array = len(buy) >= 1
        if size_array:
            for a, b in enumerate(buy):
                print('N°', a, 'Item:', b)
            print(" ")
            print("Para apagar um item, você deve digitar o número dele")
            try:
                input_del = int(input("Digite o número do item que deseja apagar: "))
                del buy[input_del]
                print("Item removido com sucesso!")
            except ValueError:
                print("Erro: Digite um número válido.")
            except IndexError:
                print("Erro: O índice fornecido não existe na lista.")
            except Exception as e:
                print(f"Erro desconhecido: {e}. Comunique-se com o desenvolvedor.")
        else:
            print('Nenhum valor encontrado, por favor inserir um!')
            continue
        
    elif input_actions == 3:
        if len(buy) >= 1:
            for _, b in enumerate(buy):
                print('Item:', b)
        else:
            print("Nenhum item na lista foi encontrado, para fazer a listagem")
    elif input_actions == 4:
        break
    else:
        print("Número invalido. Tente novamente")
        continue


nomes = [ 'Maria', 'Helena', 'Luiz' ]

n1, n2, n3 = nomes # [ 'Maria', 'Helena', 'Luiz' ]

print(*nomes)