tupla = ("1", 2)
tupla.count(2) # quantas vezes o valor 2 aparece
tupla.index(2) # indice do valor 2

minha_tupla=("Germano", 24, "inutil", "inutil_2", "inutil_3")

nome, idade ,*coisas_inuteis = minha_tupla # Aponta para dentro da tupla, o * pega o resto

nome, idade = idade, nome # troca o valor das variaveis

# Empacotamento
x=(1,2,3,4,5)
*a,b,c =x # (1,2,3),4,5
a,*b,c =x # 1,(2,3,4),5
a,b,*c =x # 1,2,(3,4,5)
