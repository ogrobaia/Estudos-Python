
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]listar')
    
    if opcao == 'i':
        os.sistem('clear')
        valor = input('Valor:')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o indice para apagar'
        )
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite numero in.')
        except IndexError:
            print('Indice nao existe na lista')
        except Exception:
            print('Erro desconhecido')
                          
    elif opcao == 'l':
        os.sistem('clear')
        
        if len(lista) == 0:
            print('Nada para listar')
            
        for i, valor in enumerate(lista):
            print(i,valor)
    
    else:
        print('Por favor escolha i, a ou l.')
        
        