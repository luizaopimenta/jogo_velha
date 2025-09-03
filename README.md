-----

# Jogo da Velha em Python

Este é um jogo da velha simples desenvolvido em Python. O objetivo do projeto é demonstrar a lógica de jogo, a interação com o usuário e a verificação de condições de vitória e empate.

## Funcionalidades

  * **Tabuleiro Dinâmico**: O jogo exibe o tabuleiro atualizado a cada jogada.
  * **Dois Jogadores**: Permite que dois jogadores (X e O) se alternem.
  * **Verificação de Vitória**: O jogo detecta automaticamente se um jogador venceu em qualquer linha, coluna ou diagonal.
  * **Verificação de Empate**: O jogo reconhece quando o tabuleiro está cheio e o resultado é um empate.
  * **Validação de Jogada**: O programa impede que um jogador faça uma jogada em uma posição já ocupada.

## Como Jogar

1.  **Pré-requisitos**: Certifique-se de que você tem o **Python** instalado em sua máquina.

2.  **Executar o Jogo**: Abra o terminal, navegue até a pasta do projeto e execute o seguinte comando:

    ```bash
    python jogo_da_velha.py
    ```

      * *Ajuste o nome do arquivo se necessário, caso ele seja diferente de `jogo_da_velha.py`.*

3.  **Fazer uma Jogada**: Digite o número da posição em que você deseja jogar (de 1 a 9) e pressione `Enter`.

### Layout do Tabuleiro

O jogo usa uma representação numérica para as posições do tabuleiro, como mostrado abaixo:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## Estrutura do Código

O código é organizado em funções para facilitar a leitura e manutenção:

  * `imprimir_tabuleiro()`: Exibe o tabuleiro atual na tela.
  * `verificar_vitoria(jogador)`: Checa se o jogador atual venceu.
  * `verificar_empate()`: Checa se o jogo terminou em empate.
  * `fazer_jogada(jogador)`: Gerencia a jogada do jogador, garantindo que a posição escolhida seja válida.
  * `jogo_da_velha()`: A função principal que orquestra o fluxo do jogo, alternando entre os jogadores e verificando as condições de vitória ou empate a cada turno.

## Tecnologias Usadas

  * **Python**

-----

**Autor:** [Luiz Fernando Pimenta Costa]
