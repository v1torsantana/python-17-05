def acha_menor(lista):
    print(lista)
    menor = lista[0]
    local_menor = 0
    for i in range(len(lista)):
        #print(f"Agora vou testar se lista[{i}], {lista[i]} > {maior}")
        if lista[i]<menor:
            #print(f"Troquei {maior} por {lista[i]}")
            menor = lista[i]
            local_menor = i
    return local_menor
#lista = [10,20,30,15]
#carros = ["up","celta","golf","corsa"]
#indice_maior = acha_maior([10,40,90,54,761,200])
#print(indice_maior)
#indice_maior = acha_maior([13,10,7665,76,761,200,34,55,567])
#print(indice_maior)
#carro_mais_caro = carros[indice_maior]
#print(carro_mais_caro)

lista_x = []
lista_y = []
x = -10
while x<10:
    f = x**2 -5*x + 6
    lista_x.append(x)
    lista_y.append(f)
    x+=0.1

indice_menor_f = acha_menor(lista_y)
menor_valor_f = lista_y[indice_menor_f]
print(menor_valor_f)
x_vertice = lista_x[indice_menor_f]
print(x_vertice)