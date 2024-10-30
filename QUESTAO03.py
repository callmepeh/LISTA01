def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fat = 1
        while num > 1:
            fat *= num
            num -= 1
        return fat


n = input("Digite o número que será agrupado")
p = input("Digite em quantas vezes ele será agrupado")

arranjo = fatorial(n) / fatorial(n - p)
combinação = fatorial(n)/fatorial(p) * fatorial(n-p)
print(f"O arranjo de {n} agrupados de {p} a {p} é igual a:")





