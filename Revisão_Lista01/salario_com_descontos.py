#15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a)salário bruto.
# b)quanto pagou ao INSS.
# c)quanto pagou ao sindicato.
# d)o salário líquido.

def salariobruto(a, b):
    total = a * b
    return total

def imposto(a):
    total = (11 * a) / 100
    return total

def inss(a):
    total = (8 * a) / 100
    return total

def sindicato(a):
    total = (5 * a) / 100
    return total

def liquido(a, b, c, d):
    total = a - b - c - d
    return total
def main():
    n = float(input('Digite quanto você ganha por hora trabalhada: '))
    n2 = float(input('Digite o número de horas trabalhadas no mês: '))
    salariobruto1 = salariobruto(n, n2)
    imposto1 = imposto(salariobruto1)
    inss1 = inss(salariobruto1)
    sindicato1 = sindicato(salariobruto1)
    liquido1 = liquido(salariobruto1, imposto1, inss1, sindicato1)
    print(f'+ Salário Bruto : R${salariobruto1}\n- IR (11%) : R${imposto1}\n- INSS (8%) : R${inss1}\n- Sindicato (5%) : R${sindicato1}\n= Salário Liquido : R${liquido1}')

if __name__ == '__main__':
    main()