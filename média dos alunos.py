print('Este programa irá calcular a média dos alunos.')
aluno = input('Qual o nome do(a) aluno(a)? ')
print('Primeiro semestre')
prova1 = float(input('Qual o nota de {} na primeira prova? '.format(aluno)))
prova2 = float(input('Qual a nota de {} na segunda prova? '.format(aluno)))
nota_final_1 = prova1 + prova2
print('A nota final do primeiro semestre foi de: {:.1f}'.format(nota_final_1))
print('Segundo semestre')
prova3 = float(input('Qual o nota de {} na primeira prova? '.format(aluno)))
prova4 = float(input('Qual a nota de {} na segunda prova? '.format(aluno)))
nota_final_2 = prova3 + prova4
print('A nota final do segundo semestre foi de: {:.1f}'.format(nota_final_2))
print('Terceiro semestre')
prova5 = float(input('Qual o nota de {} na primeira prova? '.format(aluno)))
prova6 = float(input('Qual a nota de {} na segunda prova? '.format(aluno)))
nota_final_3 = prova5 + prova6
print('A nota final do terceiro semestre foi de: {:.1f}'.format(nota_final_3))
media = (nota_final_1 + nota_final_2 + nota_final_3) / 3
print('Média final')
print('A média final de {} é {:.1f}'.format(aluno, media))
