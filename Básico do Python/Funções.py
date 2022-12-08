# Função Nomeada
# sum = soma
# len = tamanho

def diga_ola (nome_da_pessoa): # Define bloco de codigo, qual argumento recebe e retorna
    return f"Olá {nome_da_pessoa}"

print(diga_ola("germano")) # Chama a função passando o argumento

def soma (numero_1,numero_2):
    return numero_1+numero_2

print(soma(12,14))

def media (lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)

print(media([1,2,3,4,5]))

def nome(argumento_posicional,*pacote_de_argumentos): # recebe um argumento, e um argumento cheio de argumentos
    print(argumento_posicional,pacote_de_argumentos)

print(nome("Python",1,2,3,4,5,6)) # argumento argumento_posicional = Python / pacote_de_argumentos = (1,2,3,4,5,6)

def nome_2(argumento_nomeado="não tem nada",**pacote_nomeado):
    print(argumento_nomeado,pacote_nomeado)

nome_2() # retorna não tem nada e {}
nome_2("a") # retorna a e {}
nome_2(letra="a") # retorna não tem nada e {"letra": "a"}
