def imprimir_tabuleiro(tabuleiro):
    """Função para imprimir o tabuleiro de forma visualmente agradável."""
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador atual venceu.
    Verifica todas as 8 combinações de vitória (linhas, colunas, diagonais).
    """
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]            
    ]
    for comb in combinacoes_vitoria:
        if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] == jogador:
            return True
    return False

def jogar_jogo_da_velha():
    """Função principal que executa o jogo."""
    tabuleiro = [' ' for _ in range(9)]  
    jogador_atual = 'X'
    rodadas = 0

    print("---------------------------------")
    print("Bem-vindo ao Jogo da Velha!")
    print("Os jogadores são 'X' e 'O'.")
    print("Digite um número de 1 a 9 para fazer sua jogada.")
    print("---------------------------------")

    while True:
        imprimir_tabuleiro(tabuleiro)
        
        while True:
            try:
                jogada = int(input(f"Jogador '{jogador_atual}', escolha uma posição (1-9): "))
                posicao = jogada - 1
                
                if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                    tabuleiro[posicao] = jogador_atual
                    break
                else:
                    print("Posição inválida ou já ocupada. Por favor, tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Digite um número de 1 a 9.")

        rodadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"\nParabéns! O jogador '{jogador_atual}' venceu!")
            break
        
        if rodadas == 9:
            imprimir_tabuleiro(tabuleiro)
            print("\nEmpate! O tabuleiro está cheio.")
            break
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogar_jogo_da_velha()