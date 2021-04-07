#7.Faça um programa que calcula a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def area(a):
    m = a * a
    m = m * 2
    return  m

def main():
    print('Mostra a área de um quadrado.')
    a = float(input('Digite o tamanho do lado ou base do quadrado em cm: '))
    resultado = area(a)
    print(f'O dobro desta área é igual a {resultado} cm2')

if __name__ == '__main__':
    main()
