    #2-4 aplicacion de lower(minuscula), upper(mayuscula), title(mayus. inical: nombres)

nombre1 = ("naTAli sanaBRia")
print("hola " + nombre1 + ", que haces?")

print(nombre1.lower())

print(nombre1.upper())

print(nombre1.title())

    #2-5 #2-6

nombre2 = ("steve jobs")
nombre2 = (nombre2.title())
mensaje = ( "dijo una vez: Tu trabajo va a llenar gran parte de tu vida, la única manera de estar realmente satisfecho es hacer lo que creas que es un gran trabajo y la única manera de hacerlo es amar lo que haces")

print (nombre2 + mensaje)

    #2-7 strip eliminar espacios al inicio y al final,(tmb, .ltrip y .rstrip)

nombre3 = (" joaquin ")
nombre3 = nombre3.strip()
print(nombre3)

    #NUMEROS 2-8 operaciones matematicas

print(5+3)
print(10-2)
print(16/2)
print(4*2)

    # error "str": indicar que python lea un numero como string

numero_favorito = 6
print("mi número favorito es: " + str(numero_favorito))   

    #LISTAS elementos de una lista

      #     0   1    2    3    4   
letras = ["a", "b", "c", "d", "e" ]
print(letras)
print(letras[0])
print(letras[0].title())  

#    -1 es el ultimo de la lista. -2 penultimo. etc

print(letras[-1])

nota1 = ("La tercera letra del abecedario es: " + (letras[2].title()) + ("."))
print(nota1)

#   3-2 creo una lista y hago mensajes con  sus partes

nombres = ["gael", "owen", "natali"]
print(nombres)

mensaje_gael = " esta comiendo cereal."
mensaje_owen = " esta dibujando."
mensaje_natali = " esta viendo una película."

print((nombres[0].title()) + mensaje_gael)
print((nombres[1].title()) + mensaje_owen)
print((nombres[2].title()) + mensaje_natali)

#   cambiar elemento d una lista 

nombres[0] = "joaquin"
print(nombres)

# .append: añadir elemento AL FINAL de la lista

nombres.append("emilia") 
nombres.append("gael")
print(nombres)

#  .insert: añadir elemento EN CUALQ POSICION(menos final) de la lista

nombres.insert(2, "marina") 
print(nombres)

#   del: eliminar elementos de una lista PERMANENTEMENTE.

del nombres[0]
print(nombres)

#   .pop(): eliminar elementos, pero los almaceno en una papelera.

papelera_nombres = nombres.pop()
print(nombres)
print(papelera_nombres)

#   .remove(): eliminar by valor
personas= ["gael", "emilia", "owen","joaquin","marina","natali"]
print(personas)

personas.remove("natali")
personas.remove("emilia")
personas.remove("marina")
personas = str(personas)
print("estos son nombres masculinos: "+ personas)

Personas = ["gael", "emilia", "owen","joaquin","marina","natali"]

Personas.remove("gael")
Personas.remove("joaquin")
Personas.remove("owen")
Personas = str(Personas)
print("Estos son nombres femeninos: " + Personas)

#   3-5 lista de invitados

print("lista de invitados:")
lista_de_invitados = ["natali", "gael","owen","emilia"]
print(lista_de_invitados)
print("emilia no puede")
lista_de_invitados[3] = "marina"
print(lista_de_invitados)

print("conseguí una mesa más grande, puedo invitar más gente")

(lista_de_invitados.append("paulo"))
lista_de_invitados.insert(0,"luca")
lista_de_invitados.insert(3,"matilda")

print("así quedó mi lista:")
print(lista_de_invitados)

print("la mesa grande no llega, tengo que achicar la lista")

gente_que_no_entra = lista_de_invitados.pop()

lista_de_invitados.pop("marina")
lista_de_invitados.pop("paulo")
lista_de_invitados.pop("natali")
lista_de_invitados.pop("matilda")
lista_de_invitados.pop("natali")

print(lista_de_invitados)
