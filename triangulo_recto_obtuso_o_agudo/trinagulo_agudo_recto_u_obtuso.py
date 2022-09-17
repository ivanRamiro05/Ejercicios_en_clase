#Verificar que tipo de triangulo se forma segun sus angulos

print("---------------------------")
print("--------BIENVENIDO --------")
print("---------------------------")

#input
X=int(input("ingrese el valor del angulo x: "))
Y=int(input("ingrese el valor del angulo y: "))
Z=int(input("ingrese el valor del angulo z: "))

#Processing

if X>0 and Y>0 and Z>0:
    print("los valores de x,y,z son validos continua porfavor")
else:
    print("ingresa solo numeros naturales ") 
if X + Y + Z== 180:
      print("continuemos")
else:
    print("la suma de los angulos obtenidos no corresponden a un triangulo")
if X+Y<90  or Z + Y <90 or X + Z <90:
    print("El triangulo es obtuso")
elif X+Y == 90 or Y+Z == 90 or Z+X ==90:
    print("El triangulo es recto")
elif X+Y>90 or Y+Z>90 or Z+Y>90:
    print("el triangulo es agudo")
    #El output esta dentro del processing
#fin