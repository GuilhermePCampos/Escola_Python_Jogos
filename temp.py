professor = "Guilherme"
aluno1 = "João"
aluno2 = "Maria"


def funcao1(texto):
    print("[" + texto + "]")


funcao1(professor)
funcao1(aluno1)
funcao1(aluno2)
funcao1("aluno2")
funcao1("Professor " + professor)


def CalcArea(largura, comprimento):
    area = largura * comprimento
    print("A area do quadrilatero é:", area)


CalcArea(2, 3)
# CalcArea(3)
CalcArea(4, 7)
CalcArea(2, "2")

# def funcao3(parametro):
#     if int(parametro) > 0:
#         print("Número positivo", parametro)
#     elif (int(parametro) < 0):
#         print("Número negativo", parametro)
#     else:
#         print("Número zero", parametro)


# funcao3(10)
# funcao3(5 - 8)
# funcao3()
# funcao3(0)
# funcao3("5")
# funcao3(-2 + 2 * 2)


# def funcao4(valor, valor2):
#     while (valor <= valor2):
#         print(valor, end=", ")
#         valor += 1
#         if (valor == valor2 - 3):
#           break
#     print(valor2)


# funcao4(1, 10)
# funcao4(6, 10)
# funcao4(10, 1)
# funcao4(5, 15)
