"""
#if / elif /else
#se / se nao se / se nao

entrada = input('Voce quer "entrar" ou "Sair"? ')


if entrada == 'entrada':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')
    
"""
#Entendendo o Fluxo do Interpretador 
#

condicao1 = False
condicao2 = False
condicao3 = True     # somente esta condição sera checada , as demais abaixo ão serão
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Codigo para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')    
