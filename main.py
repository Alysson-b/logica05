alunos = int(input('Digite o numero de alunos:'))

soma_da_turma = 0
aprovados = 0
reprovados = 0

for i in range(alunos):

    nome = input(f'\nDigite o nome do aluno {i + 1}:')

    nota1 = float(input(f'Digite a primeira nota de {nome}: '))
    nota2 = float(input(f'Digite a segunda nota de {nome}: '))
    nota3 = float(input(f'Digite a terceira nota de {nome}: '))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        status = 'aprovado'
        aprovados += 1
    else:
        status = 'reprovado'
        reprovados += 1

    print(f'aluno: {nome}')
    print(f'notas: {nota1}, {nota2}, {nota3}')
    print(f'media: {media:.2f} - {status}')

    soma_da_turma += media

media_geral = soma_da_turma / alunos

print(f'a media geral da turma: {media_geral:.2f}')
print(f'alunos aprovados: {aprovados}')
print(f'alunos reprovados: {reprovados}')