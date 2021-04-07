#13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas.
#a) Para homens: (72.7*h) - 58.
#b) Para mulheres: (62.1*h) - 44.7.
def calculapeso(a):
    total = (72.7 * a) - 58
    return total

def calculapeso2(a):
    total = (62.1 * a) - 44.7
    return total

def main():
    h = str(input('Digite qual o seu sexo usando apenas [M] para masculino ou [F] para feminino: ')).upper()
    if h == 'M':
        m = float(input('Digite sua altura: '))
        resultado = calculapeso(m)
        print(f'Seu peso ideal deve ser {resultado}')
    elif h == 'F':
            f = float(input('Digite sua altura: '))
            resultado2 = calculapeso2(f)
            print(f'Seu peso ideal deve ser {resultado2}')
    else:
        if h != 'M' or h != 'F':
            print(f'Você não digitou [M] ou [F]')


if __name__ == '__main__':
    main()