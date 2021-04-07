#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def calcula_salario(a, b):
    t = a * b
    return t

def main():
    print(f'Mostra quanto você recebe por mês, ganhando por hora trabalhada.')
    h = float(input('Digite quanto você ganha por hora trabalhada: '))
    m = float(input('Digite quantas horas você trabalha por mês: '))
    resultado = calcula_salario(h, m)
    print(f'O seu salário nesse mês é referente a R${resultado}')

if __name__ == '__main__':
    main()
