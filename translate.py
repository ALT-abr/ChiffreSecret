from dectoinaire import Encode

def Translate(text):
    resultat = []
    for letter in text:
        if letter in Encode:
            resultat.append(Encode[letter])
        else:
            resultat.append(letter)
        
    return "".join(resultat)