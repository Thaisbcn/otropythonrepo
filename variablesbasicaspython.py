"""
Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""


mensaje="¡Hola, Mundo!."
print(mensaje)

""""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
mensaje="¡Hola, Mundo!."
mensaje="Hello world!"
print(mensaje)
#REASIGNAMOS un nuevo valor a la variable

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
var_string="Hola"
print(var_string, type(var_string))
var_int=125
print(var_int, type(var_int))
var_float=10.5
print (var_float, type (var_float))
var_bool=True
print (var_bool, type(var_bool))
var_list=[1,43.5,"tres"]#ordenada e immutable
print(var_list, type(var_list))
var_tuple=(1,43.5,"tres")#no modificable
print(var_tuple, type(var_tuple))
var_dict = {"clave1": "valor1", "clave2": "hola", "clave3": [1, 2, 3]}
print (var_dict, type(var_dict))
var_set = var_set = {1, 2, 3, 4, 5} #no permite duplicados
print(var_set, type (var_set))
print(
    f"Variable: {var_string}, Tipo: {type(var_string)}\n"
    f"Variable: {var_int}, Tipo: {type(var_int)}\n"
    f"Variable: {var_float}, Tipo: {type(var_float)}\n"
    f"Variable: {var_bool}, Tipo: {type(var_bool)}\n"
    f"Variable: {var_list}, Tipo: {type(var_list)}\n"
    f"Variable: {var_tuple}, Tipo: {type(var_tuple)}\n"
    f"Variable: {var_dict}, Tipo: {type(var_dict)}\n"
    f"Variable: {var_set}, Tipo: {type(var_set)}")
