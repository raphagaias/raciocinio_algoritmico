import random

# definição
def jogador(): # player
    jogador = input('Escolha pedra, papel ou tesoura!: ')
    while jogador not in ['pedra', 'tesoura', 'papel']:
        jogador = input('Jogada incorreta! Digite pedra, papel ou tesoura: ')
    return jogador
def pc(): # computador
    return random.choice(['pedra', 'papel', 'tesoura'])
def resultado(jogada1, jogada2): # resultado das jogadas
    if (jogada1 == jogada2):
        return 'Empate'
    elif (jogada1  == 'pedra' and jogada2 == 'tesoura') or (jogada1 == 'papel' and jogada2 == 'pedra') or (jogada1 == 'tesoura' and jogada2 == 'papel'):
        placarh['Jogador 1'] += 1 # adiciona 1 ao placar (player 1)
        placarc['Computador 1'] += 1 # adiciona 1 ao placar (computador 1)
        return 'Jogador 1 é o vencedor!'
    else:
        placarh['Jogador 2'] += 1 # adiciona 1 ao placar (player 2)
        placarh['Computador 1'] += 1  # adiciona 1 ao placar (computador player)
        placarc['Computador 2'] += 1 # adiciona 1 ao placar (computador 2)
        return 'Jogador 2 é o vencedor!'
# menu
print('----------| Joquempô |----------')
print('    Selecione uma modalidade:')
print()
print('Jogador x Jogador (1)')
print('Jogador x Computador (2)')
print('Computador x Computador (3)')
print('Sair do jogo (4)')
print()
print('Criado por Lucca, Rafael, Bruno e André')
entrada = int(input('>>> '))
# dicionarios (placar)
placarh = dict.fromkeys(['Jogador 1', 'Jogador 2', 'Computador 1'], 0) # placar player x player // player x computador
placarc = dict.fromkeys(['Computador 1', 'Computador 2'], 0) # placar computador x computador
total = 0 # total de partidas
continuar = 0
# jogo
while continuar != 'n':
    if entrada == 4: # sair do jogo
        break
    continuar = input('Deseja continuar? (s/n): ')
    if continuar == 's':
        total += 1
        if entrada == 1: # jogador x jogador
            print('Jogador 1:')
            jogada1 = jogador()
            print('Jogador 2:')
            jogada2 = jogador()
            print('Resultado: ', resultado(jogada1, jogada2))
        elif entrada == 2: # jogador x computador
            print('Jogador 1:')
            jogada1 = jogador()
            jogada2 = pc()
            print('Computador escolheu:', jogada2)
            print('Resultado: ', resultado(jogada1, jogada2))
        elif entrada == 3: # computador x computador
            jogada1 = pc()
            jogada2 = pc()
            print('Computador 1 escolheu:', jogada1)
            print('Computador 2 escolheu:', jogada2)
            print('Resultado: ', resultado(jogada1, jogada2))
        else:
            print('Opção inválida. Selecione uma das três opções.')
    elif continuar == 'n':
        break
    else:
        print('Erro! Digite um valor válido!')
        continue
# tirar os valores do dicionario
plJogador1 = placarh.get('Jogador 1')
plJogador2 = placarh.get('Jogador 2')
plJogador3 = placarh.get('Computador 1')
plComputador1 = placarc.get('Computador 1')
plComputador2 = placarc.get('Computador 2')
print('Obrigado por jogar! :)')
print('Feito por: Lucca, André, Bruno e Rafael')
print()
print('Total de rodadas: ' + str(total))
# placares finais
if entrada == 1:
    print('---| Placar |---')
    print('Jogador 1: ' + str(plJogador1), 'Jogador 2: ' + str(plJogador2))
    print('Empates: ', str(total - (plJogador1 + plJogador2)))
elif entrada == 2:
    print('---| Placar |---')
    print('Jogador: ' + str(plJogador1), 'Computador: ' + str(plJogador3))
    print('Empates: ', str(total - (plJogador1 + plJogador3)))
else:
    print('---| Placar |---')
    print('Computador 1: ' + str(plComputador1), 'Computador 2: ' + str(plComputador2))
    print('Empates: ', str(total - (plComputador1 + plComputador2)))