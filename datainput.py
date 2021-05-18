from datetime import date

#DESCRIPCION DE VARIABLES
class Data():
    institucion1 = input("Digite Nombre de la Institucion")
    institucion1 = str(institucion1)
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    day = str(day)
    ID1 = input("Digite ID del Proceso")
    ID1 = str(ID1)
