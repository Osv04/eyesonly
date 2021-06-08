from __future__ import print_function
from re import template
from mailmerge import MailMerge
from datetime import date
import forms 
import os

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




if(selectedcompany == "Servicios Diversos Arnaud SRL"):
    #UBICACION DE LOS ARCHIVOS TEMPLATE DE CADA EMPRESA
    template1 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_D_044_Enfoque_Metodología_y_Plan_de_Trabajo.docx"
    template2 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_D_049_Experiencia_Como_Contratista.docx"
    template3 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F033_Formulario_Oferta_Economica.docx"
    template4 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F034_Presentacion_de_Oferta_SDA.docx"
    template5 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F042_Formulario Oferente SDA"
    try:
        directory = institucion1+ID1
        parent_dir = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA"
        path = os.path.join(parent_dir,directory)
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    #LLAMADA DE LOS METODOS DE DESARROLLO PARA CADA EMPRESA
    forms.SNCCD044_EnfoqueMetodologiayPlandeTrabajo("Servicios Diversos Arnaud SRL",template1,institucion1,day,ID1,objeto)
    forms.SNCCD049_ExperienciaComoContratista("Servicios Diversos Arnaud SRL",template2, institucion1,day,ID1)
    forms.SNCCF033_OfertaEconomica("Servicios Diversos Arnaud SRL", template3,institucion1,day,ID1)
    forms.SNCCF034_PresentacionDeOferta("Servicios Diversos Arnaud SRL",template4,institucion1,day,ID1)
    forms.SNCCF042_InformacionOferente("Servicios Diversos Arnaud SRL",template5,institucion1,day,ID1)
    #SE DEBE GUARDAR EN LA CARPETA AUTO GENERADA

    # os.rename(path + "\\" + ID1 +'SNCCF042_PresentacionDeOferta' + selectedcompany +'.docx', ID1 +'SNCCF042_PresentacionDeOferta' + selectedcompany +'.docx')


