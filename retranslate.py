from dectoinaire import Decode

def Retranslate(text):
    resultat = []
    i = 0

    while i < len(text):
        if text[i] == "#" or text[i].isdigit():
            code = text[i:i+2]
            resultat.append(Decode.get(code,code))
            i+=2
        else:
            resultat.append(text[i])
            i+=1
    
    return "".join(resultat)