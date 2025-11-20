import sympy as sp
import random

def menu():
    print("_" * 93)
    print("Primeiramente é necessário criar a matriz, selecione a opção correspondente à 'criar matriz'!")
    print(" '1' - Criar matriz")
    print(" '2' - Alocação First fit")
    print(" '3' - Alocação Best fit")
    print(" '4' - Alocação Worst fit")
    print(" '5' - Desalocação")
    print("_" * 93)

#O usuário deverá informar o número de
#linhas e colunas para a alocação inicial da memória. Deve-se garantir que o número de linhas
#e colunas sejam maiores que zero.
X = sp.symbols('X')
escolha = [X, ' ']
def matriz(lin, col):
    matriz = []
    for i in range(0, lin):
        lin = []
        for j in range(0, col):
            novo = random.choice(escolha)
            lin.append(novo)
        matriz.append(lin)
    print('_' * 50)
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    return matriz
#Esta estratégia de alocação encontra o primeiro espaço em memória cujo
#tamanho seja igual ou maior que o desejado e então realiza a alocação. No exemplo acima,
#caso uma alocação de tamanho 3 seja requisitada, ela seria realizada nas posições (0, 17),
#(0,18) e (0,19)
def ffit():
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    print('_' * 50)
    d = int(input("Número de espaços que deseja alocar:"))
    print('_' * 50)
    lin = l
    col = c
    n = 0
    i = 0
    j = 0
    for i in range(0, lin):
        if n == d:
            break
        for j in range(0, col):
            if matriz[i][j] == X:
                n = 0
            else:
                n = n + 1
                if n == d:
                    if i == lin - 1:
                        i = i + 1
                    else:
                        pass
                    break
    if n != d:
        print("Alocamento impossível, tente novamente!")
        exit()
    else:
        i = i - 1
        for r in range(0, d):
            matriz[i][j] = X
            if r == d - 1:
                j = 0
            else:
                j = j - 1
            if j == -1:
                j = col - 1
                i = i - 1
                matriz[i][j] = X
            else:
                continue
    print("Matriz com os espaços alocados")
    print('_' * 50)
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    return matriz
#Esta estratégia busca um espaço disponível que seja o mais adequado
#para o tamanho requisitado. Isto é, caso uma alocação de tamanho ‘n’ seja requisitada, um
#espaço de tamanho ‘n’ será buscado. Caso ele exista, a alocação será realizada. Caso
#contrário, um espaço de tamanho (n+1) será buscado e assim por diante, até que um espaço
#seja encontrado ou que seja determinado que nenhum espaço esteja disponível. No exemplo
#acima, caso uma alocação de tamanho 3 seja requisitada, ela deverá ocorrer nas posições (2,6), (2,7) e (2,8).
def bfit():
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    print('_' * 50)
    d = int(input("Número de espaços que deseja alocar:"))
    print('_' * 50)
    inicio = d
    lin = l
    col = c
    i = 0
    j = 0
    n = 0
    v = 0
    L = []
    while L == []:
        for i in range(0, lin):
            for j in range(0, col):
                if matriz[i][j] == X:
                    n = 0
                else:
                    n = n + 1
                    if n == d:
                        v = 1
                        if (j + 1) == col and i == (lin - 1):
                            j = col - 1
                            i = lin - 1
                            L.append(n)
                            L.append(i)
                            L.append(j)
                            break
                        elif (j + 1) == col:
                            j = 0
                            i = i + 1
                            if matriz[i][j] != X:
                                continue
                            else:
                                j = col - 1
                                i = i - 1
                                L.append(n)
                                L.append(i)
                                L.append(j)
                                break
                        else:
                            j = j + 1
                            if matriz[i][j] != X:
                                continue
                            else:
                                j = j - 1
                                L.append(n)
                                L.append(i)
                                L.append(j)
                                break
        if v == 1:
            d = d + 1
        elif v == 0:
            print("Alocamento impossível")
            exit()
    else:
        i = L[1]
        j = L[2]
        for r in range(0, inicio):
            matriz[i][j] = X
            if r == inicio - 1:
                j = 0
            else:
                j = j - 1
            if j == -1:
                j = col - 1
                i = i - 1
                matriz[i][j] = X
            else:
                continue
    print("Matriz com os espaços alocados")
    print('-' * 100)
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    return matriz
#O algoritmo de alocação worst fit realiza a alocação de memória na
#região com maior espaço livre contanto que ela seja suficientemente grande para comportar
#o tamanho requisitado. No exemplo acima, caso uma alocação de tamanho 2 seja requisitada,
#ela ocorrerá nas posições (0,17), (0,18), (0,19) e (1,0)
def wfit():
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    print('-' * 100)
    d = int(input("Número de espaços para alocação: "))
    print('-' * 100)
    lin = l
    col = c
    inicio = d
    i = 0
    j = 0
    n = 0
    L = []
    for i in range(0, lin):
        for j in range(0, col):
            if matriz[i][j] == X:
                n = 0
            else:
                n = n + 1
                if n >= d:
                    if (j + 1) == col and i == (lin - 1):
                        j = col - 1
                        i = lin - 1
                        L.clear()
                        L.append(n)
                        L.append(i)
                        L.append(j)
                        d = d + 1
                        n = 0
                    elif (j + 1) == col:
                        j = 0
                        i = i + 1
                        if matriz[i][j] != X:
                            d = d + 1
                            continue
                        else:
                            j = col - 1
                            i = i - 1
                            L.clear()
                            L.append(n)
                            L.append(i)
                            L.append(j)
                            d = d + 1
                            n = 0
                    else:
                        j = j + 1
                        if matriz[i][j] != X:
                            d = d + 1
                            continue
                        else:
                            j = j - 1
                            L.clear()
                            L.append(n)
                            L.append(i)
                            L.append(j)
                            d = d + 1
                            n = 0
    if L[0] < inicio:
        print("Alocamento Worst fit inexistente, tente novamente!")
        exit()
    else:
        i = L[1]
        j = L[2]
        for r in range(0, inicio):
            matriz[i][j] = X
            if r == inicio - 1:
                j = 0
            else:
                j = j - 1
            if j == -1:
                j = col - 1
                i = i - 1
                matriz[i][j] = X
            else:
                continue
    print("Matriz com os espaços alocados")
    print('-' * 100)
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    return matriz
#O usuário deverá informar as coordenadas de início e fim para realizar a
#desalocação de memória. Deve-se garantir que todas as coordenadas informadas sejam
#válidas antes de realizar a desalocação
def des():
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    print('-' * 100)
    z = int(input("Digite o número da linha que deseja iniciar o desalocamento: "))
    y = int(input("Digite o número da coluna que deseja inicar do desalocamento: "))
    n = int(input("Digite o número da linha que deseja encerrar o desalocamento: "))
    m = int(input("Digite o número da coluna que deseja encerrar o desalocamento: "))
    print('-' * 100)
    lin = l
    col = c
    if z < 0 or z > (lin - 1):
        print("Desalocamento impossível, tente novamente!")
        exit()
    elif y < 0 or y > (col - 1):
        print("Desalocamento impossível, tente novamente!")
        exit()
    elif n < 0 or n > (lin - 1):
        print("Desalocamento impossível, tente novamente!")
        exit()
    elif m < 0 or m > (col - 1):
        print("Desalocamento impossível, tente novamente!")
        exit()
    elif z > n:
        print("Desalocamento impossível, tente novamente!")
        exit()
    else:
        pass

    while z != n:
        for y in range(y, col):
            matriz[z][x] = ' '
        z = z + 1
        y = 0
    if z == n:
        while y != m + 1:
            matriz[z][y] = ' '
            y = y + 1
    print("Matriz com os espaços desalocados")
    print('-' * 100)
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            print(f'[{matriz[lin][col]}]', end='')
        print()
    return matriz
while True:
    menu()
    x = int(input("Escolha a opção desejada: "))
    print('_' * 33)
    if x == 1:
        l = int(input("Selecione o número de linhas da matriz: "))
        if l == 0:
            print("Selecione um número maior que 0, tente novamente!")
            exit()
        c = int(input("Selecione o número de colunas da matriz: "))
        if c == 0:
            print("Selecione um número maior que 0, tente novamente!")
            exit()
        matriz = matriz(l, c)
    elif x == 2:
        matriz = ffit()
    elif x == 3:
        matriz = bfit()
    elif x == 4:
        matriz = wfit()
    elif x == 5:
        matriz = des()