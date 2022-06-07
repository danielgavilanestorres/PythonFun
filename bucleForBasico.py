"""
1. Basico: imprime todos los numeros enteros del 0 a 150
"""
for numeros in range(151):
    print(numeros)

"""
2. Multiplos de 5: imprime todos los multiplos de 5 entre 5 y 1000
"""
for multiplesCinco in range (5, 1001):
    if (multiplesCinco % 5 == 0):
        print(multiplesCinco)

"""
3. Contar, a la manera del Dojo: imprime numeros enteros del 1 al 100. Si es divisible por 5 imprime Coding en su lugar. 
Si es divisible por 10 imprime Coding Dojo
"""
for conteoDojo in range (1, 101):
    if (conteoDojo % 10 == 0):
        print("Coding Dojo")
    elif (conteoDojo % 5 == 0):
        print("Coding")
    else:
        print(conteoDojo)

"""
4. Whoa. Es un gran idiota: agrega los enteros impares del 0 500000, e imprime la suma final
"""
impares = 1
sumaImpares = 0
while(impares < 500000):
    sumaImpares += impares;
    print(impares)
    impares += 2
print(sumaImpares)

"""
5. Cuenta regresiva de a 4. Imprime numeros positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4
"""
for regresiva in range(2018, 0, -4):
    print(regresiva)

"""
6. Contador Flexible: Establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime
solo los enteros que sean  multiplos de mult.
"""
lowNum = 2
highNum = 9
mult = 3
for contFlexible in range(lowNum, highNum+1):
    if (contFlexible % mult == 0):
        print(contFlexible)
