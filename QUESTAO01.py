print("Imformações:")
print(" 1 - TRIANGULO\n 2 - QUADRADO\n 3 - CÍRCULO")

forma = input("Informe a forma do seu objeto:\n")
if forma == 1: 
    base = input("Digite o tamanho da base do triangulo:\n")
    altura = input("Digite a altura do triangulo:\n")
    areatriangulo = (base * altura)/2
    print("A area do seu triangulo é:", areatriangulo)
elif forma == 2:
    lado1 = input("Informa o comprimento de um lado")
    lado2 = input("Informe o comprimento do outro lado")
    areaquadrado = lado1 * lado2 
    print("A area do seu quadrado é:", areaquadrado)

else:
    comprimento = ("Informe o diametro do circulo:\n")
    areadocirculo = (comprimento/2) * (comprimento/2) * 3,14
    print("A area do seu circulo é:", areadocirculo)


