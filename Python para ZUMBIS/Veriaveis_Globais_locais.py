josé = "entrou 6h"  # VARIAVEL GLOBAL


def fatec():
    global josé  # VARIAVEL GLOBAL INSERIDA DENTRO DA FUNÇÃO
    josé = "entrou 8h"  # VARIVEL LOCAL DENTRO DO DEF( FUNÇÃO )
    print(josé)


print(josé)
fatec()
print(josé)
