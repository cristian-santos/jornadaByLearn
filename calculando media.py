nome = input('Digite seu nome do aluno: ')

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota  = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota :'))

media = (primeira_nota + segunda_nota + terceira_nota)/3

if media >= 6:
    print(f'{nome} foi aprovado com média {media:.2f}')
else:
    print(f'{nome} foi reprovado com a média {media:.2f}')
