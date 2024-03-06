nome = input('informe seu nome: ')
idade = input('informe sua idade: ')

if nome and idade:
    print(f'seu nom e {nome}')
    print(f'seu nome invertido é {nome [::-1]}')
    if ' in nome':
        print('seu nome contem espaços')   
    else:
        print('seu nome Não contem espaços')
    
    print(f'seu nome tem {len(nome)}')    
    print(f'A primeira letra do seu nom e {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
  