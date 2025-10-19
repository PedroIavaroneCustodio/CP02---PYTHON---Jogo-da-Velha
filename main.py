# CP02 - PYTHON - Jogo da Velha

def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
    print("\n")


def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        # Linhas
        if all([celula == jogador for celula in tabuleiro[i]]):
            return True
        # Colunas
        if all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    # Diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]):
        return True
    if all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


def jogada_valida(tabuleiro, linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False
    if tabuleiro[linha][coluna] != " ":
        return False
    return True


def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Escolha de símbolo
    jogador1 = input("Jogador 1, você quer ser X ou O? ").upper()
    while jogador1 not in ["X", "O"]:
        jogador1 = input("Escolha inválida. Digite X ou O: ").upper()

    jogador2 = "O" if jogador1 == "X" else "X"
    print(f"Jogador 1 é {jogador1} e Jogador 2 é {jogador2}.\n")

    jogador_atual = jogador1
    nome_jogador = "Jogador 1"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"{nome_jogador} ({jogador_atual}), é sua vez!")

        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Entrada inválida! Digite números entre 0 e 2.")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida! Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        # Verifica vencedor
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"🎉 {nome_jogador} ({jogador_atual}) venceu! 🎉")
            break

        # Verifica empate
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("😐 O jogo empatou!")
            break

        # Alterna jogador
        if jogador_atual == jogador1:
            jogador_atual = jogador2
            nome_jogador = "Jogador 2"
        else:
            jogador_atual = jogador1
            nome_jogador = "Jogador 1"


if __name__ == "__main__":
    jogar()
