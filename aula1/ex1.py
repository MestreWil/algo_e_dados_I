nome_produto = ['Iphone', 'IMAC', 'EARPODS']
preco_produto = ['7999,00', '15799,99', '399,96']
qtde_produto = ['4', '5', '9']

#função para adicionar num produto nas listas
'''def adiciona_produto():
    nome = str(input('Digite o nome do Produto:'))
    preco = float(input('Digite o preço do Produto: '))
    qtde = int('Digite a quantidade do Produto: ')
    nome_produto.append(nome)
    preco_produto.append(preco)
    qtde_produto.append(qtde)
    return 'Produto Adicionado as Listas. '''

def apagar_produto():
    num_produto = int(input(f'Digite o número entre 0 e {len(nome_produto)-1}: '))
    if num_produto > len(nome_produto) or num_produto < 0:
        print('Produto inexistente.')
    else:
        nome_produto.pop(num_produto)
        preco_produto.pop(num_produto)
        qtde_produto.pop(num_produto)

def printar_produto():
    num_produto = int(input(f'Digite o número entre 0 e {len(nome_produto) - 1}: '))
    if num_produto > len(nome_produto) or num_produto < 0:
        print('Produto inexistente.')
    else:
        print(f'Nome Produto: {nome_produto[num_produto]}\nPreço do Produto: {preco_produto[num_produto]}\nQuantidade Produto: {qtde_produto[num_produto]}')
    
def menu():
    while True:
        menu = int(input('Digite uma das opções: \n0 - Sair\n1 - Apagar Produto\n2 - Printar Produto\n'))
        if menu == 0:
            print('Obrgado Volte sempre.')
            break
        elif menu == 1:
            apagar_produto()
        elif menu == 2:
            printar_produto()
        else:
            print('Não tem essa opção.')

menu()