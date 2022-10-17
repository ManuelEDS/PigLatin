import ply.lex as lex

tokens = [
    "PALABRA",
    "NOPALABRA"
]

def t_PALABRA(t):
    r'[a-zA-Z]+'
    t.type = "PALABRA"
    return t

def t_NOPALABRA(t):
    r'[0-9]+'
    t.type = "NOPALABRA"
    return t

def t_error(t):
    t.lexer.skip(1)

archivo = open("entrada.txt" , "r")

lexer = lex.lex()

entrada = archivo.read()
print(f"El texto introducido es:\n\n{entrada}\n")
lexer.input(entrada)


def comienzaPorVocal(palabra):
    # se identifica si la primera letra es vocal o no, si lo es se retorna True
    palabra = palabra.lower()
    if palabra[0] == "a":
        return True
    elif palabra[0] == "e":
        return True
    elif palabra[0] == "i":
        return True
    elif palabra[0] == "o":
        return True
    elif palabra[0] == "u":
        return True 
    else:
        return False

def traducir(palabra):
    # se traduce la palabra a pig latin segun se pide
    if comienzaPorVocal(palabra):
        return palabra + "ay"
    else:
        return palabra[1:] + palabra[0] + "ay"

print("Los tokens introducidos son: \n")
resultado = ""
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    if tok.type == "PALABRA":
        resultado += traducir(tok.value) + " "
    else: 
        resultado += tok.value + " "

print(f"\nEl resultado es \"{resultado}\"")
archivo.close()

archivo = open("entrada.txt" , "w")
archivo.write(resultado)

