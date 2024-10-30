def primo(n):
    num = n
    cont = 0
    if n > 0:
        for cont in (1,n+1):
            if (n % cont == 0):
                cont += 1 
    if cont > 2: 
        return True
    else: 
        return False
    
def imprimeprimo(a, z):
    count = 0
    for num in (a,z+1):
        if primo(num) == True:
           print(num)
           count += 1
    if count == 0:
        print("Não existe nenhum numero primo dentro desse intervalo")

