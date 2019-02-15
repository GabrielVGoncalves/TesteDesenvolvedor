class JogoJokenpo:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def return_papel(self, pos_player1):
        return self.player1[pos_player1]

    def return_resultado(self, pos_player1, pos_player2):
        result = ''
        if self.player1[pos_player1] in self.player1 and self.player2[pos_player2] in self.player2:
            if pos_player1 == 0:
                if pos_player2 == 0:
                    result = 'EMPATE'
                elif pos_player2 == 1:
                    result = 'player2 ganhou'
                else:
                    result = 'player1 ganhou'
            elif pos_player1 == 1:
                if pos_player2 == 0:
                    result = 'player1 ganhou'
                elif pos_player2 == 1:
                    result = 'EMPATE'
                else:
                    result = 'player2 ganhou'
            elif pos_player1 == 2:
                if pos_player2 == 0:
                    result = 'player2 ganhou'
                elif pos_player2 == 1:
                    result = 'player1 ganhou'
                else:
                    result = 'EMPATE'
        else:
            result = 'opção inválida'
        return result
