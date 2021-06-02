from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

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
institucion1 = input(" Digite Nombre de la Institucion")
institucion1 = str(institucion1)
today = date.today()
day = today.strftime("%d/%m/%Y")
day = str(day)
ID1 = input(" Digite ID del Proceso")
ID1 = str(ID1)
objeto = input(" El objeto del proceso")
objeto = str(objeto)





def SNCCF042_InformacionOferenteSDA(selectedcompany, template,institucion1,day,ID1):

    template = template
    document = MailMerge(template)

    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1
    )
    document.write(ID1+'SNCCF034_PresentacionDeOferta' + selectedcompany +'.docx')


def SNCCF034_PresentacionDeOferta(selectedcompany, template,institucion1,day,ID1,objeto):
    
    template = template
    document = MailMerge(template)
    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1,
        Objeto = objeto
    )
    document.write(ID1 +'SNCCF042_InformacionOferente' + selectedcompany +'.docx')

def OfertaSDA(template,institucion1,day,ID1,objeto):
    SNCCF034_PresentacionDeOferta(template,institucion1,day,ID1,objeto)

