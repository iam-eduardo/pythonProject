# Definindo a classe TicTacToe
class TicTacToe:
    # Método construtor da classe
    def __init__(self):
        # Inicializando o tabuleiro como uma lista 4x4 de espaços vazios
        self.board = [[' ' for _ in range(4)] for _ in range(4)]
        # Definindo o jogador atual como 'X'
        self.current_player = 'X'

    # Método para imprimir o tabuleiro
    def print_board(self):
        # Para cada linha no tabuleiro
        for row in self.board:
            # Imprime a linha unindo cada elemento com '|'
            print('|'.join(row))
            # Imprime uma linha de separação
            print('-' * 7)

    # Método para verificar se uma jogada é válida
    def is_valid_move(self, row, col):
        # Se a linha ou a coluna estão fora do tabuleiro, retorna False
        if row < 0 or row > 3 or col < 0 or col > 3:
            return False
        # Se a posição já está ocupada, retorna False
        if self.board[row][col] != ' ':
            return False
        # Se passou pelas verificações, retorna True
        return True

    # Método para fazer uma jogada
    def make_move(self, row, col):
        # Se a jogada é válida
        if self.is_valid_move(row, col):
            # Coloca o símbolo do jogador atual na posição
            self.board[row][col] = self.current_player
            # Alterna o jogador atual
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            # Se a jogada não é válida, imprime uma mensagem de erro
            print("Invalid move. Try again.")

    # Método para verificar se algum jogador ganhou
    def check_win(self):
        # Para cada linha no tabuleiro
        for row in self.board:
            # Se a linha tem 4 'X' ou 4 'O', retorna True
            if row.count('X') == 4 or row.count('O') == 4:
                return True
        # Para cada coluna no tabuleiro
        for col in range(4):
            # Se a coluna tem 4 'X' ou 4 'O', retorna True
            if [row[col] for row in self.board].count('X') == 4 or [row[col] for row in self.board].count('O') == 4:
                return True
        # Verifica as diagonais
        if [self.board[i][i] for i in range(4)].count('X') == 4 or [self.board[i][i] for i in range(4)].count('O') == 4:
            return True
        if [self.board[i][3 - i] for i in range(4)].count('X') == 4 or [self.board[i][3 - i] for i in range(4)].count(
                'O') == 4:
            return True
        # Se passou por todas as verificações e ninguém ganhou, retorna False
        return False

    # Método para verificar se o jogo empatou
    def check_draw(self):
        # Para cada linha no tabuleiro
        for row in self.board:
            # Se a linha tem algum espaço vazio, retorna False
            if ' ' in row:
                return False
        # Se passou por todas as verificações e não tem espaços vazios, retorna True
        return True

    # Método para jogar o jogo
    def play(self):
        # Enquanto o jogo não terminar
        while True:
            # Imprime o tabuleiro
            self.print_board()
            # Pede ao jogador atual para escolher uma linha
            while True:
                try:
                    row = int(input("Enter row for player " + self.current_player + ": "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            # Pede ao jogador atual para escolher uma coluna
            while True:
                try:
                    col = int(input("Enter column for player " + self.current_player + ": "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            # Faz a jogada
            self.make_move(row, col)
            # Se algum jogador ganhou
            if self.check_win():
                # Imprime uma mensagem de vitória e termina o jogo
                print("Player " + ('O' if self.current_player == 'X' else 'X') + " wins!")
                break
            # Se o jogo empatou
            elif self.check_draw():
                # Imprime uma mensagem de empate e termina o jogo
                print("It's a draw!")
                break


# Se o arquivo atual está sendo executado diretamente
if __name__ == "__main__":
    # Cria uma nova instância do jogo Tic Tac Toe
    game = TicTacToe()
    # Inicia o jogo
    game.play()
