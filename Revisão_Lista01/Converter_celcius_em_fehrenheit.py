#10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
def converte_celcius_fahrenheit(a):
    f = ((a * 1.8) + 32)
    return f
def main():
    print(f'Converte graus celcius em fehrenheit.')
    c = int(input('Digite a temperatura em graus Celcius: '))
    resultado = converte_celcius_fahrenheit(c)
    print(f'{c} graus Celcius são equivalentes a {resultado} graus Fahrenheit')

if __name__ == '__main__':
    main()