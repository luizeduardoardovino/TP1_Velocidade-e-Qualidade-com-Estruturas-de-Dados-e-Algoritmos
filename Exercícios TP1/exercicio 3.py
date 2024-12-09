
array = [2, 4, 6, 8, 10, 12, 13]


numero = 8


passos = 0
for i in array:
    passos += 1
    if i == numero:
        break


print(passos)

# Saída: 4
# Para encontrar o número 8, foram necessários 4 passos na busca linear.
