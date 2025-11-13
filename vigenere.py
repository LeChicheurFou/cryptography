import string

def cesar_cipher(text, key, cipher=True):
	if type(text) == str and type(key) == int:
		return "".join([chr((ord(char) + (1 if cipher else -1)* key) % 1_114_112)\
				  												for char in text])
	else:
		raise(TypeError)


def hack_cesar_cipher(crypted_text, alphabet):
	if type(crypted_text) == str and type(alphabet) == str:
		for possible_key in range(0, 1_114_112):
			possible_uncryption = cesar_cipher(crypted_text, possible_key, cipher=False)
			if possible_uncryption[0] in alphabet:
				print(possible_key)
				print(possible_uncryption)
				print("_"*20)
	else:
		raise(TypeError)


def vigenere_cipher(text, password, cipher=True):
	list_of_keys = [ord(char) for char in password]
	crypted_text = []
	for index, char in enumerate(text):
		current_key = list_of_keys[index % len(list_of_keys)]
		if cipher:
			crypted_text.append(cesar_cipher(char , current_key))
		else:
			crypted_text.append(cesar_cipher(char , current_key, cipher=False))
	return "".join(crypted_text)


# def vigenere_uncipher(crypted_text , password):
# 	list_of_keys = [ord(char) for char in password]
# 	decrypted_text = []
# 	for index, char in enumerate(crypted_text):
# 		current_key = list_of_keys[index % len(list_of_keys)]
# 		decrypted_text.append(cesar_uncipher(char , current_key))
# 	return "".join(decrypted_text)

print(vigenere_cipher("test","b"))
print(vigenere_cipher("ÖÇÕÖ","b",False))