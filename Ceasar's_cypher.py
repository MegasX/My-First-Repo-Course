from string import ascii_lowercase
list(ascii_lowercase)

def encode(message, shift):
    alpha = ascii_lowercase
    shifted = ascii_lowercase[shift:] + ascii_lowercase[:shift]
    encoded_message = []
    message = message.lower()
	for letter in message:
		if letter in alpha:
		    encoded_message.append(shifted[ascii_lowercase.index(letter)])
		else : 
			encoded_message.append(letter)
	    return ''.join(encoded_message)

def decode(message, shift):
	alpha = ascii_lowercase
    shifted = ascii_lowercase[-shift:] + ascii_lowercase[:-shift]
    decoded_message = []
    message = message.lower()
	for letter in message:
		decoded_message.append(shifted[ascii_lowercase.index(letter)])
	    return ''.join(encoded_message)

	return decoded_message


OR---------

def decode(message, shift):
	return encode(message, -shift)




---------------------------------------------OR------------------------


from string import ascii_lowercase
list(ascii_lowercase)

def encode(message, shift):
    alpha = ascii_lowercase
    shifted = ascii_lowercase[shift:] + ascii_lowercase[:shift]
    encoder = dict(zip(alpha, shifted))
    encoded_message = []
    message = message.lower()
	for letter in message:
		encoded_message.append(encoder.get(letter, letter))
	return ''.join(encoded_message)

def decode(message, shift):
	return encode(message, -shift)









