jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c} ?')))
jogador['gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
