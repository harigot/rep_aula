
#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

p1 = 7
p2 = 7
pf = 7

nota = (((p1 + p2) / 2) + pf) / 2
print('Media do aluno:', nota)

if nota >= 7:
    print('Aprovado')
elif nota >= 5 and nota < 7:
    print('Recuperação')
elif nota < 5:
    print('Reprovado')
else:
    print('Erro')
    