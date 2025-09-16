import funcoes as f
print('Esse Programa foi desenvolvido como forma de aprendizado!')
print('Nele o usuario deve fornecer alguns números e o programa irá somar eles')
print('Exemplo: 54, será feita soma de 5 + 4, resultando 9.')
def main():
    soma = input('Digite alguns números: ')
    if soma.isdigit() and f.numeros_digitos(soma) == True:
        print(f'Números: {soma}\nResultado: {f.soma_digitos(soma)}')
    else : 
        print('Forneça valores validos!')
        print('O Programa deve receber apenas números e ao menos dois digitos!')
main()