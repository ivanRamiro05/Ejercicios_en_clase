#VERIFICACIÓN DE TRIANGULO
print("---------------------------------------------------")
print("---------BIENVENIDO MI ESTIMADO APRENDIZ-----------")
print("-¿QUIERES SABER SI A ,B Y C FORMAN UN TRIANGULO?---")
print("---------------------------------------------------")

#input
A=int(input("ingrese el valor de A: "))
B=int(input("ingrese el valor de B: "))
C=int(input("ingrese el valor de C: "))

#PROCESSING

if A>0 and B>0 and C>0:
    print("A, B y C cumplen la condición")
else:
    print ("porfavor solo ingrese numeros positivos y != a letras")
if A==B and B==C:
    print("triangulo")
elif A+B>C and A+C>B and B+C>C:
    print("triangulo")
else:
    print("los lados mencionados no corresponen a un triangulo")
#OUTPUT "el output esta integrado en el processing"
#fin