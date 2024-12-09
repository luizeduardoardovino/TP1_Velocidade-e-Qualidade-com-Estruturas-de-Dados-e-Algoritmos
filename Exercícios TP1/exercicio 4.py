
array = [2, 4, 6, 8, 10, 12, 13]


numero = 8


passos = 0
esquerda, direita = 0, len(array) - 1
while esquerda <= direita:
    passos += 1
    meio = (esquerda + direita) // 2
    if array[meio] == numero:
        break
    elif array[meio] < numero:
        esquerda = meio + 1
    else:
        direita = meio - 1


print(passos)

# Saída: 2
# A busca binária localizou o número 8 em 2 passos.
