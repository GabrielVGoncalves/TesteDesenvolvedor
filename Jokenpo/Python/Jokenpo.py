def jogar(jogador1, jogador2):

    opcao = ('pedra', 'papel', 'tesoura')

    empate = 'Empate'
    jogador1ganha = 'Jogador 1 ganhou'
    jogador2ganha = 'Jogador 2 ganhou'

    try:
        jogador1 = opcao[jogador1]
        jogador2 = opcao[jogador2]
    except IndexError:
        return 'opção invalida'

    else:
        if jogador1 == jogador2:
            return empate

        if jogador1 == 'pedra':
            if jogador2 == 'tesoura':
                return jogador1ganha
            return jogador2ganha

        elif jogador1 == 'papel':
            if jogador2 == 'pedra':
                return jogador1ganha
            return jogador2ganha

        elif jogador1 == 'tesoura':
            if jogador2 == 'papel':
                return jogador1ganha
            return jogador2ganha

