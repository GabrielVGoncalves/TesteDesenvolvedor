import unittest


from Jokenpo import JogoJokenpo


class JokenpoTest(unittest.TestCase):

    def setUp(self):
        player1 = ('pedra', 'papel', 'tesoura')
        player2 = ('pedra', 'papel', 'tesoura')
        self.Jogo = JogoJokenpo(player1, player2)

    def tearDown(self):
        pass

    def test_retorna_empate(self):
        self.assertEqual('EMPATE', self.Jogo.return_resultado(0, 0))
        self.assertEqual('EMPATE', self.Jogo.return_resultado(1, 1))
        self.assertEqual('EMPATE', self.Jogo.return_resultado(2, 2))

    def test_player1_ganha(self):
        self.assertEqual('player1 ganhou', self.Jogo.return_resultado(0, 2))
        self.assertEqual('player1 ganhou', self.Jogo.return_resultado(1, 0))
        self.assertEqual('player1 ganhou', self.Jogo.return_resultado(2, 1))

    def test_player2_ganha(self):
        self.assertEqual('player2 ganhou', self.Jogo.return_resultado(2, 0))
        self.assertEqual('player2 ganhou', self.Jogo.return_resultado(0, 1))
        self.assertEqual('player2 ganhou', self.Jogo.return_resultado(1, 2))

    def test_opcao_invalida(self):
        self.assertRaises('opção inválida')
