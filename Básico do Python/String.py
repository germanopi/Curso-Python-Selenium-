# Concatenação de String
print ("Minha mensagem") # Mostra uma string na tela
print ("Minha mensagem pulando linha \n") # Mostra uma string na tela e pula linha
print ("""
        Minha
        mensagem
        multilinha
        """)
print("oi " * 20 ) # Imprime a string 20 vezes
nome = input ("Qual seu nome? ") # Escreve uma string e espera receber uma entrada em string
idade = input ("Qual sua idade? ")
pessoa = nome + " e tem "+ idade + " anos" # Concatena string com variavel que também seja string
print ("Você é : " + pessoa)
print (type(idade)) # Retorna o tipo da variavel
idade=int(idade) # Altera o tipo da variavel para inteiro
print (idade) # imprime a variavel
print (f"A sua idade é: {idade}") # F-string concatena {expressões} em string
print (f"A sua idade depois de 2 anos será: {idade + 2}\n" # F-string, pulando linha
       f"A sua idade depois de 5 anos será: {idade + 5}\n"
       f"A sua idade depois de 10 anos será: {idade + 10} e seu nome é {nome}\n"
)
print("A sua Idade depois de 20 será: {}".format(idade+20)) # String.format concatena expressões no {} da string
del idade # Destroi o objeto

# Métodos
palavra = "Chocolate"
palavra.count("o") # 2
palavra.partition("o") # retorna a tupla ("Ch","o","c","o","late")
palavra.split("o") # retorna a lista ["Ch","c","late"]
palavra.lower() # Chocolate
palavra.index("t") # 8
palavra.replace ("o","K") # ChKcKlate
nomes = "Germano Douglas Ribero Vinicius Andre"
nomes.split(" ") # ["Germano", "Douglas", "Ribero", "Vinicius","Andre"]

# Decisão
mensagem = "Eduardo foi na casa do amigo"
if "casa" in mensagem:
    print("Ele foi para casa")
else:
    print("Ele foi para outro lugar")
