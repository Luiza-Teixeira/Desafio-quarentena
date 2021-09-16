nota_1 = float(input("Digite a nota da 1° prova:"))
nota_2 = float(input("Digite a nota da 2° prova:"))
nota_3 = float(input("Digite a nota da 3° prova:"))
mediaPonderada = ((nota_1 + nota_2 + (nota_3 * 2)) / 4)
if mediaPonderada >= 4:
    print("Aluno aprovado!!")
else:
    print("Aluno reprovado!")
