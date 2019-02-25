from unittest import TestCase
from Jokenpo import jogar


class TestesJokenpo(TestCase):

    def test_retorna_empate(self):
        self.assertEqual("Empate", jogar(0, 0))
        self.assertEqual("Empate", jogar(1, 1))
        self.assertEqual("Empate", jogar(2, 2))

    def teste_jogador1_ganha(self):
        self.assertEqual("Jogador 1 ganhou", jogar(0, 2))
        self.assertEqual("Jogador 1 ganhou", jogar(1, 0))
        self.assertEqual("Jogador 1 ganhou", jogar(2, 1))

    def teste_jogador2_ganha(self):
        self.assertEqual("Jogador 2 ganhou", jogar(2, 0))
        self.assertEqual("Jogador 2 ganhou", jogar(0, 1))
        self.assertEqual("Jogador 2 ganhou", jogar(1, 2))

    def teste_opcao_invalida(self):
        self.assertEqual("opção invalida", jogar(1, 4))
