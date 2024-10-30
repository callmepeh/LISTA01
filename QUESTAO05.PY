def num_bi(num):
    numbi = ''

    while (num > 0):
        resto = num % 2 
        numbi = str(resto) + numbi
        num = num // 2
    return print(numbi)
num = int(input("Digite o numero que deseja converter em binario: "))
num_bi (num)