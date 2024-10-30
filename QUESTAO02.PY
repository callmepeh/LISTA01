def fatiterativo(num):
    if num == 0 or num == 1:
        return 1
    else:
        fat = 1
        while num > 1:
            fat *= num
            num -= 1
        return fat
    
n = int(input("Digite o numero que deseja calcular o fatorial: "))

print(fatiterativo(n))


def fatrecursivo (num):
    if num < 2:
        return 1
    else:
       return num * fatrecursivo(num-1)
n = input("Digite o valor que voce deseja calcualar o fatorial: ")
fatrecursivo(n)