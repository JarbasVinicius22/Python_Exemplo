alunos = {"Jorge":8, 
          "Gregório":6, 
          "Cleber":4,
          "Wesley":10}


print("======================================================")
print("Lista de alunos e notas:")
print("\n")

for aluno, nota in alunos.items():
    if nota >=7:
        resultado = "\033[32mAprovado!\033[0m"
    elif nota >=5:
        resultado = "\033[33mRecuperação!\033[0m"
    elif nota<=4: 
        resultado="\033[31mReprovado!\033[0m"
    else:
        resultado = "\n"

    print(f"{aluno.capitalize()}: {nota} {resultado}")
    print("\n")


print("======================================================")