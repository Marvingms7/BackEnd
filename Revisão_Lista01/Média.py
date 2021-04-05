#4.Faça um programa que mostra as 4 notas bimetrais e mostre a média.
def media(a, b, c, d):
    med = (a + b + c + d) / 4
    return med
def main():
    print('Digite as 4 notas bimetrais para saber a sua média: ')
    n1 = float(input('Primeira nota:'))
    n2 = float(input('Segunda nota: '))
    n3 = float(input('Terceira nota: '))
    n4 = float(input('Quarta nota: '))
    resultado = media(n1, n2, n3, n4)
    print(f'A média sua média é igual a {resultado:.1f}')

if __name__ == '__main__':
    main()