import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]listar: ')
    
    if opcao == 'i':
        os.system('clear')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o indice para apagar: '
        )
        
        try:
            incide = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este indice')
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista) == 0:
            print('Nada para listar')
            
        for i, valor in enumerate(lista):
            print(i, valor)
        else:
            print('por favor, escolha i a ou l')
        

