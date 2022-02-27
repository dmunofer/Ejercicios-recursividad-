#Ejercicio 6

def palindromorec(palabra):

    a,b = 'áéíóúüñÁÉÍÓÚÜ','aeiouunAEIOUU'
    palabra = palabra.replace(" ","")
    trans = str.maketrans(a,b)
    string = palabra.translate(trans)
    if len(string)<2:                                      # Si la palabra tiene menos de 2 caracteres siempre será palindroma
        return True
    elif string.lower()[0]!=string.lower()[-1]:            # Comparamos el primer y ultimo caracter
        return False
    return palindromorec(string[1:-1])                     # Repetimos el proceso recursivamente quitando el primer y último caracter