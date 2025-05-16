def average(turma: dict[str, int]) -> float:
    '''Calcula a media das notas de uma turma informada'''
    if not turma or not isinstance(turma, dict):
        return 0.0
    total_notas = sum(turma.values())
    qtd_alunos = len(turma)
    media = total_notas / qtd_alunos
    return media

# from help_your_professor import average
# class_3B = {"marine": 18,"jean": 15,"coline": 8,"luc": 9}
# class_3C = {"quentin": 17,"julie": 15,"marc": 8,"stephanie": 13}
# print(f"Average for class 3B: {average(class_3B)}.")
# print(f"Average for class 3C: {average(class_3C)}.")