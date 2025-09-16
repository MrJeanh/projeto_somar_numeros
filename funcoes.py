def soma_digitos(numero: int):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma

def numeros_digitos(texto):
    total_digitos = sum(numero.isdigit() for numero in texto)
    return total_digitos >= 2
