'''
def aumento_salarial(salario, percentual):
    novo_salario = salario*percentual/100 + salario
    return novo_salario


salario_Fulano = aumento_salarial(2000,10)
print(salario_Fulano)
'''

def aumento_salarial(salario=5000, percentual=100):
    novo_salario = salario*percentual/100 + salario
    return novo_salario


salario_Fulano = aumento_salarial()
print(salario_Fulano)