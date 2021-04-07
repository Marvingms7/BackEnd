#12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def calculapeso(a):
    total = (72.7 * a) - 58
    return total
def main():
    a = float(input('Digite sua altura: '))
    resultado = calculapeso(a)
    print(f'Seu peso ideal deve ser {resultado:.2f} kgs')

if __name__ == '__main__':
    main()