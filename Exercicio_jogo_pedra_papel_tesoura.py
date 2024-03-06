from random import choice

jogador_vitorias = 0
maq_vitorias = 0


def opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção inválida. Tente Novamente")
        opcao_jogador()


def opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:

    print("-"*30)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("-"*30)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura")\
        or (esc_jogador == "papel") and (esc_maquina == "pedra")\
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        # jogador ganha
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu{esc_maquina} "
              " Resultado: Você Ganhou!")
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        # empate
        print(
            f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} ")
    else:
        # Maquina Ganha
        print(f"jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} "
              "Resultado: Você Perdeu")
        maq_vitorias += 1

    print("-"*30)
    print(f"Vitorias do Jogador: {jogador_vitorias}")
    print(f"Vitorias do Jogador: {maq_vitorias}")
    print("-"*30)

    esc_jogador = input("Você quer jogar novamente? ")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "n", "N"]:
        break
    else:
        break
