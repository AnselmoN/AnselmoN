def arrumar_nome(umnome, sobrenome):
    letra1 = umnome[0]
    resto = umnome[1:]
    letra1 = letra1.upper()
    resto = resto.lower()
    umnome = letra1 + resto
    letra2 = sobrenome[0]
    resto = sobrenome[1:]
    letra2 = letra2.upper()
    resto = resto.lower()
    sobrenome = letra2 + resto
    nome_completo = f'{umnome} {sobrenome}'  
    return nome_completo

umnome = input("Digite seu Nome: ")
sobrenome = input(" Digite seu Sobrenome:")
nome_completo = arrumar_nome(umnome, sobrenome)
print(f'O seu nome é: {nome_completo}')


