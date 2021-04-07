#9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
def converte_fehrenheit_celcius(a):
    c = 5 * ((a - 32) / 9)
    return c
def main():
    print('Converte Fahrenheit em Celcius.')
    f = int(input('Digite a temperatura em Fehrenheit: '))
    resultado = converte_fehrenheit_celcius(f)
    print(f'{f} graus Fehrenheit é igual a {resultado:.1f} graus Celcius')

if __name__ == '__main__':
    main()