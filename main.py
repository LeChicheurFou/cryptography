import string as st

alphabet = st.printable

def chiffre_cesar(char, key):
    if type(key) in {int , float}:
        return "".join([alphabet[(alphabet.index(element) + (key)) % len(alphabet)]\
                for element in char])
    else:
        raise(TypeError)

#print(chiffre_cesar("Antonin", 1))


def dechiffre_cesar(chiffrement, key):
    return chiffre_cesar(chiffrement, -key)


#print (dechiffre_cesar("Boupojo", 1))