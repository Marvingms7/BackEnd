#11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a)o produto do dobro do primeiro com metade do segundo.
# b)a soma do triplo do primeiro com o terceiro.
# c)o terceiro elevado ao cubo.
def calculaproduto(a, b):
    total = (a*2) + (b / 2)
    return total
def calculatriplo(a, b):
    total = (a*3) + (b / 2)
    return total
def calculacubo(a):
    total = a ** 3
    return total
def main():
    n1 = int(input('Digite o primeiro número inteiro:'))
    n2 = int(input('Digite o segundo número inteiro: '))
    n3 = float(input('Digite um número real: '))
    resultado1 = calculaproduto(n1, n2)
    resultado2 = calculatriplo(n1, n3)
    resultado3 = calculacubo(n3)
    print(f'O produto do dobro do primeiro número com metade do segundo é igual a {resultado1}\nA soma do triplo do primeiro com metade do terceiro é igual a {resultado2}\nO terceiro elevado ao cubo é igual a {resultado3}')

if __name__ == '__main__':
    main()

