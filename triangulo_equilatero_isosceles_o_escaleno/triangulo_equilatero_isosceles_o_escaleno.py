# verificar si el triangulo es equilatero isoceles o escaleno


print("-------------------------")
print("------Bienvenido---------")
print("-------------------------")

#input

A=int(input("ingrese el valor del lado de a: "))
B=int(input("ingrese el valor del lado de b: "))
C=int(input("ingrese el valor del lado de c: "))

#processing
if A>0 and B>0 and C>0:
    print("los valores ingrresados  A,B y C son correctos")
else:
    print("favor ingresar solo numeros positivos")
if A !=B and B!=C and C !=A:
    print("el triangulo es escaleno")
elif A==B and A!=C  or B==C and B!=A or C==A and C!=B:
    print("el triangulo es isosceles")
elif A==B==C:
    print("el triangulo es equilatero")
#fin