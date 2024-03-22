import random

def codigo_destino(destino):
    diccionario = {
        None : "000",
        "M"  : "001",
        "D"  : "010",
        "MD" : "011",
        "A"  : "100",
        "AM" : "101",
        "AD" : "110",
        "ADM": "111"
    }

    return diccionario[destino]

def codigo_operacion(operacion):

    #operacion = ''.join(operacion.split())

    diccionario = {
        None : None,
        "0"  :  "0101010",
        "1"  :  "0111111",
        "-1" :  "0111010",
        "D"  :  "0001100",
        "A"  :  "0110000",
        "M"  :  "1110000",
        "!D" :  "0001101",
        "!A" :  "0110001",
        "!M" :  "1110001",
        "-D" :  "0001111",
        "-A" :  "0110011",
        "-M" :  "1110011",
        "D+1":  "0011111",
        "A+1":  "0110111",
        "M+1":  "1110111",
        "D-1":  "0001110",
        "A-1":  "0110010",
        "M-1":  "1110010",
        "D+A":  "0000010",
        "D+M":  "1000010",
        "D-A":  "0010011",
        "D-M":  "1010011",
        "A-D":  "0000111",
        "M-D":  "1000111",
        "D&A":  "0000000",
        "D&M":  "1000000",
        "D|A":  "0010101",
        "D|M":  "1010101"
    }

    return diccionario[operacion]

def codigo_salto(salto):
    diccionario = {
        None  : "000",
        "JGT" : "001",
        "JEQ" : "010",
        "JGE" : "011",
        "JLT" : "100",
        "JNE" : "101",
        "JLE" : "110",
        "JMP" : "111"
    }

    return diccionario[salto]

def codigo_valor(valor, diccionario):
    binario = ""
    valor = valor.strip()
    if valor.isdigit():
        binario =  bin(int(valor))[2:]
    elif valor in diccionario:
        binario =  bin(diccionario[valor])[2:]

    while(len(binario) != 15):
        binario = "0"+ binario
    
    return binario

def agregar_al_diccionario(diccionario, lineas):
    contador = 0;
    for linea in lineas:
        if(linea.tipo != 'L'):
            contador = contador +1
        else:
            etiqueta = linea.get_etiqueta()
            diccionario[etiqueta] = contador
    
    return diccionario

def agregar_segundo(diccionario, lineas):
    contador = 16
    for linea in lineas:
        if linea.tipo == 'A' and not (linea.get_valor() in diccionario):
            if not linea.get_valor().isdigit():
                diccionario[linea.get_valor()] = contador
                contador = contador + 1
    return diccionario
            