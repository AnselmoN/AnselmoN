def arrumar_nome(nome, sobrenome):
    nome_formatado = nome.capitalize()  # Coloca a primeira letra do nome em maiúscula
    sobrenome_formatado = sobrenome.capitalize()  # Coloca a primeira letra do sobrenome em maiúscula

    nome_completo = f'{nome_formatado} {sobrenome_formatado}'  # Concatena as duas strings com um espaço entre elas
    return nome_completo

umnome = input("Digite seu Nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = arrumar_nome(umnome, sobrenome)
print(f'O seu nome é: {nome_completo}')
