def ispar(x):
    return x % 2 == 0
#equivalente da função usando o lambda:
par = (lambda x: x % 2 == 0)
print(par)
#verifica se é impar
impar = (lambda y: y % 2 != 0)
#verifica se é zero 
zero = (lambda z: z == 0)

quadrado = (lambda q: q**2)
quadrado2 = (lambda q,y: q ** y)

lista = []
while True:
   num = lista.append = int(input)
   if num < 0:
      exit()
    
pares = list(filter(lambda a: a % 2 == 0 and a > 0, lista))
impares = list(filter(lambda b: b % 2 != 0, lista))
zero = list(filter(lambda c: c == 0, lista))

sorted(pares)
sorted(impares)

pares.str = str(pares)
impares.str = str(impares)
zero.str = str(zero) 


concatena = pares.str + zero.str + impares.str 

n = int(input("Digite um valor"))

divisiveis = [x for x in range(1,n+1) if x % n == 0]

if len(divisiveis) > 2:
    print("Não é primo")
else:
    print("É primo")

