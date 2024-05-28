
class Token:
    def __init__(self, token, tipo, nombre):
        self.token = token
        self.tipo = tipo
        self.nombre = nombre
    
    def __repr__(self):
        return f'Token: {self.token}, Tipo de token: {self.tipo}, Valor del token: {self.nombre}'

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.tokens = []
        self.metodosIncompletos = []
        self.pos = 0
        self.current_char = self.texto[self.pos] if self.texto else None
        
        # Definir los diccionarios
        self.operadores_aritmeticos = {
            "combina_con": "Operador aritmético de suma",
            "corta_a": "Operador aritmético de resta",
            "duplicado_de": "Operador aritmético de multiplicacion",
            "destaca_en": "Operador aritmético de potencia",
            "inspirado_en": "Operador aritmético de raíz",
            "contrasta_con": "Operador aritmético de negativo"
        }
        self.operadores_relacionales = {
            "imitacion_de": "Operador lógico de igualdad",
            "mejor_que": "Operador lógico mayor que",
            "peor_que": "Operador lógico menor que"
        }
        self.operadores_logicos = {
            "o": "Operador lógico 'o'",
            "y": "Operador lógico 'y'"
        }
        self.separador_sentencias = {
            "\n": "Separación de sentencias"
        }
        self.operador_asignacion = {
            "equivale_a": "Operador de asignación"
        }
        self.metodos = {
            "elegir_outfit": "Empezar decision (if)",
            "otro_outfit": "Otra decisión (else)",
            "outfit_elegido": "Finalizar decision",
            "buscar_estilo": "Empezar ciclo",
            "estilo_elegido": "Finalizar ciclo"
        }
        self.identificadores = {
            "patron": "Funcion",
            "accesorio": "Variable",
            "nuevo_outfit": "Clase"
        }
        self.valores_logicos = {
            "a_la_moda": "Verdadero lógico",
            "no_a_la_moda": "Falso lógico"
        }
        self.tipos_de_variables = {
            "completo": "Variable de tipo entero",
            "incompleto": "Variable de tipo real",
            "etiqueta": "Variable de tipo cadena",
            "talla": "Variable de tipo caracter",
            "de_moda": "Variable de tipo booleana"
        }
        self.tipos_de_variables = {
            "completo": "Variable de tipo entero",
            "incompleto": "Variable de tipo real",
            "etiqueta": "Variable de tipo cadena",
            "talla": "Variable de tipo caracter",
            "de_moda": "Variable de tipo booleana"
        }
        self.letras = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
        self.numeros = {"0","1","2","3","4","5","6","7","8","9"}
        self.simbolos = {"$"}

    def esCadena(self, word):
        word_separada = list(word)
        contador = 0
        for i in word_separada:
            if i in self.numeros or i in self.simbolos:
                i = 1
                contador = contador+1
        sintaxis = 0
        if len(word_separada)==1:
            self.tokens.append(Token(word, "Desconocido", "No tiene la sintaxis correcta de cadena y no termina en *"))
        if i in self.letras or i in self.simbolos or contador!=3:
            sintaxis = sintaxis+10
        pos = len(word_separada)-1
        if word_separada[pos] != "*":
            sintaxis = sintaxis+1
        if sintaxis == 11:
            self.tokens.append(Token(word, "Desconocido", "No tiene la sintaxis correcta de cadena y no termina en *"))
        elif sintaxis == 10:
            self.tokens.append(Token(word, "Desconocido", "No tiene la sintaxis correcta de cadena"))
        elif sintaxis == 1:
            self.tokens.append(Token(word, "Desconocido", "No termina en *"))
        else: 
            self.tokens.append(Token(word, "Valor de asignacion", "Es una cadena*"))

    def esEnteroOReal(self, word):
        word_separada = list(word)
        contadorEntero = 0
        contadorPuntos = 0
        contadorDecimal = 0
        for i in word_separada:
            if i in self.numeros and contadorPuntos==0:
                contadorEntero = 1
            elif i == ".":
                contadorPuntos = contadorPuntos+1
            elif i in self.numeros and contadorPuntos==1:
                contadorDecimal =1
            else:
                return self.tokens.append(Token(word, "Desconocido", "Desconocido"))

        if contadorPuntos > 1:
            self.tokens.append(Token(word, "Desconocido", "No tiene la sintaxis correcta de entero o real"))
        elif contadorPuntos == 1:
            if contadorEntero == 1 and contadorDecimal == 1:
                self.tokens.append(Token(word, "Valor de asignación", "Es un real"))
            else:
                self.tokens.append(Token(word, "Desconocido", "No tiene la sintaxis correcta de entero o real"))
        elif contadorPuntos == 0:
            self.tokens.append(Token(word, "Valor de asignación", "Es un entero"))

    def separarPalabrasYReconocer(self):
        words = self.texto.split()
        for word in words:
            print(word)
            if word in self.operadores_aritmeticos:
                self.tokens.append(Token(word, "Operador aritmético", self.operadores_aritmeticos[word]))
            elif word in self.operadores_relacionales:
                self.tokens.append(Token(word, "Operador relacional", self.operadores_relacionales[word]))
            elif word in self.operadores_logicos:
                self.tokens.append(Token(word, "Operador lógico", self.operadores_logicos[word]))
            elif word in self.metodos:
                self.tokens.append(Token(word, "Método", self.metodos[word]))
            elif word in self.identificadores:
                self.tokens.append(Token(word, "Identificador", self.identificadores[word]))
            elif word in self.valores_logicos:
                self.tokens.append(Token(word, "Valores lógicos", self.valores_logicos[word]))
            elif word in self.tipos_de_variables:
                self.tokens.append(Token(word, "Tipo de variable", self.tipos_de_variables[word]))
            elif word in self.operador_asignacion:
                self.tokens.append(Token(word, "Operador de asignación", self.operador_asignacion[word]))
            elif word.startswith("*"):
                self.esCadena(word)
            elif word[0] in self.numeros:
                self.esEnteroOReal(word)
            elif word.startswith("+"):
                if len(word) ==3:
                    if word.endswith("+"):
                        if word[1] in self.numeros or word in self.letras or word in self.simbolos and word.endswith("+"):
                            print(len(word))
                            self.tokens.append(Token(word, "Valor de asignación", "Es un caracter"))
                        else:
                            self.tokens.append(Token(word, "Desconocido", "Sintaxis incorrecta de caracter"))
                    else: self.tokens.append(Token(word, "Desconocido", "Sintaxis incorrecta de caracter"))
                else:
                    self.tokens.append(Token(word, "Desconocido", "Sintaxis incorrecta de caracter"))
            else:
                self.tokens.append(Token(word, "Desconocido", "Desconocido"))
        
        return self.tokens
    
    def obtenerMetodosIncompletos(self):
        words = self.texto.split()
        inif = words.count("elegir_outfit")
        finif = words.count("outfit_elegido")
        incic = words.count("buscar_estilo")
        fincic = words.count("estilo_elegido")
        cantif = inif-finif
        cantcic = incic-fincic
        if cantif!=0:
            self.metodosIncompletos.append("Las decisiones no se han cerrado correctamente")
        else:
            self.metodosIncompletos.append("Las decisiones se han cerrado correctamente")
        if cantcic!=0:
            self.metodosIncompletos.append("Los ciclos no se han cerrado correctamente")
        else:
            self.metodosIncompletos.append("Los ciclos se han cerrado correctamente")
        return self.metodosIncompletos
    
    def crearMatrizTokens(self):
        matriz = []
        for token in self.tokens:
            fila = [token.token, token.tipo, token.nombre]
            matriz.append(fila)
        return matriz
    
    def crearMatrizMetodos(self):
        matriz = []
        for metodo in self.metodosIncompletos:
            matriz.append(metodo)
        return matriz
    
        

def main():
    text = """
    elegir_outfit
    nuevo_outfit combina_con +
    si accesorio mejor_que 5 
    entonces
        accesorio corta_a 1
    fin
    outfit_elegido
    """
    print(text)
    
    lexer = Lexer(text)
    tokens = lexer.separarPalabrasYReconocer()
    for token in tokens:
        print(token)

    metodos = lexer.obtenerMetodosIncompletos()
    matriz2 = lexer.crearMatrizMetodos()
    matriz = lexer.crearMatrizTokens()

    print(matriz)
    print(matriz2)

    metodos = lexer.obtenerMetodosIncompletos()
    for metodo in metodos:
        print(metodo)




if __name__ == '__main__':
    main()
