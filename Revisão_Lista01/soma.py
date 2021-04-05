#3.Faça um programa que peça dois números e imprima a soma.
def soma(a, b):
    total = a + b
    return total

def main():
    print('Os números serão somados.')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o Segundo número: '))
    resposta = soma(num1, num2)
    print(f'A soma desses dois números é igual a {resposta}')

if __name__ == '__main__':
    main()
