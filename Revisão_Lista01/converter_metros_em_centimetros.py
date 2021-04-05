#5.Faça um programa que converta metros em centímetros.
def converter(a):
    cent = a * 100
    return cent
def main():
    print('Converte metros em centímetros')
    n = float(input('Digite a quantidade em metros: '))
    resultado = converter(n)
    print(f'{n} metros são equivalentes á {resultado:.1f} centímetros')

if __name__ == '__main__':
    main()