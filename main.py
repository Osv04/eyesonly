from __future__ import print_function
from re import template
from mailmerge import MailMerge
from datetime import date
import forms 

print("*****************************************************")
print("Propiedad de Oscar Veloz Arencibia")
print("*****************************************************")
print(" Empresas")
print(""" 1) Automaki SRL
 2) Ducto Limpio S.D. SRL
 3) Servicios Diversos Arnaud SRL
 4) Red Dot Tech SAS
 5) Latin American Service SRL """)
print("*****************************************************")

empresas = ["Automaki SRL","Ducto Limpio S.D. SRL","Servicios Diversos Arnaud SRL","Red Dot Tech SAS","Latin American Service SRL"]
eleccion = input("Digite que tipo de empresa va trabajar ")
eleccion = int(eleccion) - 1 
#Ayuda para poder poner nombre de los docs
selectedcompany = empresas[eleccion]


#Declaracion de variables estandar en proceso de licitacion
institucion1 = input(" Digite Nombre de la Institucion ")
institucion1 = str(institucion1)
today = date.today()
day = today.strftime("%d/%m/%Y")
day = str(day)
ID1 = input(" Digite ID del Proceso ")
objeto = input(" El objeto del proceso ")

templat = 'SDA\SNCC_F042_Formulario Oferente SDA.docx'


if(selectedcompany == "Automaki SRL"):
    #template = 
    def OfertaSDA(template,institucion1,day,ID1,objeto):
        forms.SNCCF034_PresentacionDeOferta(template,institucion1,day,ID1,objeto)

forms.SNCCF042_InformacionOferenteSDA(selectedcompany,templat,institucion1,day,ID1)
