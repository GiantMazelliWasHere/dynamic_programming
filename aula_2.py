# Ex. 1 

'''
numeros = []

tamanho = int(input("Insira o tamanho do espaço de busca: "))

for i in range(tamanho):
    numero = float(input("Digite um número que será inserido na lista: "))
    numeros.append(numero)
    

print("Os respectivos valores são: ", numeros)
'''

#################################################################################
# Ex. 2

'''
numeros = []
tamanho = int(input("Insira o tamanho do espaço de busca: "))
i = 0


while i < tamanho:
    numero = float(input("Digite um número que será inserido na lista: "))
    numeros.append(numero)
    i+=1

print("Os respectivos valores são: ", numeros)
'''

#################################################################################
# Ex. 3

'''
lista = [10, 20, 30, 40, 50]

alvo = 30

for i in range(len(lista)):
    if lista[i] == alvo:
        print(f"O alvo {alvo} foi encontrado na posição {i}")
        break
    
else:
        print("O alvo não está na lista")
'''
        
#################################################################################
# Ex. 4

'''
lista = [10, 20 , 30 , 40 , 50]
alvo = 30
k = 0 

while k > len(lista):
    if lista[k] == alvo:
        print(f"O alvo {alvo} foi encontrado na posição {k}")
        break
    k+=1
    
else:
        print("O alvo não está na lista")
'''
        
#################################################################################
# Ex. 5

'''
def busca_linear(lista, alvo):
    
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    
    return -1

lista = [10, 20 , 30 , 40 , 50]
alvo = 30

resultado = busca_linear(lista, alvo)

if resultado != -1:
    print(f'O alvo {alvo} está na posição {resultado}')
else:
    print("O resultado não está na lista")
'''
    
#################################################################################
# Ex. 6

'''
def busca_linear(lista, alvo):
    i = 0
    
    while i < len(lista):
        if lista[i] == alvo:
            return i
            break
        
        i+=1
    
    return -1

lista = [10, 20 , 30 , 40 , 50]
alvo = 30

resultado = busca_linear(lista, alvo)

if resultado != -1:
    print(f'O alvo {alvo} está na posição {resultado}')
else:
    print("O resultado não está na lista")
'''


#################################################################################
# Ex. 7 - for

'''
nomes = []
tamanho = int(input("Insira o tamanho do espaço de busca: "))

for i in range(tamanho):
    nome = input("Digite o nome que será inserido na lista: ")
    nome = nome.capitalize()
    nomes.append(nome)
    print(nomes)

print("Os respectivos nomes são: ", nomes)

alvo = "Nathan"

for i in range(len(nomes)):
    if nomes[i] == alvo:
        print(f"O alvo {alvo} está na lista Nomes na posição {i}")
        break
    
else:
    print("O alvo não está na lista")
'''
    
#################################################################################
# Ex. 8 - while

nomes = []
tamanho = int(input("Insira o tamanho do espaço de busca: "))
i = 0

while i < tamanho:
    nome = input("Digite o nome que será inserido na lista: ")
    nome = nome.capitalize()
    nomes.append(nome)
    print(nomes)
    i+=1
    

print("Os respectivos nomes são: ", nomes)

alvo = "Nathan"
k = 0

while k < len(nomes):
    if nomes[k] == alvo:
        print(f"O gostoso do alvo {alvo} foi encontardo na posição {i}")
        break
    k+=1

else:
    print("O gostoso do alvo não está na lista")
    
#################################################################################
# Ex. Estrutura para remover acento

from unicode import unicode

