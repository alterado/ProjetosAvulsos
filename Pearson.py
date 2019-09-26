import math

N=int(input("Quantos eventos? (N) "))
nomex=input("Qual é a variável x? ")
nomey=input("Qual é a variável y? ")
lista=[]
k=0
while len(lista)<N:
    listaelemento=[]
    x=float(input("Qual o valor de {} do evento {}? ".format(nomex, k)))
    y=float(input("Qual o valor de {} do evento {}?".format(nomey, k)))
    print()
    print()
    listaelemento.append(x)
    listaelemento.append(y)
    lista.append(listaelemento)
    k+=1

def somax(lista):
    soma=0
    k=0
    while k<len(lista):
        soma=soma+lista[k][0]
        k+=1
    return soma

def somay(lista):
    soma=0
    k=0
    while k < len(lista):
        soma=soma+lista[k][1]
        k+=1
    return soma

def somaxx(lista):
    soma=0
    k=0
    while k<len(lista):
        soma=soma+(lista[k][0])**2
        k+=1
    return soma

def somaxy(lista):
    soma=0
    k=0
    while k<len(lista):
        soma=soma+((lista[k][0])*(lista[k][1]))
        k+=1
    return soma

def somayy(lista):
    soma=0
    k=0
    while k<len(lista):
        soma=soma+(lista[k][1])**2
        k+=1
    return soma


correlacao= ((N*somaxy(lista)) - ((somax(lista)) * (somay(lista))))/math.sqrt(((N*somaxx(lista)-(somax(lista)**2)) * ((N*somayy(lista)) - (somay(lista))**2)))

print("A correlação (r) entre as variáveis {} e {} é: {}".format(nomex,nomey,correlacao))
