import random

cartas_espadas = list(range(1, 14))

random.shuffle(cartas_espadas)


mao = []


while cartas_espadas:

    carta = cartas_espadas.pop()
    

    inserida = False
    for i in range(len(mao)):
        if carta < mao[i]:
            mao.insert(i, carta)
            inserida = True
            break
    if not inserida:

        mao.append(carta)


print(mao)
input()
# Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# As cartas estão agora ordenadas na "mão" final.
