name = "Alejandro"
print(type(name)) #Usamos la palabra "type" para que nos indique que tipo de dato es el que colocamos dentro de la variable.
name = 12
print(type(name))  # En estas lineas de codigo le pedimos que indique que tipo de variable es la que estamos usando
name = True
print(type(name))

#PARTE 2
print("Alejandro" + "Camas") #En esta linea le pedimos que nos sume esos strings para poder tener nombre y apellido.
print(10 + 20)
print("Alejandro" + "21")


age = 12
print("Mi edad es " + str(age)) #aqui le indicamos con la funcion "str" que es un string
print(f"Mi edad es {age}")

age = input("Introduzca su edad  => ")
print(type(age))
age = int(age)
age += 10
print(f"Su edad serara {age} dentro de 10 años")# la "f" significa la funcion format(formato)

