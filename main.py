from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

institucion1 = input("Digite Nombre de la Institucion")
institucion1 = str(institucion1)
today = date.today()
day = today.strftime("%d/%m/%Y")
day = str(day)
ID1 = input("Digite ID del Proceso")
ID1 = str(ID1)

def SNCCF042_InformacionOferenteSDA(institucion1,day,ID1):

    template = "SNCC_F042_Formulario Oferente SDA.docx"
    document = MailMerge(template)

    document.merge(
        Institucion = institucion1,
        Date = day,
        Id = ID1
    )
    document.write('test-output.docx')


def SNCCF034_PresentacionDeOferta_SDA():
    template = "SNCC_F042_Formulario Oferente SDA.docx"
    document = MailMerge(template)

    
    
