n_alunos = 10
n_notas = 4
i_aluno = 0
notas_alunos = []
while i_aluno < n_alunos:  # 10 vezes
    sum = 0
    i_nota = 0
    print("Aluno", i_aluno+1)
    while i_nota < n_notas:  # 4 vezes
        try:
            sum += float(input(f"nota {i_nota+1}" "digite uma nota: "))
            i_nota += 1
        except Exception as e:
            print("tente de novo")
    notas_alunos.append(sum/4)
    i_aluno += 1

print("Alunos acima da média:")
tem_aluno = False
for index, media in enumerate(notas_alunos):
    if media >= 7:
        print(f"Aluno {index+1} tem nota acima da média")
        tem_aluno = True

if not tem_aluno:
    print("Nenhum aluno tem nota acima da média")
