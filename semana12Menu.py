print("Escoge una de las opciones de nuestro menú: 1) DESAYUNO 2) ALMUERZO 3) CENA")

def DESAYUNO():
    return "Huevos, frijoles, plátanos, crema y pan; acompañado de juego natural. ------": 55.00

def ALMUERZO():
    return "Carne asada, papas fritas, chirmol, frijoles, cebollitas, tortillas y guacamol; acompañada de gaseosa o jugo natural. ------ ": 77.00

def CENA():
    return "Panes universitarios, acompañado de algun postre de la pastelería de la casa. La bebida puede ser caliente o fría a tu elección. ------":60.00
def TOTAL():
    return "Su total a pagar es de:"

def default_case():
    return "Opción no valida"

def switch_case(argument):
    switcher = {
        1: DESAYUNO,
        2: ALMUERZO,
        3: CENA,
        4: TOTAL,
    }
    func = switcher.get(argument, default_case)
    return func()

opcion = input()
d=int(opcion)
print(switch_case(d))