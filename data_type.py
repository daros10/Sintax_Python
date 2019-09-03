#some of important data type in python 

# --------- STRINGS -----------------------------------
# You can write Strings of differents forms 

"Hello World"
'Hello World'
'''Hello World'''
"""Hello World"""

cadena1 = "Hello World"
cadena2 = 'Hello World'
cadena3 = '''Hello World'''
cadena4 = """Hello World"""

print(cadena1)
print(cadena2)
print(cadena3)
print(cadena4)

# Concat Strings with +
print(cadena1 + cadena2)

#-------- NUMBERS --------------------------------------

#integer
numEntero = 10
print(numEntero)

#float
numFlotante = 10.5
print(numFlotante)

#--------- BOOLEANS ---------------------------
boolTrue = True
print(boolTrue)

boolFalse = False
print(boolFalse)

#--------- LIST ----------------------------
myList = [10, 20, 30, 40, 50]
print(myList)

myListString = ["Hola", "prro", ":v"]

myMixingList = ["String", 10, 15.20, True, myList]

emptyList = []

#------- TUPLES -----------------------------
#Las tuplas son como las listas, la diferencia 
#radica en que estas no pueden ser modificadas 
#sus valores son para siempre.
#Las tuplas con inmutables 

myTuple = (10, 20, 30, 40)

emptyTuple = ()

#------- DICTIONARIES --------------------
#Los diccionarios son como un Map en Dart 
#Los diccionarios son como un JSON conformado 
# por clave y valor

myDictionary = {
    "name"     : "Dario",
    "lastname" : "Herrera",
    "nickname" : "Daro",
    "phone"    : 10
}

print(myDictionary)


#----- None --------

myNoneType = None
print(myNoneType)


