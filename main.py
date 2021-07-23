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
vigencia = input(" La duracion de la oferta ")


if(selectedcompany == "Ducto Limpio S.D. SRL"):
    #UBICACION DE LOS ARCHIVOS TEMPLATE DE CADA EMPRESA
    template1 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\SNCCD044_EnfoqueMetodologiayPlandeTrabajo_DL.docx"
    template2 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\SNCCD049_Experienciacontratista_DL.docx"
    template3 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\SNCCF033_OfertaEconomica_DL.docx"
    template4 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\SNCCF034_PresentacionDeOferta_DL.docx"
    template5 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\SNCCF042_InformacionOferente_DL.docx"
    template6 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\Formulario Oferta Tecnica.docx"
    template7 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL\\SNCCF036_Equipos_Oferente_DL.docx"
    try:
        directory = institucion1+ID1
        parent_dir = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\DL"
        path = os.path.join(parent_dir,directory)
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    #LLAMADA DE LOS METODOS DE DESARROLLO PARA CADA EMPRESA
    forms.SNCCD044_EnfoqueMetodologiayPlandeTrabajo("Ducto Limpio S.D. SRL",template1,institucion1,day,ID1,objeto)
    forms.SNCCD049_ExperienciaComoContratista("Ducto Limpio S.D. SRL",template2, institucion1,day,ID1)
    forms.SNCCF033_OfertaEconomica("Ducto Limpio S.D. SRL", template3,institucion1,day,ID1,objeto)
    forms.SNCCF034_PresentacionDeOferta("Ducto Limpio S.D. SRL",template4,institucion1,day,ID1,objeto,vigencia)
    forms.SNCCF042_InformacionOferente("Ducto Limpio S.D. SRL",template5,institucion1,day,ID1)
    forms.OfertaTecnica("Ducto Limpio S.D. SRL",template6,institucion1,day,ID1,objeto)
    forms.SNCCF036_Equipos_Oferente("Ducto Limpio S.D. SRL",template7,institucion1,day,ID1)

    #SE DEBE GUARDAR EN LA CARPETA AUTO GENERADA

    # os.rename(path + "\\" + ID1 +'SNCCF042_PresentacionDeOferta' + selectedcompany +'.docx', ID1 +'SNCCF042_PresentacionDeOferta' + selectedcompany +'.docx')

if(selectedcompany == "Automaki SRL"):
    #UBICACION DE LOS ARCHIVOS TEMPLATE DE CADA EMPRESA
    #OBSERVACIONES CREAR TEMPLATE 2 PARA AUTOMAKI
    template1 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\AUTOMAKI\\SNCC_D_044_Enfoque_Metodología_y_Plan_de_Trabajo.docx"
    #template2 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_D_049_Experiencia_Como_Contratista.docx"
    template3 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\AUTOMAKI\\SNCC_F033_Formulario_Oferta_Economica.docx"
    template4 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\AUTOMAKI\\SNCC_F034_Presentacion_de_Oferta_Automaki.docx"
    template5 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\AUTOMAKI\\SNCC_F042_Formulario Oferente Automaki.docx"
    template6 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\AUTOMAKI\\Formulario Oferta Tecnica.docx"
    try:
        directory = institucion1+ID1
        parent_dir = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\AUTOMAKI"
        path = os.path.join(parent_dir,directory)
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    #LLAMADA DE LOS METODOS DE DESARROLLO PARA CADA EMPRESA
    forms.SNCCD044_EnfoqueMetodologiayPlandeTrabajo("Automaki SRL",template1,institucion1,day,ID1,objeto)
    #forms.SNCCD049_ExperienciaComoContratista("Automaki SRL",template2, institucion1,day,ID1)
    forms.SNCCF033_OfertaEconomica("Automaki SRL", template3,institucion1,day,ID1,objeto)
    forms.SNCCF034_PresentacionDeOferta("Automaki SRL",template4,institucion1,day,ID1,objeto,vigencia)
    forms.SNCCF042_InformacionOferente("Automaki SRL",template5,institucion1,day,ID1)
    forms.OfertaTecnica("Automaki SRL",template6,institucion1,day,ID1,objeto)

