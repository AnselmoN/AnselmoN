def converte(valor):
    real = valor * 4.92
    return real


dolar = float(input('digite dolar:'))
numero = converte(dolar)
print(f'seu valor: {dolar} significa R$ {numero}')