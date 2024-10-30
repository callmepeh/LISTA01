lucro_total = 200

reducao = 0.50
quantidade = 120
preco = 5.00


for preco in range(9):
    quantidade += 26
    preco -= 0.50

    lucro_total = preco * quantidade
    print(f"O preco do ingresso = {preco}, quantidade = {quantidade}, lucro = {lucro_total}")
     