if(selectedcompany == "Servicios Diversos Arnaud SRL"):
    #UBICACION DE LOS ARCHIVOS TEMPLATE DE CADA EMPRESA
    template1 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCCD044_EnfoqueMetodologíayPlandeTrabajo.docx"
    template2 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_D_049_Experiencia_Como_Contratista.docx"
    template3 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F033_Formulario_Oferta_Economica.docx"
    template4 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F034_Presentacion_de_Oferta_SDA.docx"
    template5 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F042_Formulario Oferente SDA.docx"
    #Ofertatecnica que fue creado por mi 
    template7 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCC_F036_Equipos_Oferente.docx"
    # try:
    #     directory = institucion1+ID1
    #     parent_dir = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA"
    #     path = os.path.join(parent_dir,directory)
    #     os.mkdir(path) 
    # except OSError as error: 
    #     print(error)

    #LLAMADA DE LOS METODOS DE DESARROLLO PARA CADA EMPRESA
    forms.SNCCD044_EnfoqueMetodologiayPlandeTrabajo("Servicios Diversos Arnaud SRL",template1,institucion1,day,ID1,objeto)
    forms.SNCCD049_ExperienciaComoContratista("Servicios Diversos Arnaud SRL",template2, institucion1,day,ID1)
    forms.SNCCF033_OfertaEconomica("Servicios Diversos Arnaud SRL", template3,institucion1,day,ID1,objeto)
    forms.SNCCF034_PresentacionDeOferta("Servicios Diversos Arnaud SRL",template4,institucion1,day,ID1,objeto,vigencia)
    forms.SNCCF042_InformacionOferente("Servicios Diversos Arnaud SRL",template5,institucion1,day,ID1)
    forms.SNCCF036_Equipos_Oferente("Servicios Diversos Arnaud SRL",template7,institucion1,day,ID1)
    #SE DEBE GUARDAR EN LA CARPETA AUTO GENERADA

    # os.rename(path + "\\" + ID1 +'SNCCF042_PresentacionDeOferta' + selectedcompany +'.docx', ID1 +'SNCCF042_PresentacionDeOferta' + selectedcompany +'.docx')

if(selectedcompany == "Red Dot Tech SAS"):
    #UBICACION DE LOS ARCHIVOS TEMPLATE DE CADA EMPRESA
    template1 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\NT\\SNCCD044_EnfoqueMetodologíayPlandeTrabajo_NT.docx"
    template2 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\NT\\SNCCD049_Experienciacontratista_NT.docx"
    template3 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\NT\\SNCCF033_OfertaEconomica_NT.docx"
    template4 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\NT\\SNCCF034_PresentacionDeOferta_NT.docx"
    template5 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\NT\\SNCCF042_InformacionOferente_NT.docx"
    template6 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\NT\\Formulario Oferta Tecnica.docx"
    #Ofertatecnica que fue creado por mi 
    template7 = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA\\SNCCF036_Equipos_Oferente_NT.docx"
    # try:
    #     directory = institucion1+ID1
    #     parent_dir = "C:\\Users\\oscar\\Documents\\Proyectos\\xProjectOVA-EYESONLY\\SDA"
    #     path = os.path.join(parent_dir,directory)
    #     os.mkdir(path) 
    # except OSError as error: 
    #     print(error)

    #LLAMADA DE LOS METODOS DE DESARROLLO PARA CADA EMPRESA
    forms.SNCCD044_EnfoqueMetodologiayPlandeTrabajo("Red Dot Tech SAS",template1,institucion1,day,ID1,objeto)
    forms.SNCCD049_ExperienciaComoContratista("Red Dot Tech SAS",template2, institucion1,day,ID1)
    forms.SNCCF033_OfertaEconomica("Red Dot Tech SAS", template3,institucion1,day,ID1,objeto)
    forms.SNCCF034_PresentacionDeOferta("Red Dot Tech SAS",template4,institucion1,day,ID1,objeto,vigencia)
    forms.SNCCF042_InformacionOferente("Red Dot Tech SAS",template5,institucion1,day,ID1)
    forms.SNCCF036_Equipos_Oferente("Red Dot Tech SAS",template7,institucion1,day,ID1)
    forms.OfertaTecnica("Red Dot Tech SAS",template6,institucion1,day,ID1,objeto)
    
    #SE DEBE GUARDAR EN LA CARPETA AUTO GENERADA