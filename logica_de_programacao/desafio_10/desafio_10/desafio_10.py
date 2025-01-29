"""Calcula a média do aluno até que seja solicitado encerramento"""

repeat = True

while repeat:

    grade_a = None
    grade_b = None


    while grade_a is None:
        try:
            grade_a = float(input ("Digite a nota 1: "))

        except ValueError:
            print('Por favor, digite uma nota válida')

        if grade_a < 0 or grade_a > 10:
            print('Por favor, digite uma nota entre 0 e 10')
            grade_a = None


    while grade_b is None:
        try:
            grade_b = float(input ("Digite a nota 2: "))

        except ValueError:
            print('Por favor, digite uma nota válida')
            grade_b = None

        if grade_b < 0 or grade_b > 10:
            print('Por favor, digite uma nota entre 0 e 10')

    average_grade = (grade_a + grade_b) / 2

    if average_grade >= 7:
        print(f"Você está aprovado com a média {average_grade}")
    else:
        print(f"Você está reprovado com a média {average_grade}")


    loop = input("Deseja continuar? (S/N): ")

    if loop in ('n','N'):
        repeat = False
