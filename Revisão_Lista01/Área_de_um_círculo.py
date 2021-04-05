#6.Faça um programa que peça o raio de um círculo , calcule e mostre a área.
def area(a):
    PI = 3.14
    raio = a
    ar = (raio**2) * PI
    return ar

def main():
    print('Mostra a área de um circulo.')
    raio = float(input('Digite o raio: '))
    resultado = area(raio)
    print(f'A área do circulo é igual á {resultado} cm2')

if __name__ == '__main__':
    main()
