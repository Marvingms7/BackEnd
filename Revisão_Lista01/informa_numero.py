#2.Faça um programa que peça um número e então mostre a mensagem "O número informado foi [número]".
def main():
    n = int(input('Informe um número para ser mostrado na tela: '))
    print(f'O número informado foi {n}')

if __name__ == '__main__':
    main()