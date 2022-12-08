def quadrado(lista_numeros):
    lista_respostas =[]
    for numero in lista_numeros:
        lista_respostas.append(numero **2)
    return lista_respostas


def cubo(lista_numeros):
    lista_respostas =[]
    for numero in lista_numeros:
        lista_respostas.append(numero **3)
    return lista_respostas

lista_valores=[]

for valor in range(10):
    lista_valores.append(int(input("Escolha um numero ")))

print(lista_valores)

dicionario ={
"lista padrão": lista_valores,
"lista quadrada":quadrado(lista_valores),
"lista cubica": cubo(lista_valores)
}
