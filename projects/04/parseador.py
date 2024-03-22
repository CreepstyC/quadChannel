class parseo():
    def __init__(self, linea):
        self.linea = linea.strip()
        self.tipo = None
        self.limpiar()
        self.verificar()

    def verificar(self):
        if self.linea.startswith('//') or self.linea == '':
            self.tipo = None
        elif self.linea.startswith('@'):
            self.tipo = 'A'
        elif self.linea.startswith('('):
            self.tipo = 'L'
        else:
            self.tipo = 'C'

    def limpiar(self):
        indice = self.linea.find('//')

        if(indice == 0):
            self.linea = ''
        elif indice != -1:
            self.linea = self.linea[:indice]

        self.linea = self.linea.strip()

    def get_valor(self):
        if(self.tipo != 'A'):
            return None
        return self.linea[1:].split(' ')[0]
    
    def get_destino(self):
        indice = self.linea.find('=')

        if(self.tipo != 'C' or indice == -1):
            return None
        
        return self.linea[:indice]
    
    def get_operacion(self):
        indice_igual = self.linea.find("=")
        indice_punto_coma = self.linea.find(";")

        if(self.tipo != 'C'):
            return None
        
        if(indice_igual != -1 and indice_punto_coma != -1):
            return self.linea[indice_igual+1:indice_punto_coma].strip()
        elif(indice_igual == -1 and indice_punto_coma != -1 ):
            return self.linea[:indice_punto_coma].strip()
        elif(indice_igual != -1 and indice_punto_coma == -1):
            return self.linea[indice_igual+1:].strip()
        elif(indice_igual == -1 and indice_punto_coma == -1):
            return self.linea.strip()
        
    def get_salto(self):
        indice_punto_coma = self.linea.find(";")

        if(self.tipo != 'C' or indice_punto_coma == -1):
            return None
            
        return self.linea[indice_punto_coma+1:].strip()
    
    def get_etiqueta(self):
        indice_1 = self.linea.find("(")
        indice_2 = self.linea.find(")")

        if(self.tipo != "L"):
            return None
        
        if(indice_1 != -1 and indice_2 != -1):
            return self.linea[indice_1+1:indice_2].strip()
        
        return None