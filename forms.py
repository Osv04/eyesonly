from __future__ import print_function
from datetime import date
from re import template
from mailmerge import MailMerge
from datetime import date

def SNCCF042_InformacionOferente(selectedcompany,templat,institucion1,day,ID1):

    document = MailMerge(templat)

    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1
    )
    document.write(ID1+'SNCCF042_InformacionOferente' + selectedcompany +'.docx')

def SNCCF034_PresentacionDeOferta(selectedcompany,template,institucion1,day,ID1,objeto,vigencia):
    
    template = template
    document = MailMerge(template)
    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1,
        Objeto = objeto,
        Vigencia = vigencia,
    )
    document.write(ID1 +'SNCCF034_PresentacionDeOferta' + selectedcompany +'.docx')

def SNCCF033_OfertaEconomica(selectedcompany,template,institucion1,day,ID1,objeto):
    
    template = template
    document = MailMerge(template)
    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1,
        Objeto = objeto
    )
    document.write(ID1 +'SNCCF033_OfertaEconomica' + selectedcompany +'.docx')

def SNCCD044_EnfoqueMetodologiayPlandeTrabajo(selectedcompany,template,institucion1,day,ID1,objeto):
    
    template = template
    document = MailMerge(template)
    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1,
        Objeto = objeto
    )
    document.write(ID1 +'SNCCF044_EnfoqueMetodologiayPlandeTrabajo' + selectedcompany +'.docx')

def SNCCD049_ExperienciaComoContratista(selectedcompany,template,institucion1,day,ID1):
    
    template = template
    document = MailMerge(template)
    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1,
 
    )
    document.write(ID1 +'SNCCD049_ExperienciaComoContratista' + selectedcompany +'.docx')

def OfertaTecnica(selectedcompany,template,institucion1,day,ID1,objeto):
    
    template = template
    document = MailMerge(template)
    document.merge(
      Institucion = institucion1,
        Date = day,
        Id = ID1,
        Objeto = objeto
    )
    document.write(ID1 +'OFERTATECNICA' + selectedcompany +'.docx')

def SNCCF036_Equipos_Oferente(selectedcompany,template,institucion1,day,ID1):
    template = template
    document = MailMerge(template)
    document.merge(
      Institucion = institucion1,
        Date = day,
        Id = ID1,
    )
    document.write(ID1 +'SNCCF036_Equipos_Oferente' + selectedcompany +'.docx') 