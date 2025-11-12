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

def brut_force(test_words , number_keys):
    globals_solutions = []   
    for potentiel_key in range(0,number_keys):
        solution_brut_force = dechiffre_cesar(test_words, potentiel_key)
        globals_solutions.append(solution_brut_force)
    return globals_solutions

#print(brut_force("Boupojo", len(alphabet)))