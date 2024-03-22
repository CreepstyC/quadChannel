import sys
import parseador as ps
import codificador as cd

diccionario = {
    "SCREEN" : 16384,
    "KBD" : 24576,
    "SP" : 0,
    "LCL" : 1,
    "ARG" : 2,
    "THIS" : 3,
    "THAT": 4
}

for i in range(16):
    llave = "R" + str(i)
    diccionario[llave] = i


def main(diccionario):
    lineas = []
    nombre_archivo = sys.argv[1]
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = ps.parseo(linea)
            if(linea.tipo == None):
                continue
            lineas.append(linea)
    
    diccionario = cd.agregar_al_diccionario(diccionario, lineas)
    diccionario = cd.agregar_segundo(diccionario, lineas)

    nombre_archivo_hack = nombre_archivo[:nombre_archivo.find('.asm')] + ".hack"
    with open(nombre_archivo_hack, 'w') as archivo_hack:
        for i in lineas:
            instruccion = ""
            if(i.tipo == 'C'):
                instruccion = "111" + cd.codigo_operacion(i.get_operacion()) + cd.codigo_destino(i.get_destino()) + cd.codigo_salto(i.get_salto())
                archivo_hack.write(instruccion + '\n')
            elif(i.tipo == 'A'):
                instruccion= cd.codigo_valor(i.get_valor(), diccionario)
                instruccion = "0" +  instruccion
                archivo_hack.write(instruccion + '\n')
    

if __name__ == '__main__':
    main(diccionario)