jogador = dict()
partida = dict()
gols = list()
cont = 0
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
if jogador['partidas'] != 0:
    partida = (jogador['partidas'])
for p in range(0, partida):
    cont += 1
    part = str(input('Quantos gols fez na {}° partida? '.format(cont)))
    gols.append(part[:])
    jogador['gols'] = gols
print('=-' * 20)
print(jogador)
print('=-' * 20)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor: {v}')
print('=-' * 20)
print('O jogador {} jogou {} partidas'.format(jogador['nome'], partida))
for k, v in enumerate (gols):
    print(f'  =>  No {k+1}° jogo {jogador["nome"]} fez {v} gols')
print('=-' * 20)