# Código para retornar os caracteres individuais de uma string que não são espaços em branco.
string = "Sítio do pica-pau amarelo \n 2023"
resultado = [char for char in string if not char.isspace()]
print(resultado)
input()

# Saída: ['S', 'í', 't', 'i', 'o', 'd', 'o', 'p', 'i', 'c', 'a', '-', 'p', 'a', 'u', 'a', 'm', 'a', 'r', 'e', 'l', 'o', '2', '0', '2', '3']
