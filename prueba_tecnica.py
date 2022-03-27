# Prueba Técnica - MasCobranzas - Marzo 2022

# Utilizar la librería Pandas para la resolución de los siguientes items:

# Importación de la Librería:
import pandas as pd 

#Código

#----------------------------------------#
#1 - Lectura del archivo.
df= pd.read_excel(r'base_de_datos.xlsx')
#Código

#----------------------------------------#
#2 - Mostrar el nombre de las columnas que contiene la base de datos.
df.columns.values
#Código


#----------------------------------------#
#3 - Realizar un validador de columnas tal que evalúe los nombres de las columnas mostradas 
# en el punto anterior y muestre un mensaje diciendo "columnas válidas" si se encuentra todas
# estas columnas, si hay alguna que está faltando o tiene distinto nombre, que informe de qué 
# columna se trata.

#Código

#----------------------------------------#
#4 - Mostrar la cantidad de filas y columnas de la base de datos.

#Código

#----------------------------------------#
#5 - Mostrar la información de los primeros 10 registros.

#Código

#----------------------------------------#
#6 - Generar una nueva columna con el nombre de "Nombre Completo" donde sea una concatenación 
# de las columnas "Apellido" y "Nombre". Esta nueva columna debe ser la 2da columna 
# de la base de datos, eliminando las 2 columnas mencionadas.

#Código

#----------------------------------------#
#7 - La columna H e I de la base de datos contiene los nombres de "Fch ingreso" y "Fch nacimiento". 
# Renombrar estas columnas por su nombre correcto: "Fecha Ingreso" y "Fecha Nacimiento".

#Código

#----------------------------------------#
#8 - A estas columnas ("Fecha Ingreso" y "Fecha Nacimiento") reemplazar todos sus valores "/" por
# "-". De forma tal que la fecha quede especificada con el formato de la siguiente manera: dd-mm-aaaa

#Código

#----------------------------------------#
#9 - Generar una nueva columna a la derecha del resto, llamada "Actividad" donde todos sus valores 
# sean "Activo".

#Código

#----------------------------------------#
#10 - Generar un nuevo excel con las modificaciones realizadas en los puntos anteriores.

#Código

#----------------------------------------#